def binary_insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        left = 0
        right = i -1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] > key:
                right = mid - 1
            else:
                left  = mid + 1
        # 这个表示从i-1，到left 进行倒序循环 例如i-1 = 5，left = 2，则会5，4，3，2这么循环
        for j in range(i-1,left-1,-1):
            arr[j+1] = arr[j]
        arr[left] = key
    return arr

if __name__ == "__main__":
    test_arr = [1,2,3,5,8,4,2]
    print(binary_insert_sort(test_arr))
