# Time Complexity: O(N)
# Space Complexity: O(N)
import math

def find_leaders(arr):
    max_ = -math.inf
    i = len(arr)-1
    leaders = []
    while i >= 0:
        # print(arr[i])
        if arr[i] > max_:
            leaders.append(arr[i])
        
        max_ = max(max_, arr[i])
        i -= 1

    return leaders

arr = [1,4,2,3,2]
print(find_leaders(arr))