from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://toutiao.com")

driver.save_screenshot("save_1.png")

ac = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/ul/li[5]/a')
ActionChains(driver).move_to_element(ac).perform()

time.sleep(2)
driver.save_screenshot("save_2.png")