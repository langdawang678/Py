from widget import Widget

import unittest

# 执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    # 测试 getSize()方法的测试用例
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

    # 测试 resize()方法的测试用例
    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))

    def tearDown(self):
        self.widget = None
'''
lib文件夹下unitTest包（框架）下有case.py模块里有class TestCase类。
让所有执行测试的类都继承于 TestCase 类，可以将 TestCase 看成是对特定类进行测试的方法的
集合
setUp 和tearDown都是TestCase中定义的方法
assertEqual()也是 TestCase 类中定义的方法。
'''

# 构造测试集
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testReSize"))
    return suite
'''
TestSuite 类可以看成是 TestCase 类的一个容器，用来对多个测试用例进行组织，这样多个测试用例可
以自动在一次测试中全部完成,提供名为 suite()的全局方法，PyUnit 在执行测试的过程调用 suite()方法来确定有多少个测试用
例需要被执行
可以在单元测试代码中定义一个名为 suite()的全局函数，并将其作为整个单元测试的入口
'''

# 测试
if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')