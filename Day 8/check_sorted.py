def check_sort(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
            break
    return sorted

arr = [1,2,2,3,5]
print(check_sort(arr))