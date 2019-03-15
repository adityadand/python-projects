from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome('A:\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600) 

def main():
	name = "Subscribe to beehack"
	msg = "subscribe to beehack"
	count = 1

	input('Enter anything after scanning QR code')

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	msg_box = driver.find_element_by_class_name('_2S1VP')

	for i in range(count):
		msg_box.send_keys(msg)
		button = driver.find_element_by_class_name('_35EW6')
		button.click()
		
o = 1
no = int(input("enter no of time"))
while (o <= no):
 main()
  O = O + 1