"""
##一个while True，直到匹配到时，return;或者次数超过长度一半时return
"""
def binary_search(arr, target):
    right = len(arr)-1  # 最大索引=长度-1
    left = 0
    times = 1
    while True:
        mid = (left + right) // 2  # 中分（二分），取整
        if left > right:    # 左边的索引大于右边的索引时，代表未找到target
            print(target, "未找到")
            return
        else:
            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] == target:
                print("find target's index is", mid, ",cost %d times" % times)
                return
            else:
                left = mid + 1
            times += 1

if __name__ == '__main__':
    # arr = [3,11,545,13,5,7,22,8]
    arr =  [3, 5, 7, 8, 11, 13, 22, 545]
    binary_search(arr, 1)
    binary_search(arr, 3)
    binary_search(arr, 44)
    binary_search(arr, 544)
    binary_search(arr, 545)
    binary_search(arr, 555)