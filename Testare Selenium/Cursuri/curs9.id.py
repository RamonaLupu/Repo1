import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(3)
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form") # putem deschide un site
time.sleep(5)
chrome.find_element(By.ID, "first-name").send_keys("Marian")
time.sleep(5)
chrome.find_element(By.ID, "last-name").send_keys("Gheorghisor")
time.sleep(5)


chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()
time.sleep(5)

chrome.quit() # inchide toata instanta browserului
# chrome.close() -> inchide un singur tab (cel activ) din instanta de browser