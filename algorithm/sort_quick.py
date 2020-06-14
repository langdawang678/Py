"""
https://blog.csdn.net/weixin_43250623/article/details/88931925
基准元素，一般来说选取有几种方法:取第一个元素

选择一个基准数，通过一趟排序后，
将原序列分为两部分，使得前面的比后面的小，
然后再依次对前后进行拆分进行快速排序，递归该过程，直到序列中所有记录均有序。

"""
def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:  # 递归的退出条件
        return
    mid = alist[start]  # ！设定起始的基准元素
    i = start  # i为序列左边在开始位置的由左向右移动的游标
    j = end  # j为序列右边末尾位置的由右向左移动的游标
    while i < j:
        while i < j and alist[j] >= mid:
            # 如果i与j未重合，j(右边)指向的元素大于等于基准元素，则j向左移动
            j -= 1
        alist[i] = alist[j]
        # 走到此位置时j指向一个比基准元素小的元素,将j指向的元素放到i的位置上,
        # 此时j指向的位置空着,接下来移动i找到符合条件的元素放在此处

        while i < j and alist[i] <= mid:
            # 如果i与j未重合，i指向的元素比基准元素小，则i向右移动
            i += 1
        alist[j] = alist[i]
        # 此时i指向一个比基准元素大的元素,将i指向的元素放到j空着的位置上,
        # 此时i指向的位置空着,之后进行下一次循环,将j找到符合条件的元素填到此处

    # 退出循环后，i与j重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    alist[i] = mid  # ！将基准元素放到位置i=j,因为i已经赋值给其他;是mid不是alist[start]
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, i - 1)  # start :0  i -1 原基准元素靠左边一位
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, i + 1, end)  # i+1 : 原基准元素靠右一位  end: 最后



if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
