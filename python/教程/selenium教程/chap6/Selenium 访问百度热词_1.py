from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

dr =webdriver.Chrome()

dr.implicitly_wait(30)

# dr =webdriver.PhantomJS(executable_path=r'C:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# dr.get("https://baidu.com")
dr.get("https://www.csdn.net")

tmp = dr.find_element_by_link_text('首页').get_attribute('href')
print(tmp)

dr.quit()
