# pip install webdriver-manager
# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://ru.shein.com/')


# 1-------------------  ПОЗИТИВ

def check_1():
    checkbox = driver.find_element(by=By.NAME, value='header-search')
    checkbox.send_keys('Iphone 13 Pro Max')
    checkbox.send_keys(Keys.ENTER)


# 2----------------------  НЕГАТИВ


def check_2():
    checkbox = driver.find_element(by=By.NAME, value='header-search')
    checkbox.send_keys('Напольное зеркало')
    checkbox.send_keys(Keys.ENTER)


# 3----------------------- ПОЗИТИВ


def check_3():
    checkbox = driver.find_element(by=By.NAME, value='header-search')
    checkbox.send_keys('2773543')
    checkbox.send_keys(Keys.ENTER)
    button = driver.find_element(by=By.CLASS_NAME, value='S-product-item__name')
    button.click()
    button = driver.find_element(by=By.CLASS_NAME, value='product-intro__size-radio-inner')
    button.click()




    button = driver.find_element(by=By.CLASS_NAME, value='product-intro__add-btn')
    button.click()


# 4----------------------- НЕГАТИВ

def check_4():
    checkbox = driver.find_element(by=By.NAME, value='header-search')
    checkbox.send_keys('2160692')
    checkbox.send_keys(Keys.ENTER)

# 5-------------------  Негатив

def check_5():
    checkbox = driver.find_element(by=By.NAME, value='header-search')
    checkbox.send_keys('24142141242142141')
    checkbox.send_keys(Keys.ENTER)

# 6-------------------  ПОЗИТИВ

def check_6():
    checkbox = driver.find_element(by=By.NAME, value='header-search')
    checkbox.send_keys('Чехол')
    checkbox.send_keys(Keys.ENTER)




check_3()