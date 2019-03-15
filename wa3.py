#code to send infinite message to a group
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome('A:\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600) 

name = input('Enter the name of user or group to send infinite message: ')
msg = input("enter the msg: ")
	
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('_2S1VP')
	
	  
while (true):
 msg_box.send_keys(msg+Keys.RETURN)
 time.sleep(1)

 

