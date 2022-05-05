import urllib.request
from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys
import pickle
from random import *

def pictures(serch):
    text = [] 
    url = "https://yandex.ru/images/search?from=tabbar&text=" + serch

    options = webdriver.ChromeOptions()
    chromedriver = r"C:\Users\pniki\Documents\Пограммы\парсинг\парсингselenium\chromedriver.exe"
    driver = webdriver.Chrome(executable_path = chromedriver, options = options)


    try: 
        driver.get(url = url)
        driver.implicitly_wait(10)
        items = driver.find_elements(by = 'xpath', value = '//img[@class="serp-item__thumb justifier__thumb"]')

        i = 0
        for items[i] in items:
            urllib.request.urlretrieve(items[i].get_attribute("src"), 'imges\\pict' + str(i) + ".jpg")
            print(items[i].get_attribute("src"))
            i+= 1

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()
