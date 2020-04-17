#test_mathfunc.py
import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):
    '''#一个class继承了unittest.TestCase，便是一个测试用例
    #其中有多个以 test 开头的方法，每个在load的时候便会生成一个TestCase实例
    #可以将 TestCase 看成是对特定类进行测试的方法的集合'''
    @classmethod
    def setUpClass(cls):
        print ("This setUpClass() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print ("This tearDownClass() method only called once too.")
        
    def setUp(self):
        print("do something before test.Prepare environment.")
        
    def tearDown(self):
        print ("do something after test.Clean up.")
        '''setUp()和 tearDown()都是 TestCase 类中定义的方法'''
        
    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))


    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))
        
    @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(3, divide(5, 2))
        print(divide(5, 2))

if __name__ == '__main__':
    unittest.main(verbosity=0)
'''unittest.main（)，无参数默认时verbosity=1,
等于0则不显示每个用例的执行结果'''
