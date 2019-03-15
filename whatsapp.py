# send message from python to whatsapp + no of times + loop availability
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
	name = input('Enter the name of user or group : ')
	msg = input("enter the msg: ")
	no = int(input("enter no of time to send >>>"))
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()
	msg_box = driver.find_element_by_class_name('_2S1VP')
	i = 1 
	  
	while (i <= no):
	 msg_box.send_keys(msg+Keys.RETURN)
	 time.sleep(1)
	 i=i+1
	  
	 
	yno = input("do you want to send more message")
	 
	if (yno == "yes"):
	  main()
	  
	else:
	 exit()
	 
main()
 

