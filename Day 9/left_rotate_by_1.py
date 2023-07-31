# Time Complexity: O(n)
# Space Complexity: O(1)

def left_rotate(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    
    arr[n-1] = temp

    return arr

arr = [1,5,3,4,6]
print(left_rotate(arr))
