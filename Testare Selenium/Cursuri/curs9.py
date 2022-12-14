# Selectori
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# locatori in Selenium
# 1. ID
chrome_page = webdriver.Chrome() # .Chrome este clasa din pachetul Selenium
chrome_page.get('https://the-internet.herokuapp.com/login') # accesarea paginii html dorite
# time.sleep(5) # o sa opreasca pagina 5 secunde pt a putea vedea noi mai bine

chrome_page.find_element(By.ID, 'username').send_keys('Ramona')  # gasim un elelement dupa ID si tiparim stringul dat ca parametru


chrome_page.find_element(By.ID, 'password').send_keys('ramona1')
time.sleep(5)


chrome_page.find_element(By.TAG_NAME, 'button').click() # accesam elemente dupa tag_name
time.sleep(5)

chrome_page.find_element(By.LINK_TEXT, 'Elemental Selenium').click()
time.sleep(2)




chrome_page.quit() # metoda inchide toata instanta browswrului
# chrome_page.close() # metoda aceasta inchide un singur tab( cel activ din instanta de browser)



