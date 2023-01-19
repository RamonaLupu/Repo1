import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

test = webdriver.Chrome()
test.get('https://the-internet.herokuapp.com/login')
test.find_element(By.TAG_NAME, 'form')
time.sleep(2)

test.find_element(By.CSS_SELECTOR, 'form >div [type="text"]').send_keys('dan')
time.sleep(3)
# test.find_element(By.CSS_SELECTOR, 'form >div [type="text"]').clear()
test.find_element(By.CSS_SELECTOR, 'form >div [type="text"]').send_keys(Keys.CONTROL + 'a')
test.find_element(By.CSS_SELECTOR, 'form >div:nth-of-type(1) input').send_keys('adela')
time.sleep(3)

test.find_element(By.CSS_SELECTOR, 'form>div:last-of-type input').send_keys('123')
time.sleep(2)

test.find_element(By.CSS_SELECTOR, 'form >div [type="text"]').clear()

test.find_element(By.CSS_SELECTOR, 'form>div:first-of-type input').send_keys('ramona')
time.sleep(2)

test.quit()

#     XPATH

