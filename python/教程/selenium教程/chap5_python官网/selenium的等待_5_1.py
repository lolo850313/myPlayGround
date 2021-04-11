from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

dr =webdriver.Chrome()

dr.implicitly_wait(10)

# dr =webdriver.PhantomJS(executable_path=r'C:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# dr.get("https://baidu.com")
dr.get("https://www.csdn.net")

try:
    # WebDriverWait(driver=self.dr,timeout=20,poll_frequency=0.5,ignored_exceptions=None)
    # 打开的浏览器，超时时间，检查频率
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_all_elements_located(By.LINK_TEXT, u'首页'))
finally:
    print(dr.find_element_by_link_text('首页').get_attribute('href'))

tmp = dr.find_element_by_link_text('首页').get_attribute('href')
print(tmp)

dr.quit()
