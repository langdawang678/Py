# coding=utf-8
# !user/bin/env python3
# -*- coding: gbk -*-
import os
import sys
import time
import xlrd
import xlwt

'''
使用说明：
一、环境配置：
1. 安装python3 ： https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe
2. 配置环境变量
3. pip3 install xlrd和pip3 install xlwt

二、操作步骤
1. 下载玲珑塔excel报告，当前脚本的同一路径下，把【旧的excel报告】重命名为old.xlsx，【新的excel报告】改为new.xlsx
2. 用python3运行，1分钟左右输出：对比结果.xls （包含 1.语料对比结果 2.rerun的语料(这次fail,上次pass)）
'''

# tips = '''
# "0": "多轮",
# "1": "单轮",
#
# "2": "飞燕设备",
# "3": "单条(非品类接入)",
# "4": "品类接入",
# "5": "单句多意图"
# '''
# print(tips)

# 根据case分类创建执行目录
# inputNum = str(input("输入数字选择对应语料目录...："))
# cwd = os.getcwd()
# # print("当前目录为: %s" % s)
# dict1 = {"0": "P0多轮",
#          "1": "P0单轮",
#          "2": "P0飞燕",
#          "3": "P0单条(非品类接入)",
#          "4": "P0品类接入",
#          "5": "P0单句多意图"}
# directory = dict1.get(inputNum)
# newDir = directory + "/" + "new.xlsx"
# oldDir = directory + "/" + "old.xlsx"
# resultDir = directory + "/" + "对比结果.xls"
# newFailDir = directory + "/" + "new_fail_corpus.txt"
# print(newDir, "\n", oldDir, "\n", resultDir)

# 获取当前目录文件，检查是否存在冲突或者文件不存在
listdir = os.listdir(os.getcwd())
if "对比结果.xls" in  listdir or ("new.xlsx" and "old.xlsx") not in listdir:
    print('''当前目录的excel文件名 设置错误或者文件冲突:
    1.请先remove or rename 上一次的《对比结果.xls》,
    2.请确保正确的命名了new.xlsx和old.xlsx
    3.rerun this script
''')
# 也可用os.path.exist(filepath or filename)判断文件或目录是否存在
    sys.exit(0)


print("\n", "开始时间 :", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 打开被写的excel，建立新表
workbook_new = xlwt.Workbook()
sheet_new = workbook_new.add_sheet('1.语料对比结果') # 表0，存放对比结果
sheet_new_1 = workbook_new.add_sheet('2.rerun的语料(这次fail,上次pass)') # 表1，存放new_fail的语料和语境

# 在新文件写入第一行的固定值,并保存
sheet_new.write(0, 0, "哪一次跑的")
sheet_new.write(0, 1, "两次对比结果")
sheet_new.write(0, 2, "语料")
sheet_new.write(0, 3, "领域判断")
sheet_new.write(0, 4, "意图判断")
sheet_new.write(0, 5, "参数判断")
sheet_new.write(0, 6, "答复判断")
sheet_new.write(0, 7, "实际领域")
sheet_new.write(0, 8, "实际意图")
sheet_new.write(0, 9, "实际参数")
sheet_new.write(0, 10, "实际答复")
sheet_new.write(0, 11, "traceID")
workbook_new.save('对比结果.xls')

# 读new和old的excel文件和表
try:
    workbook1 = xlrd.open_workbook("./new.xlsx")
    workbook2 = xlrd.open_workbook("./old.xlsx")
except FileNotFoundError as fnf_error:
    print("文件不存在：new.xlsx或者old.xlsx不在当前目录")

f1 = workbook1.sheets()[0]  # f1=new=这次运行的
f2 = workbook2.sheets()[0]  # f2=old=上次运行的

print(" new.xlsx的语料数：", f1.nrows - 1)
print(" old.xlsx的语料数：", f2.nrows - 1)

# 比较两个文件的行列数
if f1.ncols != f2.ncols:
    print('''当前: 两个文件的列数不一致，语料的excel文件格式改变了，当前运行失败
    本次: 如需对比，请修改新的excel文件的格式，使新的文件和旧的保持一致")
    下次: 运行时，可根据140-160的注释，修改对应数据的数字即可''')
if f1.nrows != f2.nrows:
    print('''两次的用例数量不一致，请检查两次增改的用例''')
    
print("执行中，当前数量较多，请耐心等待1分钟左右..........")

# 定义写入函数
def writeToExcel(hangshu, compare_result, corpus1, corpus2, f111, f112, f113, f114, f115, f116, f117, f118, f119, f211,
                 f212, f213, f214, f215, f216, f217, f218, f219):
    # 写入语料1的数据
    sheet_new.write(hangshu, 0, "这次(new)")
    sheet_new.write(hangshu, 1, compare_result)
    sheet_new.write(hangshu, 2, corpus1)
    sheet_new.write(hangshu, 3, f115)
    sheet_new.write(hangshu, 4, f116)
    sheet_new.write(hangshu, 5, f117)
    sheet_new.write(hangshu, 6, f118)
    sheet_new.write(hangshu, 7, f111)
    sheet_new.write(hangshu, 8, f112)
    sheet_new.write(hangshu, 9, f113)
    sheet_new.write(hangshu, 10, f114)
    sheet_new.write(hangshu, 11, f119)
    # 写入语料2的数据并保存
    sheet_new.write(hangshu + 1, 0, "上次(old)")
    sheet_new.write(hangshu + 1, 1, compare_result)
    sheet_new.write(hangshu + 1, 2, corpus2)
    sheet_new.write(hangshu + 1, 3, f215)
    sheet_new.write(hangshu + 1, 4, f216)
    sheet_new.write(hangshu + 1, 5, f217)
    sheet_new.write(hangshu + 1, 6, f218)
    sheet_new.write(hangshu + 1, 7, f211)
    sheet_new.write(hangshu + 1, 8, f212)
    sheet_new.write(hangshu + 1, 9, f213)
    sheet_new.write(hangshu + 1, 10, f214)
    sheet_new.write(hangshu + 1, 11, f219)
    workbook_new.save('对比结果.xls')


# 拎出new_fail的语料和语境，放于表2
new_fail_corpus = []  # 记录“本次fail上次pass”的语料
new_fail_corpus_context = []  # 记录“本次fail上次pass”的语料的语境，rerun时根据语料输入不同的语境
# new_add_corpus = []  # 记录“新增添加”的语料，因为无法对比上次，需要单独拎出

# 遍历sheet1的行
i = 1  # i代表excel的行数，从第1行开始，因为第0行是表头
writerow = 1
while i < f1.nrows:
    f1_row_X = f1.row_values(i)  # 文件1的第i行
    f1_corpus = f1_row_X[4]  # 每i行的第4个为语料
    # 判定该行的四项值
    f1_corpus_result = 1
    if f1_row_X[15] == "false" or f1_row_X[16] == "false" or f1_row_X[17] == "false" or f1_row_X[
        18] == "false":
        f1_corpus_result = 0
    j = 1  # 代表第i行时的每个j列
    while j < f2.nrows:
        f2_row_X = f2.row_values(j)  # 文件2的第i行
        f2_corpus = f2_row_X[4]  # 每i行的第4个为语料
        if f1_corpus == f2_corpus:  # print("在f2第", j, "行", "找到了和f1相同的语料:", f2_corpus)
            # 定义15-18的四项和22的traceID
            f1_row_X11 = f1_row_X[11]  # 文件1(new=本次)实际领域
            f1_row_X12 = f1_row_X[12]  # 实际意图
            f1_row_X13 = f1_row_X[13]  # 实际参数
            f1_row_X14 = f1_row_X[14]  # 实际答复
            f1_row_X15 = f1_row_X[15]  # 实际领域命中判断
            f1_row_X16 = f1_row_X[16]  # 实际意图命中判断
            f1_row_X17 = f1_row_X[17]  # 实际参数命中判断
            f1_row_X18 = f1_row_X[18]  # 实际答复命中判断
            f1_row_X19 = f1_row_X[19]  # 实际traceID
            f1_row_X9 = f1_row_X[9]    # 语境，存放于new_fail_corpus_and_context[]的list中

            f2_row_X11 = f2_row_X[11]  # 文件2(old=上次)实际领域
            f2_row_X12 = f2_row_X[12]
            f2_row_X13 = f2_row_X[13]
            f2_row_X14 = f2_row_X[14]
            f2_row_X15 = f2_row_X[15]
            f2_row_X16 = f2_row_X[16]
            f2_row_X17 = f2_row_X[17]
            f2_row_X18 = f2_row_X[18]
            f2_row_X19 = f2_row_X[19]
            f2_row_X9 = f2_row_X[9]  # 语境

            f2_corpus_result = 1
            if f2_row_X[15] == "false" or f2_row_X[16] == "false" or f2_row_X[17] == "false" or f2_row_X[
                18] == "false":
                f2_corpus_result = 0

            if f1_corpus_result == 1 and f2_corpus_result == 0:
                compare_result = "这次pass,上次fail"
                writeToExcel(writerow, compare_result, f1_corpus, f2_corpus, f1_row_X11, f1_row_X12, f1_row_X13,
                             f1_row_X14, f1_row_X15, f1_row_X16, f1_row_X17,
                             f1_row_X18, f1_row_X19, f2_row_X11, f2_row_X12, f2_row_X13, f2_row_X14, f2_row_X15,
                             f2_row_X16, f2_row_X17, f2_row_X18, f2_row_X19)
                writerow = writerow + 2
            elif f1_corpus_result == 0 and f2_corpus_result == 1:
                compare_result = "这次fail,上次pass"
                writeToExcel(writerow, compare_result, f1_corpus, f2_corpus, f1_row_X11, f1_row_X12, f1_row_X13,
                             f1_row_X14, f1_row_X15, f1_row_X16, f1_row_X17,
                             f1_row_X18, f1_row_X19, f2_row_X11, f2_row_X12, f2_row_X13, f2_row_X14, f2_row_X15,
                             f2_row_X16, f2_row_X17, f2_row_X18, f2_row_X19)

                new_fail_corpus.append(f1_corpus)  # 追加这次fail的语料
                new_fail_corpus_context.append(f1_row_X9)  # 追加这次fail的语料的语境
                writerow = writerow + 2

            elif f1_corpus_result == 0 and f2_corpus_result == 0:
                compare_result = "两次都fail"
                writeToExcel(writerow, compare_result, f1_corpus, f2_corpus, f1_row_X11, f1_row_X12, f1_row_X13,
                             f1_row_X14, f1_row_X15, f1_row_X16, f1_row_X17,
                             f1_row_X18, f1_row_X19, f2_row_X11, f2_row_X12, f2_row_X13, f2_row_X14, f2_row_X15,
                             f2_row_X16, f2_row_X17, f2_row_X18, f2_row_X19)
                writerow = writerow + 2
        j = j + 1
    i = i + 1

# 将“本次fail，上次pass”的语料保存到另一个表
for i in range(len(new_fail_corpus)):
    sheet_new_1.write(i, 0, new_fail_corpus[i])
    sheet_new_1.write(i, 1, new_fail_corpus_context[i])
    workbook_new.save('对比结果.xls')

print("\n", "结束时间 :", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 完成对比后新建目录并重命名
# os.renames("new.xlsx", newDir)
# os.renames("old.xlsx", oldDir)
# os.renames("对比结果.xls", resultDir)

