"""
suite = unittest.TestSuite()类的对象调用addTests()方法
    addTests(入参)，入参可为list，类("方法")
suite2 = unittest.TestLoader()类的多个方法：
    loadTestsFromName
    loadTestsFromNames
    loadTestsFromTestCase
    loadTestsFromModule
suite.addTests(suite2)  可以传入TestLoader类的对象的loadTestsFromXXXX
"""

import unittest

from unittestdemo import Test_Init
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
            loadTestsFromModule
    '''
    # 三、loadTestsFromName()，传入'模块名.TestCase名'
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))

    # 四、loadTestsFromNames()，类似，传入列表
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))

    # 五、loadTestsFromTestCase()，传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    # 注意，用TestLoader的方法是无法对case进行排序的，同时，suite中也可以套suite。

    # 六、loadTestsFromModule
    suite2 = unittest.TestLoader().loadTestsFromModule(Test_Init)
    suite.addTests(suite2)
    print(suite)
    with open('UnittestTextReport.txt', 'w') as f:
        # 用普通文本生成报告 ，另一种是HtmlTestRunner， verbosity为0 1 2
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
        # unittest.TextTestRunner(stream=f, verbosity=2).run(suite)
