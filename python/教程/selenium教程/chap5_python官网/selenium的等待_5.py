from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

dr =webdriver.Chrome()

dr.implicitly_wait(30)

# dr =webdriver.PhantomJS(executable_path=r'C:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# dr.get("https://baidu.com")
dr.get("https://top.baidu.com")


for index in range(10):
    tmpLi = dr.find_element_by_xpath('//*[@id="hot-list"]/li['+ str(index+1) +']/a')
    print(tmpLi.get_attribute("title"))
# dr.quit()
