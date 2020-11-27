from testbaidu import baiduTest
from test_youdao import YoudaoTest

import unittest

suite = unittest.TestSuite()
suite.addTest(baiduTest.test_baidu("test_baidu"))
suite.addTest(YoudaoTest.test_youdao("test_youdao"))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)