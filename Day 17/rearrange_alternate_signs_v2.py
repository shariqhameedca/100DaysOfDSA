# Time complexity: O(n)
# Space complexity: O(n)

def rearrange_alternate_signs_v2(arr):
    pos = []
    neg = []
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[i*2] = pos[i]
            arr[i*2 + 1] = neg[i]

        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[index] = pos[i]
            index += 1

    else:
        for i in range(len(pos)):
            arr[i*2] = pos[i]
            arr[i*2 + 1] = neg[i]

        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[index] = neg[i]
            index += 1


    return arr


arr = [1,2,-2,-2,1,6,4]
print(rearrange_alternate_signs_v2(arr))