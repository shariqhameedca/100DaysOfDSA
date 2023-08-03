# Time complexity: O(n)
# Space complexity: O(1)

def largest_subarray(arr, k):
    n = len(arr)
    l, r = 0,0
    maxLen = 0
    sum = arr[0]
    while r < n:
        while l<=r and sum > k:
            sum -= arr[l]
            l += 1
        if (sum == k):
            maxLen = max(maxLen, r-l+1)
        r += 1
        if r < n:
            sum += arr[r]

    return maxLen

arr = [1,2,3,0,4,5]
print(largest_subarray(arr, 6))      