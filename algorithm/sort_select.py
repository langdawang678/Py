"""
选择排序：https://www.runoob.com/python3/python-selection-sort.html
双for循环，外层控制轮数，内层控制每轮的最小值的下标记。
每轮选择第1个数作为最小数，然后从左往右遍历出最小的。
"""
arr = [3.4, 12, 5, 77, 11, 3, 7, 8, 1]
for i in range(len(arr)-1):
    min_index = i  # 假定最左侧的是最小值
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:  # 当右侧比左侧还小时，把最小值下标给右侧，继续往右遍历
            min_index = j  # 这两个都不用到i，而是“临时变量”arr[minindex]
        #  下标给完后，也遍历结束，此时把最小值给到a[i]
        arr[min_index], arr[i] = arr[i], arr[min_index]
print(arr)
