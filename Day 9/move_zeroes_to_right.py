# Time complexity: O(N)
# Space complexity: O(1)

def move_zeros(arr):
    j = -1
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

arr = [1,2,0,2,0,5]
print(move_zeros(arr))