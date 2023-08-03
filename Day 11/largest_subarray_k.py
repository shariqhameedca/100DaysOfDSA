# Time complexity: O(n^2)
# Space complexity: O(n)

def largest_subarray(arr, k):
    sumMap = {}
    maxLen = 0
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum == k:
            maxLen = max(maxLen, i+1)
        rem = sum - k
        if rem in sumMap.keys() and sumMap[rem] != sumMap[-1]:
            len_ = i - sumMap[rem]
            maxLen = max(maxLen, len_)
        
        if rem in sumMap.keys() and sumMap[rem] == sumMap[-1]:
            sumMap[sum] = i

    return maxLen

arr = [1,2,3,0,4,5]
k = 6
ret_ = largest_subarray(arr, k)
print(ret_)

