from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://baidu.com")
driver.maximize_window()

time.sleep(2)

JS1 = 'window.open("https://sougou.com")'
driver.execute_script(JS1)

time.sleep(2)

JS2 = 'window.open("https://fanyi.youdao.com")'
driver.execute_script(JS2)

driver.quit()