def quick_sort(arr,start,end):
    if start >= end:
        return arr
    left = start
    right = end
    mid = arr[left]

    while left < right:
        while arr[right] >= mid and left < right:
            right = right -1
        arr[left] = arr[right]
        while arr[left] <= mid and left < right:
            left = left +1
        arr[right] = arr[left]
    arr[left] = mid
    quick_sort(arr,start,left-1)
    quick_sort(arr,right+1,end)

if __name__ == "__main__":
    test_arr = [1,2,5,6,3,4]
    quick_sort(test_arr,0,len(test_arr)-1)
    print(test_arr)