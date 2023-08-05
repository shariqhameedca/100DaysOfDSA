# Time complexity: O(n)
# Space complexity: O(1)

def sort_012s(arr):
    n = len(arr)
    low, mid = 0, 0
    high = n-1

    while mid < high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
        
    return arr

arr = []
sorted_arr = sort_012s(arr)
print(sorted_arr)