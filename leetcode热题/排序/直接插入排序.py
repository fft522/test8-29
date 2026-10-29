def insert_dirt(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j > 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    test_arr = [1,5,4,8,3]
    print(insert_dirt(test_arr))
