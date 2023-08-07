# Time complexity: O(n)
# Space complexity: O(1)

def max_profit(arr):
    mini = arr[0]
    maxProfit = 0
    n = len(arr)

    for i in range(n):
        profit = arr[i] - mini
        maxProfit = max(profit, maxProfit)
        mini = min(mini, arr[i])

    return maxProfit

arr = [7,1,5,3,6,4]
print(max_profit(arr))