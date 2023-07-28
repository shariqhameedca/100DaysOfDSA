def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        
        arr[min], arr[i] = arr[i], arr[min]

    return arr

arr = [5,4,3,2,1]
print(selection(arr))