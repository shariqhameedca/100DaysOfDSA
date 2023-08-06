# Time complexity: O(N)
# Space complexity: O(1)

def max_subarr_sum(arr):
    max_ = arr[0]
    sum = 0
    i = 0
    while i < len(arr):
        sum += arr[i]
        max_ = max(sum, max_)
        if sum < 0:
            sum = 0
        i += 1

    return max_

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarr_sum(arr))