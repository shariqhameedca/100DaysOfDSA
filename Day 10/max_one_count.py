# Time complexity: O(n)
# Space complexity: O(1)

def max_one_count(arr):
    maximum = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            if count >= maximum:
                maximum = count
        else:
            count = 0

    return maximum

arr = [1,1,1,0,0,1,1,0,1,1,1,1,1,1]
print(max_one_count(arr))