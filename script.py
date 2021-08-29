from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() #Change to webdriver.Firefox() and install geckodriver, if using Firefox.

message = 'Hello! This message is sent by chatbot!' # Edit this string to change the message sent
n = 50 # Number of times message should be sent
username = 'Gaurav' # Change to the Contact name of the person to send the message to

driver.get("http://web.whatsapp.com/")
time.sleep(15)
searchbar = driver.find_element_by_class_name('_13NKt')
searchbar.send_keys(username + Keys.RETURN)
text_bar = driver.find_element_by_class_name('_1LbR4')
msgbox = text_bar.find_element_by_class_name('_13NKt')
for i in range(0,n):
    msgbox.send_keys(message + Keys.RETURN)