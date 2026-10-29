# 这个代码思路不是在一个组中全排序完在排下一个组，是按顺序排，排到谁再看其在哪个组
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        # 前gap个元素在每个组中已经排好序了，因为其在每个组中为第一个元素
        for i in range(gap,n):
            temp = arr[i]
            j = i
            # 在每个组中从后往前以此后移
            while j >=gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = temp
        gap = gap//2
    return arr