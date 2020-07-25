import pytest

from pythoncode.calc import Calculator


class TestCalc:
    def setup_class(self):
        print("在整个测试类前执行setup_class")
        self.calc = Calculator()

    def teardown_class(self):
        print("在整个测试类后，执行setup_class")

    def setup(self):
        print("在单个测试方法前执行setup_class")
        self.calc = Calculator()

    def teardown(self):
        print("在单个测试类后，执行setup_class")
    @pytest.mark.parametrize("a,b,c", [
        (1, 1, 2),
        (1, 13, 14),
        (1, 1, 1),
        (1, 1, 3),
    ])
    def test_add(self, a, b, c):
        calc = Calculator()
        assert c == calc.add(a, b)

    def test_div(self):
        calc = Calculator()
        print("00000000000000")
        assert 1 == calc.div(4, 2)
