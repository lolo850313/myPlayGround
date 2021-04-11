from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://baidu.com")

driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id('su').click()

cookies = driver.get_cookies()

cookie = driver.get_cookie("BAIDUID")



print("baidu cookie")

print(cookie)

for i in (cookies):
    print(i)

driver.add_cookie({"name":"testname_1234567890","value":"testvalue_1234567890"})

for i in (cookies):
    print(i)
    
driver.quit()