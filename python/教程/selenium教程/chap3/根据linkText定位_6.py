from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://baidu.com")
time.sleep(2)

driver.find_element_by_link_text("新闻").click()
driver.back()
time.sleep(2)

driver.find_element_by_link_text("地图").click()
driver.back()
time.sleep(2)

driver.find_element_by_link_text("视频").click()
driver.back()
time.sleep(2)

driver.quit()