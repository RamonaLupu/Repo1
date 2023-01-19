# Metoda de set-up

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import unittest
from unittest import TestCase


class Alerts(unittest.TestCase):
    ALERT_BUTTON = (By.XPATH, '//*[text()="Click for JS Alert"]')
    CONFIRM_BUTTON = (By.XPATH, '//*[text()="Click for JS Confirm"]')
    PROMPT_BUTTON = (By.XPATH, '//*[text()="Click for JS Prompt"]')
    ALERT_MSG = (By.ID, "result")
# Definirea metodei de setUp
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.maximize_window()
        time.sleep(3)
        self.chrome.implicitly_wait(2)
# Definirea metodei de tearDown
    def tearDown(self) -> None:
        self.chrome.quit()
    def test_alert_accept(self):
        self.chrome.find_element(*self.ALERT_BUTTON).click()
        js_alert = self.chrome.switch_to.alert
        js_alert.accept()  # built-in method care accepta alerta e.g. da click pe buton
        time.sleep(3)
        actual_alert_msg = self.chrome.find_element(*self.ALERT_MSG).text
        expected_alert_msg = "You successfully clicked an alert"
        assert actual_alert_msg == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "

    def test_confirm_acept(self):
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        js_confirm = self.chrome.switch_to.alert
        js_confirm.accept()
        actual_confirm_msg = self.chrome.find_element(*self.ALERT_MSG).text
        expected_confirm_msg = "You clicked: Ok"
        assert actual_confirm_msg == expected_confirm_msg, f"Error: {expected_confirm_msg}, actual {actual_confirm_msg} "

    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        js_confirm = self.chrome.switch_to.alert
        js_confirm.dismiss()
        actual_confirm_msg = self.chrome.find_element(*self.ALERT_MSG).text
        expected_confirm_msg = "You clicked: Cancel"
        assert actual_confirm_msg == expected_confirm_msg, f"Error: {expected_confirm_msg}, actual {actual_confirm_msg} "

    @unittest.skip    #posibilitatea de a da skip la un test

    def test_prompt_no_text_accept(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()
        js_confirm = self.chrome.switch_to.alert
        js_confirm.accept()
        actual_prompt_msg = self.chrome.find_element(*self.ALERT_MSG).text
        expected_prompt_msg = "You entered:"
        assert actual_prompt_msg == expected_prompt_msg, f"Error: {expected_prompt_msg}, actual {actual_prompt_msg} "

    @unittest.skip
    def test_prompt_no_text_dismiss(self):
            self.chrome.find_element(*self.PROMPT_BUTTON).click()
            js_confirm = self.chrome.switch_to.alert
            js_confirm.dismiss()
            actual_prompt_msg = self.chrome.find_element(*self.ALERT_MSG).text
            expected_prompt_msg = "You entered: null"
            assert actual_prompt_msg == expected_prompt_msg, f"Error: {expected_prompt_msg}, actual {actual_prompt_msg} "


    def test_prompt_text_accept(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()
        js_confirm = self.chrome.switch_to.alert
        js_confirm.send_keys('Hello!')
        js_confirm.accept()
        actual_prompt_msg = self.chrome.find_element(*self.ALERT_MSG).text
        expected_prompt_msg = "You entered: Hello!"
        assert actual_prompt_msg == expected_prompt_msg, f"Error: {expected_prompt_msg}, actual {actual_prompt_msg} "

    def test_prompt_text_dismiss(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()
        js_confirm = self.chrome.switch_to.alert
        js_confirm.send_keys('Hello!')
        js_confirm.dismiss()
        actual_prompt_msg = self.chrome.find_element(*self.ALERT_MSG).text
        expected_prompt_msg = "You entered: null"
        assert actual_prompt_msg == expected_prompt_msg, f"Error: {expected_prompt_msg}, actual {actual_prompt_msg} "
