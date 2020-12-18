# file_name: test_abc.py
import pytest

class Test_Mark:
    def test_a(self):  # test开头的测试函数
        print("test_a，smoke")
        assert 1  # 断言成功

    @pytest.mark.me
    def test_b(self):
        print("------->test_b")
        assert 1  # 断言失败

    def test_c(self):
        print("test_c")
        assert 1  # 断言失败

    def test_d(self):
        print("test_d")
        assert 1  # 断言失败


