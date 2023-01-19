import unittest
import time
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Context_menu(unittest.TestCase):
    BOX = (By.ID, 'hot-spot')
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/context_menu")
        self.chrome.maximize_window()
        time.sleep(3)
        self.chrome.implicitly_wait(2)

    # Definirea metodei de tearDown
    def tearDown(self) -> None:
        self.chrome.quit()

    def test_contextmenu(self):
        action = ActionChains(self.chrome)
        elem = self.chrome.find_element(*self.BOX)
        action.context_click(elem).perform() # click dreapta
        time.sleep(2)
        alert = self.chrome.switch_to.alert
        text = alert.text
        assert text == 'You selected a context menu'
        alert.accept()
        time.sleep(3)



