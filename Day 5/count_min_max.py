def frequency(arr, n):
    map = {}

    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1

    min_freq = n
    max_freq = 0

    min_ele = 0
    max_ele = 0
    for key in map:
        if map[key] > max_freq:
            max_freq = map[key]
            max_ele = key

        if map[key] < min_freq:
            min_freq = map[key]
            min_ele = key

    return max_ele, min_ele

arr = [1,2,3,1,2,5]
print(frequency(arr, len(arr)))