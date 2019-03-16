import requests
from bs4 import BeautifulSoup

def gold():
 page = requests.get("https://www.moneycontrol.com/commodity/gold-price.html")
 soup = BeautifulSoup(page.content, 'html.parser')
 gold = soup.find(class_="gr_30")
 print("gold price = ",gold.text)
 
def silver(): 
 page1 = requests.get("https://www.moneycontrol.com/commodity/silver-price.html")
 soup = BeautifulSoup(page1.content, 'html.parser')
 silver = soup.find(class_="gr_30")
 print("silver price =",silver.text)

def cotton():
 page2 = requests.get("https://www.moneycontrol.com/commodity/cotton-price.html")
 soup = BeautifulSoup(page2.content, 'html.parser')
 cottonprice = soup.find(class_="gr_30")
 print("cotton price =",cottonprice.text)

def crude():
 page3 = requests.get("https://www.moneycontrol.com/commodity/crudeoil-price.html")
 soup = BeautifulSoup(page3.content, 'html.parser')
 crudeoilprice = soup.find(class_="rd_30")
 print("crude oil price =",crudeoilprice.text)

def natural():
 page4 = requests.get("https://www.moneycontrol.com/commodity/naturalgas-price.html")
 soup = BeautifulSoup(page4.content, 'html.parser')
 naturalgasprice = soup.find(class_="rd_30")
 print("natural gas price =",naturalgasprice.text);

def aluminium():
 page5 = requests.get("https://www.moneycontrol.com/commodity/aluminium-price.html")
 soup = BeautifulSoup(page5.content, 'html.parser')
 aluminiumprice = soup.find(class_="rd_30")
 print("aluminium price =",aluminiumprice.text);

def copper():
 page6 = requests.get("https://www.moneycontrol.com/commodity/copper-price.html")
 soup = BeautifulSoup(page6.content, 'html.parser')
 copperprice = soup.find(class_="gr_30")
 print("copper price =",copperprice.text);


def nickel():
 page7 = requests.get("https://www.moneycontrol.com/commodity/nickel-price.html")
 soup = BeautifulSoup(page7.content, 'html.parser')
 nickelprice = soup.find(class_="rd_30")
 print("nickel price =",nickelprice.text);

def lead():
 page8 = requests.get("https://www.moneycontrol.com/commodity/lead-price.html")
 soup = BeautifulSoup(page8.content, 'html.parser')
 leadprice = soup.find(class_="rd_30")
 print("lead price =",leadprice.text);

def zinc():
 page9 = requests.get("https://www.moneycontrol.com/commodity/zinc-price.html")
 soup = BeautifulSoup(page9.content, 'html.parser')
 zincprice = soup.find(class_="rd_30")
 print("zinc price =",zincprice.text);

def mentaoil():
 page10 = requests.get("https://www.moneycontrol.com/commodity/menthaoil-price.html")
 soup = BeautifulSoup(page10.content, 'html.parser')
 menthaoilprice = soup.find(class_="rd_30")
 print("methaoil price =",menthaoilprice.text);

def rmseed():
 page11 = requests.get("https://www.moneycontrol.com/commodity/ncdex/rmseed-price.html")
 soup = BeautifulSoup(page11.content, 'html.parser')
 rmseedprice = soup.find(class_="gr_30")
 print("rape mustard price =",rmseedprice.text);

def soybean():
 page12 = requests.get("https://www.moneycontrol.com/commodity/ncdex/sybeanidr-price.html")
 soup = BeautifulSoup(page12.content, 'html.parser')
 sybeanprice = soup.find(class_="gr_30")
 print("soybean price =",sybeanprice.text);

def cocudakl():
 page13 = requests.get("https://www.moneycontrol.com/commodity/ncdex/cocudakl-price.html")
 soup = BeautifulSoup(page13.content, 'html.parser')
 cocudaklprice = soup.find(class_="gr_30")
 print("cocudakl price =",cocudaklprice.text);

def Turmeric():
 page14 = requests.get("https://www.moneycontrol.com/commodity/ncdex/tmcfgrnzm-price.html")
 soup = BeautifulSoup(page14.content, 'html.parser')
 tmcfgrnzmprice = soup.find(class_="gr_30")
 print("Turmeric price =",tmcfgrnzmprice.text);

def dhaniya():
 page15 = requests.get("https://www.moneycontrol.com/commodity/ncdex/dhaniya-price.html")
 soup = BeautifulSoup(page15.content, 'html.parser')
 dhaniyaprice = soup.find(class_="gr_30")
 print("dhaniya price =",dhaniyaprice.text);

def sugar():
 page16 = requests.get("https://www.moneycontrol.com/commodity/ncdex/sugarm-price.html")
 soup = BeautifulSoup(page16.content, 'html.parser')
 sugarmprice = soup.find(class_="gr_30")
 print("sugar price =",sugarmprice.text);
 
def jeera():
 page17 = requests.get("https://www.moneycontrol.com/commodity/ncdex/jeeraunjha-price.html")
 soup = BeautifulSoup(page17.content, 'html.parser')
 jeeraunjhaprice = soup.find(class_="gr_30")
 print("jeera price =",jeeraunjhaprice.text);

def wheat():
 page18 = requests.get("http://www.commoditiescontrol.com/live-wheat-price.html")
 soup = BeautifulSoup(page18.content, 'html.parser')
 wheatprice = soup.find(class_="data_tbl")
 print("wheat price =",wheatprice.find('td').text)

def chana():
 page19 = requests.get("http://www.commoditiescontrol.com/live-chana-price.html")
 soup = BeautifulSoup(page19.content, 'html.parser')
 chanaprice = soup.find(class_="data_tbl")
 print("chana price =",chanaprice.find('td').text)

def palmoil():
 page20 = requests.get("http://www.commoditiescontrol.com/live-palm-oil-price.html")
 soup = BeautifulSoup(page20.content, 'html.parser')
 palmoilprice = soup.find(class_="data_tbl")
 print("palm oil =",palmoilprice.find('td').text)

def potato():
 page21 = requests.get("https://www.commodityonline.com/mandiprices/potato/maharashtra/168/22")
 soup = BeautifulSoup(page21.content, 'html.parser')
 potatoprice = soup.find(class_="dt_ta_14")
 print("potato price =",potatoprice.text)

def onions():
 page22 = requests.get("https://www.commodityonline.com/mandiprices/onion/maharashtra/166/22")
 soup = BeautifulSoup(page22.content, 'html.parser')
 onionprice = soup.find(class_="dt_ta_14")
 print("onion price =",onionprice.text)


def allcommodities():
	gold()
	silver()
	cotton()
	crude()
	natural()
	aluminium()
	copper()
	nickel()
	lead()
	zinc()
	mentaoil()
	rmseed()
	soybean()
	cocudakl()
	Turmeric()
	dhaniya()
	sugar()
	jeera()
	wheat()
	chana()
	palmoil()
	potato()
	onions()


def pcomm():
 print("choose commodities")
 print("1. gold")
 print("2. silver")
 print("3. cotton")
 print("4. crude")
 print("5. natural")
 print("6. aluminium")
 print("7. copper")
 print("8. nickel")
 print("9. lead")
 print("10. zinc")
 print("11. methaoil")
 print("12. rmseed")
 print("13. soybean")
 print("14. cocudakl")
 print("15. Turmeric")
 print("16. dhaniya")
 print("17. sugar")
 print("18. jeera")
 print("19. wheat")
 print("20. chana")
 print("21. palmoil")
 print("22. potato")
 print("23. onions")
 choice = int(input())
 if (choice == 1):
	 gold()
 if (choice == 2):
	 silver()
 if (choice == 3):
	 cotton()
 if (choice == 4):
	 crude()
 if (choice == 5):
	 natural()
 if (choice == 6):
	 aluminium()
 if (choice == 7):
	 copper()
 if (choice == 8):
	 nickel()
 if (choice == 9):
	 lead()
 if (choice == 10):
	 zinc()
 if (choice == 11):
	 methaoil()	
 if (choice == 12):
	 rmseed()
 if (choice == 13):
	 soybean()
 if (choice == 14):
	 cocudakl()
 if (choice == 15):
	 Turmeric()
 if (choice == 16):
	 dhaniya()
 if (choice == 17):
	 sugar()
 if (choice == 18):
	 jeera()
 if (choice == 19):
	 wheat()
 if (choice == 20):
	 chana()
 if (choice == 21):
	 palmoil()
 if (choice == 22):
	 potato()
 if (choice == 23):
     onions()

def start():
 print("do you want to see all commodities or only particular ones")
 print("press 1 for all commodities")
 print("press 2 for particular ones")
 choose = int(input())
 if(choose == 1):
    allcommodities()
 if(choose == 2):
    pcomm()
 if(choose == 3):
 	print("fuck")

start()




