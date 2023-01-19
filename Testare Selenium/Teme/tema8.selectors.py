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

# test1 = webdriver.Chrome()
# test1.get('https://phptravels.net/')

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
#
# test1.quit()


#    CSS - ID

# test1 = webdriver.Chrome()
# test1.get('https://phptravels.net/')
# test1.find_element(By.CSS_SELECTOR, 'span#select2-hotels_city-container').click()
# time.sleep(2)
#
# #     CSS - class
# test1.find_element(By.CSS_SELECTOR, 'input.select2-search__field').send_keys('paris')
# time.sleep(2)
# # test1.find_element(By.CSS_SELECTOR,
# # time.sleep(2)

# #      CSS - atribut = valoare partiala
# test1.find_element(By.CSS_SELECTOR, 'span>[id*="select2-hotels"]').click()
# time.sleep(3)
#
#
#
# test1.quit()

#      XPATH - atribut/valoare


# testXpath = webdriver.Chrome()
# testXpath.get('https://phptravels.net/')

# # testXpath.find_element(By.XPATH,"//span[@class='select2-selection__arrow']").click()
# testXpath.find_element(By.XPATH, "//span[@class='selection']").click()
# testXpath.find_element(By.XPATH, "//*[@class='select2-search__field']").send_keys('tunisia')
# # testXpath.find_element(By.XPATH, '//*[@id="select2-hotels_city-container"]').click()
# time.sleep(3)

# #    XPATH - textul de pe element

# testXpath.find_element(By.XPATH,"//a[text()='Become Supplier']").click()
# time.sleep(3)
#
# testXpath.find_element(By.XPATH,"//a[text()='Optional']").click()
#
# time.sleep(3)
#
# testXpath.back()
# testXpath.back()
#
# time.sleep(3)
#
# testXpath.find_element(By.XPATH, "//span[text()=' Search by City']").click()
# time.sleep(3)
#
# testXpath.quit()


#    XPATH - partial text

# testXpath2 = webdriver.Chrome()
# testXpath2.get('https://the-internet.herokuapp.com')
# testXpath2.find_element(By.XPATH, "//a[contains(text(), 'Authentication')]").click()
#
# time.sleep(3)
#
# testXpath2.back()

#     XPATH - or (| using pipe)

# testXpath2.find_element(By.XPATH, "//a[text()='WYSIWYG Editor']").click()
# testXpath2.find_element(By.XPATH, "//button[@title='Bold'] | //button[@title='Italic']").click()
# time.sleep(2)
# testXpath2.find_element(By.XPATH, "//span[text()='File'] | //span[text()='Edit']").click()
# time.sleep(2)

#     XPATH [1]

# testXpath2.find_element(By.XPATH, "(//button[@type='button'])[3]").click()
# time.sleep(3)
#
#
# #     XPATH - parent::
#
# testXpath2.back()
# testXpath2.find_element(By.XPATH, "//a[contains(text(), 'Form Authentication')]").click()
# time.sleep(2)
#
# testXpath2.find_element(By.XPATH, "//i[@class='fa fa-2x fa-sign-in']//parent::button").click()
# time.sleep(3)
#
# testXpath2.quit()
#
# #     XPATH - sibling::
#
# test1 = webdriver.Chrome()
# test1.get('https://phptravels.net/')
# test1.find_element(By.XPATH, "//span[@class='la la-calendar form-icon'] /following-sibling::input[@id='checkin']").click()
# time.sleep(3)
#
# test1.quit()


#   XPATH - with function with param

# Deschidem pagina pe care lucram
test_page = webdriver.Chrome()
test_page.get("https://phptravels.net/signup")

def choose_element(label, input_value):
    input = test_page.find_element(By.XPATH, f'//label[text()="{label}"]//parent::div//input')
    input.clear()
    input.send_keys(input_value)

choose_element("First Name", "Ramona")
time.sleep(2)
choose_element("Last Name", "Gherasim")
time.sleep(2)
choose_element("Phone", "123")
time.sleep(2)
choose_element("Email", "ramona@yahoo.com")
time.sleep(2)

# def choose_element1(placeholder, input_value):
#     input = phptravels_page.find_element(By.XPATH, f'//input[@placeholder="{placeholder}"]')
#     input.clear()
#     input.send_keys(input_value)
#
# choose_element1("First Name", "Alexandra")
# time.sleep(2)
# choose_element1("Last Name", "Adela")
# time.sleep(2)

test_page.quit()


test_page = webdriver.Chrome()
test_page.get("https://the-internet.herokuapp.com/login")

def choose_element(id, input_value):
    input = test_page.find_element(By.XPATH, f'//input[@id="{id}"]')
    input.clear()
    input.send_keys(input_value)

choose_element("username", "Ramona")
time.sleep(2)
choose_element("password", "Gherasim")
time.sleep(2)

test_page.quit()