# Time complexity: O(N) + O(NlogN)
# Space complexity: O(1)

def twoSum(arr, target):
    arr = sorted(arr) # Takes NlogN at best, depending on the sorting algorithm, e.g: Quick Sort
    left = 0
    right = len(arr)-1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1

    return False

arr = [3,5,2,6,1]
print(twoSum(arr, 2))
