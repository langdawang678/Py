#实现功能：统计原log总行数，总devID数，总的online和offline数，打印设备主要信息（name、PK、name）

#步骤1：获取APP的MTOP接口getalldevice的response
#步骤2：同目录新建log.txt并保存[步骤1]的response
#步骤3：python3环境运行，将在同目录下输出新的文件newlog.txt

with open("log.txt", encoding='utf-8', errors='ignore') as file:
    list1 = file.readlines()
print("log文件行数：", len(list1))

sum = []
devSum= []
onlineSum = []
offlineSum = []
for i in list1:
    # if '"devId":' or '"devName":'or'"productKey":' or '"onlineState":'in i:
    if '"devId"' in i:
        sum.append("----------------------------------------------\n")
        sum.append(i)
        devSum.append(i)
    if '"devName"'in i:
        sum.append(i)
    if '"productKey"'in i:
         sum.append(i)
    if '"name"'in i:
        sum.append(i)
    if '"onlineState":"online"'in i:
        onlineSum.append(1)
        sum.append(i)
    if '"onlineState":"offline"'in i:
        offlineSum.append(1)
        sum.append(i)

onlinenums = "有onlinestatus的online设备数：" + str(len(onlineSum)) + "\n"
offlinenums = "有onlinestatus的offline设备数：" + str(len(offlineSum)) + "\n"
devnums = "devId总数：" + str(len(devSum)) + "\n"
print(onlinenums)
print(offlinenums)
print(devnums)
# print(sum)
with open("newlog.txt", "w" , encoding='utf-8', errors='ignore') as file2:
    file2.writelines(onlinenums)
    file2.writelines(offlinenums)
    file2.writelines(devnums)
    file2.writelines(sum)