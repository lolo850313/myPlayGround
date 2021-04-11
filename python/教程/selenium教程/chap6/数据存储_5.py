import csv 
import time 
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys

def write(item):
    with open("D://jrtt.csv", "a") as f:
        writer = csv.write(f)
        try:
            writer.writerow(f)
        except:
            print('error') 


def getInfo():
    title = dr.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/h1')
    sauce = dr.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div[1]/span[1]')
    titleTime = dr.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div[1]/span[2]')
    info = [title.text, sauce.text, titleTime.text]
    print(info)
    return info



# dr =webdriver.PhantomJS(executable_path=r'C:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# dr.get("https://baidu.com")
url = "https://www.toutiao.com/search/?keyword=selenium"
dr =webdriver.Chrome()

dr.implicitly_wait(2)
dr.get(url)

time.sleep(2)


for i in range(50):
    ActionChains(dr).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
    print(f'下拉{i}次')

time.sleep(1)
url_=dr.find_elements_by_css_selector('.title')
# print(url_)

url_list = []
for i in url_:
    url_list.append(i.get_attribute('href'))

# print(url_list)
for i in url_list[:10]:
    try:
        dr.get(i)
        time.sleep(2)
        write(getInfo())
        print(111)

        dr.get(url)
        print("finish")
    except:
        print('error')