def insertion(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

arr = [1,2,2,0,1,5,4]
print(insertion(arr))