import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            price_element = soup.find('span', class_='gep-price__integer')
            if price_element:
                return price_element.text.strip()
            else:
                return "Price not found on the page."
        else:
            return "Failed to fetch the webpage. Status code: {}".format(response.status_code)
    except Exception as e:
        return "An error occurred: {}".format(str(e))

# Example usage:
product_page_url = "https://www.noelleeming.co.nz/p/apple-iphone-15-128gb---black/N220866.html"
price = get_product_price(product_page_url)
print("Product Price:", price) 