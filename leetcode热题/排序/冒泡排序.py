def bubble_sort(arr):
    n = len(arr)
    # 只需要排n-1轮即可
    for i in range(n-1):
        swapped = False
        # 每轮比较n-1-i次，因为没比较一轮，就归位一个元素
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    test_arr = [1,5,6,2]
    print(bubble_sort(test_arr))