from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# test1 = webdriver.Chrome()
# test1.get('https://phptravels.net/')

# #       ID
#
# test1.find_element(By.ID, 'ACCOUNT').click()
# time.sleep(3)
#
# test1.find_element(By.ID, 'checkin').click()
# time.sleep(3)
#
# test1.find_element(By.ID, 'checkout').click()
# time.sleep(3)
#
# test1.find_element(By.ID, 'select2-hotels_city-container').click()
# time.sleep(3)
#
# #      Class name
#
# test1.find_element(By.CLASS_NAME, 'select2-search__field').send_keys('paris,france')
# time.sleep(3)
#
# test1.find_element(By.CLASS_NAME, 'guest_hotels').click()
# time.sleep(2)
#
# test1.find_element(By.CLASS_NAME, 'roomInc').click()
# time.sleep(2)

# #     Link text
# test1.find_element(By.LINK_TEXT, 'Hotels').click()
# time.sleep(2)
# test1.back()

# test1.find_element(By.LINK_TEXT, 'Transfers').click()
# time.sleep(2)
# test1.back()
# time.sleep(2)

# test1.find_element(By.LINK_TEXT, 'Offers').click()
# time.sleep(3)

# test1.quit()


#       Partial link text

# test2 = webdriver.Chrome()
# test2.get('http://automationpractice.com/index.php')
# test2.find_element(By.PARTIAL_LINK_TEXT, 'Contact your').click()
# time.sleep(3)
#
# test2.quit()
#
# test3 = webdriver.Chrome()
# test3.get('https://the-internet.herokuapp.com/')
# test3.find_element(By.PARTIAL_LINK_TEXT, 'Elements').click()
# time.sleep(3)
# test3.back()
#
# test3.find_element(By.PARTIAL_LINK_TEXT, 'A/B Testing').click()
# time.sleep(2)
#
# test3.quit()


#          Name
#
# test4 = webdriver.Chrome()
# test4.get('https://www.techlistic.com/p/selenium-practice-form.html')
# test4.find_element(By.ID, 'ez-accept-all').click()
# test4.find_element(By.NAME, 'firstname').send_keys('Ramona')
# time.sleep(5)
# test4.find_element(By.NAME, 'lastname').send_keys('Lupu')
# time.sleep(5)
# test4.find_element(By.ID, 'sex-1').click()
# time.sleep(3)
#
# test4.quit()


#         Tag

test1 = webdriver.Chrome()
test1.get('https://phptravels.net/')

# test1.find_element(By.ID, 'ACCOUNT').click()
# time.sleep(1)
# test1.find_element(By.LINK_TEXT, 'Customer Login').click()
# time.sleep(2)
# lista_inputuri = test1.find_elements(By.TAG_NAME, "input")
# lista_inputuri[0].send_keys("raduramona86@yahoo.com")
# lista_inputuri[1].send_keys("ramona")
# time.sleep(1)
# test1.back()
# time.sleep(2)

test1.quit()

