

#山峰数组 简单
#分析 这题有点无聊 只需要寻找数组中最大值的下标 输出就行 但是这是O(n)的算法

#想一个O(log(n))的方法 其实这个就是在找数组的最大值 所以用寻找最大值的算法就能找到 所以二分查找就是最优解




# 执行用时：36 ms, 在所有 Python3 提交中击败了45.18%的用户
# 内存消耗：15.8 MB, 在所有 Python3 提交中击败了62.25%的用户



List = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
def PeakIndexInMountainArray (list):
    length = len(list)
    t = list[0]
    for i in range(1, length):
        if list[i] > t:
            q = i
            t = list[i]
    print(q)

#二分查找
def PeakIndexInMountainArray_erfen(list):
    length = len(list)
    left, right, ans = 1, length-2, 0
    while left <= right:
        mid = (left + right) // 2
        if list[mid] > list[mid+1]:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    print(ans)

PeakIndexInMountainArray_erfen(List)
# PeakIndexInMountainArray(List)
