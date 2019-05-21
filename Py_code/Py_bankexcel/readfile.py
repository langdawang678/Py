# import  xlrd,xlwt
# #读取文件夹的文件名存入txt
# import os
# import os.path
# # rootdir = "."
# # file_object = open('train_list.txt','w')
# # for parent,dirnames,filenames in os.walk(rootdir):
# #     for filename in filenames:
# #         print (filename)
# #         file_object.write(filename+ '\n')
# # file_object.close()
#
# class Read_files():
#     def __init__(self,filepath):
#         self.filepath=filepath
#
#     def readfiles(self):
#         for parent,dirnames,filenames in os.walk(self.filepath):
#             filelists=[]
#             for filename in filenames:
#                 filelists.append(self.filepath +filename)
#         print('当前需要处理的文件有：'+str(len(filelists))+'个,\n'+'文件名为：'+str(filelists))
#
#         # wenjianshu=0
#         # wenjiangeshu=len(filelists)
#         # allrows=0
#         # while wenjianshu < wenjiangeshu:
#         #     test_excel=xlrd.open_workbook(filelists[wenjianshu])
#         #     table=test_excel.sheets()[0]
#         #     thisrows = table.nrows
#         #     print(thisrows)
