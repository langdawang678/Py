class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b

print("被导入的计算器模块，测试被导入模块的顶格读取")
# 即该模块被其他模块导入时，这个print语句会被读取（没有缩进的都会被读取）
print(__name__)  # __main__
print(__file__)  # D:/PycharmProjects/Py/pythoncode/calc.py

