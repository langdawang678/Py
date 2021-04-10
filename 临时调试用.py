#
# import os
# lists = os.system("adb devices")
# print(lists)

# coding=utf-8
import re
import os


def get_deviceid():
    adb_info = os.popen('adb devices').readlines()
    print('adb devices ：', adb_info)

    str_init = ' '
    for i in range(len(adb_info)):
        str_init += adb_info[i]

    print("****")
    print(str_init)
    print("****")

    devices_name = re.findall('\n(.+?)\t', str_init, re.S)

    print('所有设备：\n', devices_name)


get_deviceid()
