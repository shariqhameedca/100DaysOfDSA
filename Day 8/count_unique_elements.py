def count_unique(arr):
    i = 0
    if arr:
        for j in range(len(arr)):
            if arr[j] != arr[i]:
                arr[i+1] = arr[j]
                i += 1
    else:
        return 0
    
    return i+1

arr = [1,1,2,2,3,3]
print(count_unique(arr))