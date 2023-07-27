def hashed_arr(arr):
    hashed_arr = len(arr)*[0]

    for num in arr:
        hashed_arr[num] += 1

    return hashed_arr

print(hashed_arr([1,1,2,3,4,2]))