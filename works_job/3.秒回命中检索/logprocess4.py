import os,openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
total = []  # 统计秒回命中数


def isEffective(toBeCheckedFile):
    # print(toBeCheckedFile)
    with open(toBeCheckedFile, encoding='gb18030', errors='ignore') as file:
        list1 = file.readlines()

    for i in list1:
        if "Effective AsrRoute is local asr, NativeIotAdapter control successfully" in i:
            # print("      命中")  # 每条语料的syslog中，这条记录只有一次
            total.append(1)


# 遍历log文件夹
def getFileList(path):
    for parent, dirNames, fileNames in os.walk(path):
        filesList = []
        for filename in fileNames:
            filesList.append(path + filename)
        return filesList



# 遍历log文件并检查是否命中
filesList = getFileList('./log/')
for checkFile in filesList:
    isEffective(checkFile)
print("秒回命中数:", len(total))
print("执行总数：", len(filesList))
