import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

base_url = "http://quotes.toscrape.com"

def scrape_quotes():
    url = "/page/1"
    all_quotes =[]
    while url:
        res = requests.get(f"{base_url}{url}")
        print(f"Now Scrapping... {base_url}{url}.......")
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text" : quote.find(class_="text").get_text(),
                "author" : quote.find(class_="author").get_text(),
                "bio-link" :quote.find("a")["href"] 
            })
        next_button = soup.find(class_="next")
        url = next_button.find('a')['href'] if next_button else None 
        sleep(2) 
    return all_quotes

quotes = scrape_quotes()
#write quotes to csv file

with open("quotes.csv", "w") as file:
    headers = ["text", "author","bio-link"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for quote in quotes:
        csv_writer.writerow(quote)
    