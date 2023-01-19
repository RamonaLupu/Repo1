import unittest
import time
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Key(unittest.TestCase):
    USERNAME = (By.ID, 'username')
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.maximize_window()
        time.sleep(3)
        self.chrome.implicitly_wait(2)

    # Definirea metodei de tearDown
    def tearDown(self) -> None:
        self.chrome.quit()

    def test_select_all(self):
        usermane = self.chrome.find_element(*self.USERNAME)
        usermane.send_keys('alabalaportocala')
        time.sleep(2)
        usermane.clear()
        time.sleep(2)
        usermane.send_keys('ala')
        time.sleep(2)
        usermane.send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        usermane.send_keys(Keys.BACKSPACE)
        time.sleep(2)

        listt = ['ala', 'bala', 'porto', 'cala']
        for elem in listt:
            usermane.send_keys(elem)
            time.sleep(2)

        usermane.send_keys(Keys.ARROW_LEFT, 'T')
        time.sleep(2)

        usermane.send_keys(Keys.ARROW_LEFT)
        usermane.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        

