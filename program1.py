import requests
from bs4 import BeautifulSoup
import re
import sqlite3

def get_product_price(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            price_element = soup.find('span', class_='ProductDetail__Price__Sell')
            if price_element:
                # Extract numeric part of the price and convert to float
                price_text = price_element.text.strip()
                price_numeric = re.search(r'\d+\.\d+', price_text)
                if price_numeric:
                    return float(price_numeric.group())
                else:
                    return "Price not found or could not be parsed."
            else:
                return "Price element not found on the page."
        else:
            return "Failed to fetch the webpage. Status code: {}".format(response.status_code)
    except Exception as e:
        return "An error occurred: {}".format(str(e))

# Example usage:
product_page_url = "https://plaza.store.supervalue.co.nz/lines/homebrand-milk-lite-3l"
price = get_product_price(product_page_url)
product_name = "milk"

# Create or connect to SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create products table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    product_name TEXT,
                    price REAL
                )''')  # Use REAL for SQLite to store floating-point numbers

# Insert data into the products table
if isinstance(price, float):
    cursor.execute("INSERT INTO products (product_name, price) VALUES (?, ?)", (product_name, price))
    conn.commit()
    print("Data insertion successful.")
    print("Price:", price)
else:
    print("Unable to insert data into the database:", price)

# Close connection
conn.close()
