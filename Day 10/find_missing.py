# Time complexity: O(n)
# Space complexity: O(1)

def find_missing(arr, N):
    xor1 = 0
    xor2 = 0
    n = N-1
    for i in range(n):
        xor1 = xor1 ^ (i+1)
        xor2 = xor2 ^ arr[i]

    xor1 = xor1 ^ N
    return xor1 ^ xor2

arr = [1,2,4,5]
print(find_missing(arr, 5))