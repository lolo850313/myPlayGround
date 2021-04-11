from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time


dr =webdriver.Chrome()

# dr =webdriver.PhantomJS(executable_path=r'C:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe')
dr.get("https://baidu.com")

time.sleep(2)
JS1 = "document.title = 'xxx'"
dr.execute_script(JS1)

time.sleep(1)
# document.getElementById
JS2 = r"alert(document.title)"
dr.execute_script(JS2)
time.sleep(3)

dr.quit()
