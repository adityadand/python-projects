# send message to multiple groups
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome('A:\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
all_names = ['Lite hackers', 'Hacker army', 'Decption']
msg = 'multiple message testing via python'
count = 1

input('Enter anything after scanning QR code')

for name in all_names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)) and user.click()  	
    msg_box = driver.find_element_by_class_name('_2S1VP')
    msg_box.send_keys(msg + Keys.ENTER)
   
