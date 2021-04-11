from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://baidu.com")

driver.find_element_by_class_name("s_ipt").send_keys("selenium")
time.sleep(2)

driver.quit()