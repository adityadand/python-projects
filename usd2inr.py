import requests
from bs4 import BeautifulSoup
while True:
 page = requests.get("http://www.moneycontrol.com/currency/bse-usdinr-price.html/")
 soup = BeautifulSoup(page.content, 'html.parser')
 monctrl = soup.find('span',{'class':'r_20'})
 print("1 usd $ = "+(monctrl.get_text())+"inr")

 
