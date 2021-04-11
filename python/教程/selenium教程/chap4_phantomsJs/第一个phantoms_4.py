from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

driver =webdriver.PhantomJS(executable_path=r'C:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get("https://cn.bing.com")

title = driver.title
print(title)

keywords = "selenium 自动化测试"
driver.find_element_by_id("sb_form_q").send_keys(keywords)
driver.save_screenshot('bing_1.png')

driver.find_element_by_id('sb_form_q').click()
driver.save_screenshot('bing_2.png')


driver.find_element_by_xpath('//*[@id="b_results"]/li[3]/div[1]/h2/a').click()
driver.save_screenshot('bing_3.png')

driver.quit()
