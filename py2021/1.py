list1 = [8, 9, 10, 11, 12, 13, 14]
list2 = []
tmp = ()
def getArray(sum):
    for i in range(len(list1)):
        # print("-----", list1[i], end=",")
        for j in range(i + 1, len(list1)):
            # print(list1[j])
            x = sum - list1[i] - list1[j]
            if (x != list1[i]) and (x != list1[j]) and (x in list1[j:len(list1)]):
                tmp = list1[i], list1[j], x
                list2.append(sorted(tmp))
                # list2.append(tmp)
    # print(set(list2))
    print(f"{sum}的组合是{list2}\n")
    list2.clear()

getArray(31)
getArray(33)
getArray(35)