# coding:utf-8
import json

# 获取配置文件到本地

# 读取json文件
with open("prodconf.json", 'r') as json_f:
    json_info = json.load(json_f)
    dict_aicloud = json_info.get("ai_cloud")

    # 修改环境
    print('''
    请输入对应要切换的环境，
    1.数字0：线上
    2.数字1-8：对应预发1到预发8,
    3.数字11：预发1环境外网,
    4.数字22：预发2环境外网
    ''')
    env_choose = input("input here ：")

    if env_choose == "0":
        print("del smartbox/prodconf.json")
    elif env_choose == "1":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "xxxxx"
        dict_aicloud['server'] = "gp.xxxxx.com"   # 预发1环境
    elif env_choose == "2":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "xxxxx"
        dict_aicloud['server'] = "gp2.xxxxx.com"  # 预发2环境
    elif env_choose == "3":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "xxxxx"
        dict_aicloud['server'] = "gp3.xxxxx.com"  # 预发3环境
    elif env_choose == "4":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "xxxxx"
        dict_aicloud['server'] = "gp4.xxxxx.com"  # 预发4环境
    elif env_choose == "5":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "xxxxx"
        dict_aicloud['server'] = "gp5.xxxxx.com"  # 预发5环境
    elif env_choose == "6":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "xxxxx"
        dict_aicloud['server'] = "gp6.xxxxx.com"  # 预发6环境
    elif env_choose == "7":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "xxxxx"
        dict_aicloud['server'] = "gp7.xxxxx.com"  # 预发7环境
    elif env_choose == "8":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "xxxxx"
        dict_aicloud['server'] = "gp8.xxxxx.com"  # 预发8环境
    elif env_choose == "11":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "true"
        dict_aicloud['server'] = "gpretest-xxxxx.com"  # 预发1环境外网"
    elif env_choose == "22":
        dict_aicloud['port'] = xxxxx
        dict_aicloud['use_ssl'] = "true"
        dict_aicloud['server'] = "gdev-xxxxx.com"  # 预发2环境外网

    # 替换和写入
    json_info["ai_cloud"] = dict_aicloud
    with open("prodconf.json", 'w') as json_f:
        json_f.seek(0)  #文件指针回到头部，否则会追加
        json_f.write(json.dumps(json_info))

# 导入配置文件并重启
