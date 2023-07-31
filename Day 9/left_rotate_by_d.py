# Time complexity: O(n+d)
# Space complexity: O(d)

def left_rotate(arr, d):
    temp = []
    n = len(arr)
    for i in range(d):
        temp.append(arr[i])

    for i in range(d, n):
        arr[i-d] = arr[i]

    for i in range(n-d, n):
        arr[i] = temp[i - (n-d)]

    return arr


arr = [1,2,3,5,4]
print(left_rotate(arr, 2))