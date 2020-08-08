import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

"""
1.打开表单
2.读取表头
3.读取所有数据 （list嵌套dict的可读性强）
4.指定单元格写入数据（使用静态方法，不要用实例方法）
"""


class ExcelHandler:
    def __init__(self, filepath):
        """初始化函数"""
        self.filepath = filepath
        # 这里也可以把name放到init中，但是一次只能操作1个表单，先不用。
        # 0.35 requests模块讲解和应用(一)-模块api---28分钟前

    def open_sheet(self, name) -> Worksheet:
        """打开表单
        在函数后加-> 代表函数的返回类型 ，是一种函数注解
        作用：小技巧，解决 sheet = wb[name] 后，在pycharm中，无法sheet点操作
        """
        wb = openpyxl.load_workbook(self.filepath)
        sheet = wb[name]
        return sheet

    def get_title(self, name):
        """获取首行，返回首行的list形式"""
        sheet = self.open_sheet(name)
        title = []
        for cell in sheet[1]:
            title.append(cell.value)  # 这里的value在点的时候没有提示，见openpyxl_basic.py的说明
        return title

    def get_all(self, name):
        """获取所有数据"""
        sheet = self.open_sheet(name)
        rows = list(sheet.rows)[1:]  # 第1行是表头,对应的是list的第0行

        # 数据类型1：把数据放在list套list中。但可读性不高
        # data = []
        # for column in rows:
        #     row_data = []
        #     for cell in column:
        #         row_data.append(cell.value)
        #     data.append(row_data)
        # return data

        # # 数据类型2：把数据放在list套dict中。方便查找
        data = []
        title = self.get_title("Sheet1")
        for row in rows:
            row_data = []
            for cell in row:
                row_data.append(cell.value)
            # print(row_data)  # 每次输出excel的一行数据

            data_dict = dict(zip(title, row_data))  # zip这行数据
            data.append(data_dict)  # 把每次的dict放到data中
        return data

    def write(self):
        """
        写入excel数据
        """
        # 0.36，17分50秒


# 用来先测试封装的内容：
if __name__ == '__main__':
    excel = ExcelHandler(r"excel.xlsx")
    print(excel.get_all("Sheet1"))
