#test_suite.py

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)
    
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)
'''
上面用了TestSuite的 addTests() 方法，并直接传入了TestCase列表，我们还可以：

# 直接用addTest方法添加单个TestCase
suite.addTest(TestMathFunc("test_multi"))

# 用addTests + TestLoader
# loadTestsFromName()，传入'模块名.TestCase名'
suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))

# loadTestsFromNames()，类似，传入列表
suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))


# loadTestsFromTestCase()，传入TestCase
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

注意，用TestLoader的方法是无法对case进行排序的，同时，suite中也可以套suite。
'''

