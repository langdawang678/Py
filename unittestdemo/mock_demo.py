from unittest import mock
import unittest
'''
Mock是Python中一个用于支持单元测试的库，它的主要功能是使用mock对象替代掉指定的Python对象，以达到模拟对象的行为。
Python 2.7，mock还未加入标准库。需要单独 pip install mock，是个单独的模块
Python 3.4，mock已经加入了标准库。
'''
# 被测试的接口/方法，这里直接写在同一个类里
class Count():
    def add(self, a, b):
        return a+b
# 测试类TestCount，去mock上面的方法（接口）
class TestCount(unittest.TestCase):
    def test_add(self):
        count = Count()
        # 把调用的方法直接mock掉：
        count.add = mock.Mock(return_value=10)

        result = count.add(1,2)
        print("调用被mock的【Count类的实例count中的count()方法】后的值是：",result)
        self.assertEqual(result,10)
if __name__ == '__main__':
    unittest.main()