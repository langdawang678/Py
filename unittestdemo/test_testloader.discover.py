"""
演示unittest.TestLoader().discover()方法

测试用例执行步骤
1、初始化加载器，testloader=unittest.TestLoader()
2、查找测试用例，suite=testloader.discover(文件夹，默认test开头) # 也可'test*.py'
还有其他加载的方式：

3、打开一个文件，用于存放text报告
4、初始化运行器，runner = unittest.TextTestRunner（文件）
5、运行运行器， runner.run(suite)
"""
import unittest

testLoader = unittest.TestLoader()
suite = testLoader.discover(".", "test_math*.py")
print(suite)

if __name__ == '__main__':
    with open("TextTestRunner_test_math*.py.txt", "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        runner.run(suite)

