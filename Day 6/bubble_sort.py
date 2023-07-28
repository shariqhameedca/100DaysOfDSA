def bubble(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [1,2,3,2,5,1]

print(bubble(arr))