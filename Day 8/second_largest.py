import math

def sec_largest(arr):
    largest = arr[0]
    slargest = -math.inf
    for i in range(len(arr)):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        else:
            if arr[i] > slargest and arr[i] < largest:
                slargest = arr[i]

    return slargest

arr = [12,15,15,3,6,13,13]
print(sec_largest(arr))
            