#some of this code was written by chatGPT
# it wrote the webscrapping code and the database code
# but i changed some of the code so that i worked together
import requests
from bs4 import BeautifulSoup
import sqlite3
 
def get_product_price(url):
    try:
        #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, """headers=headers""")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            price_element = soup.find('span', class_='ProductDetail__Price__Sell')
            if price_element:
                return price_element.text.strip()
            else:
                return "Price not found on the page."
        else:
            return "Failed to fetch the webpage. Status code: {}".format(response.status_code)
    except Exception as e:
        return "An error occurred: {}".format(str(e))

 
# Example usage:
product_page_url = "https://plaza.store.supervalue.co.nz/lines/homebrand-milk-lite-3l"
price = get_product_price(product_page_url)
product_name = "milk"

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    product_name TEXT,
                    price INTERGER
                )''')
conn.commit()
conn.close()




conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO products (product_name, price) VALUES (?, ?)", (product_name, price))
conn.commit()
conn.close()
print("it worked")

