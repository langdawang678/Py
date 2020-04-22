# coding:utf-8
import json
import os
# 获取配置文件到本地
# os.system("adb pull xxx)

# 读取json文件
with open("xxx.json", 'r') as json_f:
    json_info = json.load(json_f)
    print(json_info)
    dict_aicloud = json_info.get("ai_cloud")
    print(dict_aicloud)

    # 修改环境
    print('''
    请输入对应要切换的环境，
    1.数字0：线上
    2.数字1-8：对应预发1到预发8,
    3.数字11：预发1环境外网,
    4.数字22：预发2环境外网
    ''')

    env_choose= input("input here ：")
    if env_choose == "1":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "false"
        dict_aicloud["server"] = "gp..com"   # 预发1环境
    elif env_choose == "2":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "false"
        dict_aicloud["server"] = "gp2..com"  # 预发2环境
    elif env_choose == "3":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "false"
        dict_aicloud["server"] = "gp3..com"  # 预发3环境
    elif env_choose == "4":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "false"
        dict_aicloud["server"] = "gp4..com"  # 预发4环境
    elif env_choose == "5":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "false"
        dict_aicloud["server"] = "gp5..com"  # 预发5环境
    elif env_choose == "6":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "false"
        dict_aicloud["server"] = "gp6..com"  # 预发6环境
    elif env_choose == "7":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "false"
        dict_aicloud["server"] = "gp7..com"  # 预发7环境
    elif env_choose == "8":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "false"
        dict_aicloud["server"] = "gp8..com"  # 预发8环境
    elif env_choose == "11":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "true"
        dict_aicloud["server"] = "1..com"  # 预发1环境外网"
    elif env_choose == "22":
        dict_aicloud["port"] = 80
        dict_aicloud["use_ssl"] = "true"
        dict_aicloud["server"] = "1...com"  # 预发2环境外网
    else:
        os.system("adb shell rm xxx/xxx/xxx.json")
        os.system("adb shell sync")
        os.system("adb reboot")
        print("rebooting")

# 替换和写入
json_info["ai_cloud"] = dict_aicloud
json.dump(json_info, open("xxx.json", "w"))

# with open("xxx.json", 'w') as json_f:
#     # json_f.seek(0)  #文件指针回到头部，否则会追加
#     json_f.write(json.dumps(json_info))  # 【文件对象，写入字典序列化后的字符串】和直接json.dump有同样效果
# os.system("adb push xxxx.json /xxx/xxxx")
# os.system("adb shell sync")
# os.system("adb reboot")

