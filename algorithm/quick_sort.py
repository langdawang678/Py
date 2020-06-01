'''
https://zhuanlan.zhihu.com/p/63227573
基准元素，一般来说选取有几种方法:
取第一个元素
取最后一个元素
取第中位置元素间
取第一个、最后一个、中间位置3者的中位数元素

选择一个基准数，通过一趟排序后，
将原序列分为两部分，使得前面的比后面的小，
然后再依次对前后进行拆分进行快速排序，递归该过程，直到序列中所有记录均有序。

'''


def quick_sort(lists, i, j):
    if i >= j:
        return list
    pivot = lists[i]  # 1: 首先取序列第一个元素为基准元素pivot=R[low]
    low = i
    high = j
    while i < j:
        # 2：从后向前扫描，找小于等于pivot的数，如果找到，R[i]与R[j]交换，i++。
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        # 3：从前往后扫描，找大于pivot的数，如果找到，R[i]与R[j]交换，j--
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[j] = pivot
    quick_sort(lists, low, i - 1)
    quick_sort(lists, i + 1, high)
    return lists


if __name__ == "__main__":
    lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    print("排序前的序列为：", lists)
    print("\n排序后的序列为：", quick_sort(lists, 0, len(lists)-1))
