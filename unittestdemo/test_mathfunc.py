# test_mathfunc.py
import unittest
from unittestdemo.mathfunc import *


class TestMathFunc(unittest.TestCase):
    '''#һ��class�̳���unittestdemo.TestCase������һ����������
    #�����ж���� test ��ͷ�ķ�����ÿ����load��ʱ��������һ��TestCaseʵ��
    #���Խ� TestCase �����Ƕ��ض�����в��Եķ����ļ���'''

    @classmethod
    def setUpClass(cls):
        print("This setUpClass() 测试类前执行1次.")

    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() 测试类后执行1次.")

    def setUp(self) -> None:
        print("每个测试方法前")

    def tearDown(self):
        print("每个测试方法后")

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
'''unittestdemo.main��)���޲���Ĭ��ʱverbosity=1,
����0����ʾÿ��������ִ�н��'''
