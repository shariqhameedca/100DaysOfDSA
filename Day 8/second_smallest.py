import math

def second_smallest(arr):
    smallest = arr[0]
    ssmallest = math.inf

    for i in range(len(arr)):
        if arr[i] < smallest:
            ssmallest = smallest
            smallest = arr[i]
        else:
            if arr[i] < ssmallest and arr[i] != smallest:
                ssmallest = arr[i]

    return ssmallest

arr = [1,2,6,2,1]
print(second_smallest(arr))