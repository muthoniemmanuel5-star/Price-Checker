import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# 1. The Target: Practice site for scraping
URL = "http://toscrape.com"

def check_price():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # 2. Find the Data
    title = soup.find("h1").get_text()
    price_text = soup.find("p", class_="price_color").get_text()
    
    # Clean the price
    price = float(price_text.replace('£', ''))

    print(f"Product: {title}")
    print(f"Current Price: {price}")

    # 3. Logic: If the price is low, save it
    target_price = 60.00 # Adjusted to 60 so it triggers for this specific book (£51.77)
    if price < target_price:
        print("ACTION: Price is below target! Saving to log...")
        save_to_excel(title, price)

def save_to_excel(name, val):
    file_name = 'price_log.csv'
    data = {'Product': [name], 'Price': [val]}
    df = pd.DataFrame(data)
    
    # Check if file exists to decide if we need a header
    file_exists = os.path.isfile(file_name)
    
    # Append to CSV
    df.to_csv(file_name, mode='a', index=False, header=not file_exists)
    print(f"Saved to {file_name}")

if __name__ == "__main__":
    check_price() # This is the fix that makes the script actually run!
