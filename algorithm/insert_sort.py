'''
# for控制轮数
# while 左大时，需要右移；通过 i=i-1控制一直往左比。
'''
def insertionSort(arr):
    for i in range(1, len(arr)):  # 从第二个开始比较
        right_value = arr[i]  # 右侧的待插入值
        while i >= 0 and arr[i-1] > right_value:  # 当下标大于0 and 左侧大时，需要右移
            arr[i] = arr[i-1]
            i -= 1  # 继续往左比，直到左值不再大于右侧目标值
        arr[i] = right_value  # 当不需要移动时，把要原始的右值，放到左侧的位置
    print("排序后的数组:", arr)


if __name__ == '__main__':
    arr = [12, 1,21,1,3,11, 13, 5, 6]
    print("排序前的数组:", arr)
    insertionSort(arr)
