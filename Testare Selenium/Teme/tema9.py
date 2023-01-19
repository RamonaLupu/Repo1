import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import unittest

class Login(unittest.TestCase):
    form_authentication = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    h2 = (By.XPATH, '//h2')
    login_button = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
    link = (By.XPATH, "//a[text()='Elemental Selenium']")

    def setUp(self):
        self.tema = webdriver.Chrome()
        self.tema.maximize_window()
        self.tema.get('https://the-internet.herokuapp.com/')
        self.tema.find_element(*self.form_authentication).click()
    def tearDown(self):
        self.tema.quit()

    def test1_verifica_url(self):
        time.sleep(2)
        actual = self.tema.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        assert actual == expected, f"Error: URL incorect "


    def test2_page_title(self):
        title_page = self.tema.title
        expected_title = 'The Internet'
        self.assertEqual(title_page,expected_title, 'Title incorect')

    def test3_h2(self):
        elem_h2 = self.tema.find_element(*self.h2)
        actual_h2 = elem_h2.text
        expected_h2 = 'Login Page'
        assert actual_h2 == expected_h2, f"Error: h2 incorect "
    def test4_login_button(self):
        actual_login_button= self.tema.find_element(*self.login_button).is_displayed()
        assert actual_login_button, 'Login button is not displayed'
    def test5_href_link(self):
        actual_link = self.tema.find_element(*self.link).get_attribute('href')
        expected_link = 'http://elementalselenium.com/'
        assert actual_link == expected_link, f'href link incorect'



