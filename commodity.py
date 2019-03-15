import requests
from bs4 import BeautifulSoup
while True:
page = requests.get("https://www.moneycontrol.com/commodity/gold-price.html")
soup = BeautifulSoup(page.content, 'html.parser')
gold = soup.find(class_="gr_30")
print(gold.text)
 
