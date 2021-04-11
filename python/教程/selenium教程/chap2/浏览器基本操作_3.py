from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://baidu.com")

time.sleep(2)
driver.get("https://news.baidu.com")

time.sleep(2)
driver.back()

time.sleep(2)
driver.forward()

time.sleep(2)
driver.refresh()

time.sleep(2)
driver.quit()

