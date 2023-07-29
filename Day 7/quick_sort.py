def quick_sort(arr, low, high):
    if low < high:
        p = f(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)

def f(arr, low, high):
    piv = arr[low]
    i = low
    j = high

    while (i<j):
        while arr[i] <= piv and i <= high-1:
            i += 1
        
        while arr[j] > piv and j >= low+1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


arr = [1,0,0,0]
quick_sort(arr, 0, 3)
print(arr)
