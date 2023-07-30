def largest(arr):
    largest_num = arr[0]
    for num in arr:
        if num > largest_num:
            largest_num = num

    return largest_num

arr = [12,14,1,2,77]
print(largest(arr))