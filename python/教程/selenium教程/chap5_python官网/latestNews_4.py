from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

dr =webdriver.Chrome()

# dr =webdriver.PhantomJS(executable_path=r'C:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# dr.get("https://baidu.com")
dr.get("https://www.python.org")

time.sleep(2)
JS1 = "document.title='XXXX'"
dr.execute_script(JS1)

time.sleep(2)
dr.find_element_by_id('id-search-field').send_keys('pycon')
dr.find_element_by_id('submit').click()

dr.find_elements_by_css_selector(r'#content > div > section > form > ul > li:nth-child(1) > h3 > a').click()
dr.save_screenshot("latestNews_save.png")

dr.quit()
