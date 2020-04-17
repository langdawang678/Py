import time
import xlrd,xlwt,os,time

#存放原excel到todo、存储文件路径名、文件个数
excelpath='./todo/'
for parent, dirnames, filenames in os.walk(excelpath):
    fileslist = []
    for filename in filenames:
        fileslist.append(excelpath + filename)
print(fileslist)
localtime = time.asctime( time.localtime(time.time()) )
print ("开始时间 :", localtime)
wenjianshu=0
wenjiangeshu=len(fileslist)

#打开被写的excel，建立新表
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('0')

#读第一个文件，在新文件写入第一行的固定值,并保存
test_excel=xlrd.open_workbook(fileslist[0])
table=test_excel.sheets()[0]
firstrow =table.row_values(0)
j = 0
while j < table.ncols:
    firstdata = firstrow[j]
    print(firstdata)
    worksheet.write(0, j, firstdata)
    j = j + 1
workbook.save('newexcel.xls')

#外层循环控制文件：打开第x个原excel，并获取各自的第0张表格
allrows = 1
while wenjianshu < wenjiangeshu:
    test_excel=xlrd.open_workbook(fileslist[wenjianshu])
    table=test_excel.sheets()[0]
    #中层循环控制行数：
    hangshu=1
    while hangshu <table.nrows:
        row_hangzhi = table.row_values(hangshu)
        #内层循环控制列的位置和该列对应的值
        lieshu = 0
        while lieshu < table.ncols:
            data = row_hangzhi[lieshu]
            worksheet.write(allrows, lieshu, data)
            lieshu = lieshu+1
        hangshu=hangshu+1
        allrows = allrows + 1
    wenjianshu =wenjianshu+1
print(allrows)
print ("结束时间 :", localtime)
workbook.save('newexcel.xls')

'''todo 
第二个文件读取，再写入all.xls，注意1不写第一行，追加写入。
时间格式的处理
'''