# Time complexity: O(N)
# Space complexity: O(1)

def linear_search(arr, target):
    n = len(arr)

    for i in range(n):
        if arr[i] == target:
            return i

    return -1

arr = [1,2,4,6,3]
print(linear_search(arr, 1))