from selenium import webdriver
wd = webdriver.Chrome(r'C:\chromedriver.exe')

wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
a = wd.find_elements_by_class_name('animal')

for i in a:
    print(i.text)
# search_input.send_keys("hewenhao")
