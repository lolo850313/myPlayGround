from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://baidu.com")

time.sleep(2)
JS = "window.scrollTo(10000,document.body.scrollHeight)"
driver.execute_script(JS)