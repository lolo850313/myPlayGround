from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://baidu.com")

driver.find_element_by_name("wd").send_keys("selenium")

time.sleep(2)

driver.find_element_by_id("su").click()
time.sleep(2)

driver.quit()