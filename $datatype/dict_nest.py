# coding=utf-8
# 字典存储在列表中
print('字典存储在列表中:')
alien0 = {'color': 'red', 'points': 5}
alien1 = {'color': 'green', 'points': 10}
alien2 = {'color': 'yellow', 'points': 15}

aliens = [alien0, alien1, alien2]
for a in aliens:
    print(a)

# 字典中存列表
print('\n字典中存列表:')
favorite_languages = {
    'tom': ['python', 'java'],
    'merry': ['c'],
    'jack': ['java', 'js'],
}
for name, languages in favorite_languages.items():
    print(name, languages)
    # print("\n" + name.title() + "'s favorite languages are:")
    # for language in languages:
    # print("\t" + language.title())


# 字典中存字典
print('\n字典中存字典:')
testdict = {
    'key1':{'color': '哈哈哈哈', 'points': 5},
    'key2': {'color': 'red', 'points': 15}
}
print('读取嵌套字典中的某个key的值=',testdict.get("key1").get("color"))
