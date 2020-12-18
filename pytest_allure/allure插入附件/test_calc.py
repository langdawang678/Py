import allure
import pytest
import sys
sys.path.append("../..")  # 加入上一级的目录，否则命令行运行会找不到上级module

from pytest_allure.calc import Calculator


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
        allure.attach("添加str：添加类型为TEXT",
                      name="name是TEXT",
                      attachment_type=allure.attachment_type.TEXT
                      )
        allure.attach('<img src="https://ceshiren.com/uploads/default/original/2X/3/3013870f5b1eedf2c58ab743c99695ab9d1b660a.jpeg" width="100%">',
                      name="name是HTML",
                      attachment_type=allure.attachment_type.HTML
                      )
        assert c == calc.add(a, b)

    def test_div(self):
        calc = Calculator()
        print("00000000000000")
        allure.attach.file("./allure.png",
                           name="allure.attach.file图片",
                           attachment_type=allure.attachment_type.PNG)
        # allure.attach.file("",
        #                    name="视频,
        #                    attachment_type=allure.attachment_type.MP4)

        assert 1 == calc.div(4, 2)
