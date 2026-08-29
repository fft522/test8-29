def select_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_key = i
        for j in range(i+1,n):
            if arr[min_key] > arr[j]:
                min_key = j
        arr[min_key],arr[i] = arr[i],arr[min_key]
    return arr

if __name__ =="__main__":
    test_arr = [1,5,3,8,4,2]
    select_sort(test_arr)
    print(test_arr)
