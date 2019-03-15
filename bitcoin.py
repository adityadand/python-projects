import requests
from bs4 import BeautifulSoup
while True:
 page = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
 soup = BeautifulSoup(page.content, 'html.parser')
 
 coincap = soup.find(class_="container main-section")
 coincap2 = coincap.find_all(class_="h2 text-semi-bold details-panel-item--price__value")
 btcprice = coincap2[0]
 sage = requests.get("http://www.moneycontrol.com/currency/bse-usdinr-price.html/")
 soup1 = BeautifulSoup(sage.content, 'html.parser')
 monctrl = soup1.find('span',{'class':'r_20'})
 a = btcprice.get_text()
 b = monctrl.get_text()
 print("$"+btcprice.get_text()+" bitcoin price in inr = "+a+"*"+b)
