from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys
import pickle

def wikipedia(serch):
    text = []
    url = "https://ru.wikipedia.org/wiki/" + serch
    options = webdriver.ChromeOptions() 
    chromedriver = r"Ваш путь до драйвера"
    driver = webdriver.Chrome(executable_path = chromedriver, options = options)

    try:
        driver.get(url = url)
        driver.implicitly_wait(10)

        items = driver.find_elements(by='xpath',value = '//div[@class="mw-parser-output"]')

        i = 0

        #for i in range(len(items)):

        for i in range(len(items)):

            text.append(items[i].text)
            text.append('\n\n\n\n\n\n')

            i+=1
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    return text

print(wikipedia('Пушкин'))