def frequency(arr, n):
    map = {}

    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1

    return map

arr = [1,2,3,1,2,5]
print(frequency(arr, len(arr)))