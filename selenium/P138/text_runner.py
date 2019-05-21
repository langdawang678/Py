#coding=utf-8
from widget import Widget
import unittest
# 执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))

# 测试
if __name__ == "__main__":
     # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
    TestRunner 类作为测试用例的基本执行环境，来驱动整个单元测试过程。
    Python 开发人员在进行单元测试时一般不直接使用 TestRunner 类，
    而是使用其子类 TextTestRunner 来完成测试，并将测试结果以文本方式显示出来：
    '''


