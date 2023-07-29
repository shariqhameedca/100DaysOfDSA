def mergeSort(arr, low, high):
    if low >= high:
        return
    
    mid = (low+high)//2

    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)

    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    temp = []
    p = low
    q = mid+1

    while(p<=mid and q<=high):
        if arr[p]<=arr[q]:
            temp.append(arr[p])
            p += 1
        else:
            temp.append(arr[q])
            q += 1

    while(p<=mid):
        temp.append(arr[p])
        p += 1

    while(q<=high):
        temp.append(arr[q])
        q += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]

arr = [0,1,5,4,3,54,75,20]
mergeSort(arr, 0, 7)
print(arr)