# Time complexity: O(n)
# Space complexity: O(1)

def max_subarr_sum(arr):
    max_ = arr[0]
    sum = 0
    i = 0
    ansStart = -1
    ansEnd = -1
    while i < len(arr):
        if sum == 0:
            start = i
        sum += arr[i]
        if sum > max_:
            max_ = sum
            ansStart = start
            ansEnd = i
        if sum < 0:
            sum = 0
        i += 1

    return arr[ansStart: ansEnd+1]

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarr_sum(arr))