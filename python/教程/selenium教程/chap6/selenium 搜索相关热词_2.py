from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

dr =webdriver.Chrome()

dr.implicitly_wait(30)

# dr =webdriver.PhantomJS(executable_path=r'C:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# dr.get("https://baidu.com")
dr.get("https://top.baidu.com")

hw_arr = []
for i in range(10):
    xpath = '//*[@id="hot-list"]/li[' +  str(i+1) + ']/a[1]'
    value = dr.find_element_by_xpath(xpath).get_attribute('title')
    hw_arr.append(value)

keyword = (hw_arr[0])

URL ='https://www.toutiao.com/search/?keyword=%s'%keyword
dr.get(URL)
# dr.quit()
