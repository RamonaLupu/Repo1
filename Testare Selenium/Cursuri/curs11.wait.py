# Waits
# 1. sleep
# 2. implicit wait
# 3. explicit wait

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test = webdriver.Chrome()
test.implicitly_wait(5)

test.get('https://the-internet.herokuapp.com/login')
test.maximize_window()  # maximeaza fereastra

test.find_element(By.ID, 'username').send_keys('tomsmith')
# time.sleep(5)
# test.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
# time.sleep(5)

#3.
pas = WebDriverWait(test, 5).until(EC.presence_of_element_located((By.ID, 'passsword')))
pas.send_keys('SuperSecretPassword!')





test.quit()

