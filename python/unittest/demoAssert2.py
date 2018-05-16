import unittest
import math
import re

class demoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4+5,9)
    
    def test2(self):
        self.assertNotEqual(5*2,10)

    def test3(self):
        self.assertTrue(4+5==9,"The result is False")
        
    def test4(self):
        self.assertTrue(4+5==10,"assertion fails")

    def test5(self):
        self.assertIn(3,[1,2,3])

    def test6(self):
        self.assertNotIn(3,range(5))

if __name__ == "__main__":
#unittest.main()开始了整个单元测试，这里实际上是调用了main.py中的
#TestProgram类的构造函数，因为在该文件中有这样一条语句：main = TestProgram。
    unittest.main()


