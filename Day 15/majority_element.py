# Time complexity: 
# Space complexity:
import math

def majority_element(arr):
    n = len(arr)
    cnt = 0

    for i in range(n):
        if cnt == 0:
            cnt = 1
            element = arr[i]
        elif arr[i] == element:
            cnt += 1
        else:
            cnt -= 1

    cnt_ele = 0
    for i in range(n):
        if arr[i] == element:
            cnt_ele += 1

    if cnt_ele > math.ceil(n/2):
        return element
    
    return -1

arr = [1,1,4,4,4,1,1,1]
print(majority_element(arr))
