import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print("Test.setUp")

    def testOne(self):
        print("Test.testOne")

    def tearDown(self):
        print("Test.tearDown")

class Test1(unittest.TestCase):

    def setUp(self):
        print("\nTest1.setUp" )

    def testOne(self):
        print("Test1.testOne")

    def tearDown(self):
        print("Test1.tearDown")

if __name__ == "__main__":
    suite = unittest.TestSuite()
#为什么Test 和Test1的参数是str，且会影响结果，参数是怎么影响结果的？
    suite.addTest(Test('tearDown'))
    suite.addTest(Test1('testOne'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
    