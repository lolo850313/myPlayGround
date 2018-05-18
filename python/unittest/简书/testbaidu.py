from selenium import webdriver
import unittest, time

class baiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").submit()
        time.sleep(5)
        title = driver.title
        self.assertEqual(title,u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ =="__main__":
    unittest.main()