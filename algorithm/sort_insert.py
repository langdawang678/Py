def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]  # 每一轮，右侧的待插入值
        j = i-1  # 控制key值左侧的下标
        while j >= 0 and a[j] >key:  # 当下标大于0 and 左侧大时，需要右移
            a[j + 1] = a[j]  #右移，这里不是赋值给arr[i],因为arr[i]在外层是固定的
            j -= 1  # 继续往左比，直到左值不再大于右侧目标值
        a[j + 1] = key  # 当不需要移动时，把要原始的右值，放到左侧的位置。j+1是因为while后，j-1了，然后while不成立
    print("排序后的数组:", a)


if __name__ == '__main__':
    arr = [12, 1,21,1,3,11, 13, 5, 6]
    print("排序前的数组:", arr)
    insertionSort(arr)

"""
插入排序：https://www.runoob.com/python3/python-insertion-sort.html
从左往右大的值往右插
外层for控制轮数，
内层从第二个开始（下标1）while左大时，需要右移；通过 i=i-1控制一直往左比。
当不需要移动时，把要原始的右值，放到左侧的位置。
"""
