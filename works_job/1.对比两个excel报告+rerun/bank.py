import time
import xlrd,xlwt,os,time

#���ԭexcel��todo���洢�ļ�·�������ļ�����
excelpath='./todo/'
for parent, dirnames, filenames in os.walk(excelpath):
    fileslist = []
    for filename in filenames:
        fileslist.append(excelpath + filename)
print(fileslist)
localtime = time.asctime( time.localtime(time.time()) )
print ("��ʼʱ�� :", localtime)
wenjianshu=0
wenjiangeshu=len(fileslist)

#�򿪱�д��excel�������±�
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('0')

#����һ���ļ��������ļ�д���һ�еĹ̶�ֵ,������
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

#���ѭ�������ļ����򿪵�x��ԭexcel������ȡ���Եĵ�0�ű��
allrows = 1
while wenjianshu < wenjiangeshu:
    test_excel=xlrd.open_workbook(fileslist[wenjianshu])
    table=test_excel.sheets()[0]
    #�в�ѭ������������
    hangshu=1
    while hangshu <table.nrows:
        row_hangzhi = table.row_values(hangshu)
        #�ڲ�ѭ�������е�λ�ú͸��ж�Ӧ��ֵ
        lieshu = 0
        while lieshu < table.ncols:
            data = row_hangzhi[lieshu]
            worksheet.write(allrows, lieshu, data)
            lieshu = lieshu+1
        hangshu=hangshu+1
        allrows = allrows + 1
    wenjianshu =wenjianshu+1
print(allrows)
print ("����ʱ�� :", localtime)
workbook.save('newexcel.xls')

'''todo 
�ڶ����ļ���ȡ����д��all.xls��ע��1��д��һ�У�׷��д�롣
ʱ���ʽ�Ĵ���
'''
