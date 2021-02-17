import pytest
from selenium import webdriver


# 定义fixture
@pytest.fixture()  # pytest能识别出是一个前置后置
def init():
    # 前置
    print("我是函数级别的前置，start....")
    # driver = webdriver.Chrome()
    # driver.get(url="https://www.baidu.com/")
    yield  # 分割前后置
    print("我是函数别的前置，start....")
    # driver.quit()  # 后置


# 定义fixture
@pytest.fixture(scope="class")
def mycc():
    print("我是类级别的前置，start....")
    yield
    print("我是类级别的后置，end...")


# 测试用例
def test_1():
    print("*******1111")


@pytest.mark.usefixtures("init")  # 测试用例中调用 之前定义的fixture
def test_2():
    print("*******2222")

@pytest.mark.usefixtures("init")
@pytest.mark.usefixtures("mycc")
class TestA:
    def test_aaa(self):
        print("*******test_aaa")

    def test_bbb(self):
        print("*******test_bbb")
