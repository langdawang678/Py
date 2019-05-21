'''
申明，长度，最大最小值，append()/insert()，引用和修改。
del/pop()/remove()
'''

a = 1
bcd = 2
l1 = [a, bcd, 'efg', 123, '456', '哈哈']
print('this is my first list1:', l1)
print(len(l1))
print(max(str(l1)))

t1 = (1, 2, 'a', 'bc', '哈哈')
print(type(t1))
l2 = list(t1)
print(type(l2))

l2[4] = "哈哈哈"
print(l2[4])

# append末尾添加元素,insert制定位置添加元素
l2.append("appended")
print('append:', l2)
l2.insert(0, "inserted")
print("insert:", l2)

#del直接删除。pop()一般删除后要用，可pop(具体位置)。remove()具体的值。
del l2[0]
print('del [0]:', l2)
tmp_poped = l2.pop()
print('pop:', tmp_poped)
l2.remove('哈哈哈')
print(l2)

# sort()按字母排序。sort(reverse=True)按字母反序。。reverse()直接倒序。
l3 = ['c', 'a', 'b']
l3.sort()
print('sort:', l3)
#print('sort(reverse=True):', l3.sort(reverse=True)
#print('reverse:', l3.reverse())
