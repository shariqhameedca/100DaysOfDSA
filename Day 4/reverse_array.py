def reverse_arr(arr, start, end):
    if (start<end):
        arr[start], arr[end] = arr[end], arr[start]
        reverse_arr(arr, start+1, end-1)

arr = [1,2,3,4,5]
reverse_arr(arr, 0, 4)
print(arr)