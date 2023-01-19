#/html/body/div[2]/div/div/form/div[1]/div/input  # full xpath absolut - toate elementele de la root pala la elementul selectat
#//*[@id="password"]  = xpath relativ

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

test = webdriver.Chrome()
test.get('https://the-internet.herokuapp.com/login')
test.find_element(By.XPATH, '//*[@id="password"]').send_keys(123)
time.sleep(2)

# Xpath=//tagname[@attribute='value']

test.find_element(By.XPATH, '//input[@type="text"]').send_keys('ramona')
time.sleep(2)

# xpath cu keyword contains

test.find_element(By.XPATH, "//input[contains(@name, 'pass')]").send_keys(123)

# xpath cu text

test.find_element(By.XPATH, "//i[(text()=' Login')]").click()
time.sleep(2)

# navigarea din parinte inspre copil se face cu un /
# navigarea catre un urmas care nu este direct se face cu //
# navigarea in sesns invers la frate anterior /preceding-sibiling::tag
# navigarea la urmatorul frate se face cu //
# test.find_element(By.XPATH, '//*[@id='username']/preceding-sibling::label')
#
# test.find_element(By.XPATH, "//form[@name='login']/div[1]//input").send_keys('1234')
#
# test.quit()