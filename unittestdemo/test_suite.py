# test_suite.py

import unittest
from unittestdemo.test_mathfunc import TestMathFunc

if __name__ == '__main__':
    '''
    unittest.TestSuite()类的addTests方法
    '''
    suite = unittest.TestSuite()
    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    # 一、把tests这个list作为入参给suite
    suite.addTests(tests)
    # 二、直接用addTest方法添加单个TestCase
    suite.addTest(TestMathFunc("test_multi"))

    '''
        unittest.TestLoader()类的多个方法：
            loadTestsFromName
            loadTestsFromNames
            loadTestsFromTestCase
    '''
    # 三、loadTestsFromName()，传入'模块名.TestCase名'
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))

    # 四、loadTestsFromNames()，类似，传入列表
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))

    # 五、loadTestsFromTestCase()，传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    # 注意，用TestLoader的方法是无法对case进行排序的，同时，suite中也可以套suite。

    with open('UnittestTextReport.txt', 'a') as f:
        # 用普通文本生成报告 ，另一种是HtmlTestRunner， verbosity为1或者2
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
        # unittest.TextTestRunner(stream=f, verbosity=2).run(suite)
