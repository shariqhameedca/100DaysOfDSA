# Time complexity: O(n)
# Space complexity:

def rearrange_alternate_signs(arr):
    temp = len(arr) * [0]
    available_pos = 0
    available_neg = 1

    for i in range(len(arr)):
        if arr[i] > 0:
            temp[available_pos] = arr[i]
            available_pos += 2
        elif arr[i] < 0:
            temp[available_neg] = arr[i]
            available_neg += 2

    return temp

arr = [2,3,-2,-5,1]
print(rearrange_alternate_signs(arr))
