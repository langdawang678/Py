"""
二分：https://www.runoob.com/python3/python-binary-search.html
有序序列，从中间开始找。
一个while True（也可用递归）控制4种情况：
a、当左侧index >右侧时，代表未找到
b、当匹配到时（目标值=中间值），return;
c、当目标值< 中间值时，则区间在左，右侧index = mid-1
d、当目标值> 中间值时，则区间在右，左侧index = mid+1
"""


def binary_search(listarr, target):
    right = len(listarr) - 1  # 最大索引=长度-1
    left = 0
    times = 1
    while True:
        mid = (left + right) // 2  # 中分（二分），取整
        if left > right:  # 左边的索引大于右边的索引时，代表未找到target
            print(f"target is {target},未找到")
            return
        else:
            if listarr[mid] > target:
                right = mid - 1
            elif listarr[mid] == target:
                print(f"find target's index is {mid} ,cost {times} times")
                return
            else:
                left = mid + 1
            times += 1


if __name__ == '__main__':
    # arr = [3,11,545,13,5,7,22,8]
    arr = [3, 5, 7, 8, 11, 13, 22, 545]
    binary_search(arr, 1)
    binary_search(arr, 3)
    binary_search(arr, 44)
    binary_search(arr, 544)
    binary_search(arr, 545)
    binary_search(arr, 555)
