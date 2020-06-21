import json
# 1.一般是先读取json文件为字典，load
with open("json.json") as fp:
    jsoninfo = json.load(fp)  # jsoninfo为字典
    print("1.读取.json文件后的类型：",type(jsoninfo),"\n")  # <class 'dict'>

# 2.再把字典序列化为json字符串（list,touple也同为pyobj）
list1 =['a','2','#']
print("2.把字典序列化后的类型：",type(json.dumps(jsoninfo)))  # <class 'str'>
print("2.把列表序列化后的类型：",type(json.dumps(list1)),"\n")  # <class 'str'>

# 3.反序列化=json字符串loads为py对象（只有列表和字典），
json_str=json.dumps(jsoninfo)  # <class 'str'>
pyobj = json.loads(json_str)
print("3.字符串的反序列化后：",type(pyobj),"\n")  # <class 'dict'>

print('4.把信息(一般是字典)写入json文件')
# 方法1：json.dump (json_info, file)
# with open('cookie_tmp.json', 'w') as fp:
#     json.dump(jsoninfo,fp)

# 方法2：json_f.write(json.dumps(json_info))
with open('cookie_tmp.json', 'w') as fp:
    fp.write(json.dumps(jsoninfo))
