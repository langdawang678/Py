# arr = [3,1,4,5]
# for i in range(len(arr)):
#     min_index = i  # 假定最左侧的是最小值
#     print(i)
#     for j in range(i + 1, len(arr)):
#         print("i=",i,"j=",j)
#         if arr[j] < arr[min_index]:  # 当右侧比左侧还小时，把最小值下标给右侧，继续往右遍历
#             min_index = j  # 这两个都不用到i，而是“临时变量”arr[minindex]
#         #  下标给完后，也遍历结束，此时把最小值给到a[i]
#         arr[min_index], arr[i] = arr[i], arr[min_index]
#     print("---")
# print(arr)

for j in range(5,4):
    print(j)
    ##