🎉 Day 16: Array Problems [MEDIUM] 🎉<br><br>
On the 16th day of my #100DaysOfDSA challenge, I solved two challenges related to arrays

### The first problem was to find the subarray that gives the maximum sum.
I solved the problem using Kadane's Algorithm <br><br>
Let's take an array, <br>
arr = [-2, -3, 4, -1, -2, 1, 5, -3]<br><br>
Now, I iterate over the array, keeping a sum variable and a max_sum variable and aggregating it. Whenever, the sum is less than 0, we set it to 0 because we don't want negative sum to decrease the sum of a subarray if we carry it further. We also check if the sum gets greater than max_sum, we set the sum to max_sum. Whenever the sum is equal to 0, it means we have dropped a subarray and are starting a new subarray. A new subarray ends when the sum becomes greater than max_. So, I added these tweaks to get the start and end indices of the subarray that yields the most sum.
<br><br>After the iteration is complete, we return arr[start:end+1].
<br><br>
Time complexity: O(n)<br>
Space complexity: O(1)

### The second problem was to find the maximum profit we can get by buying or selling stock.
I iterated over the array and for each day I checked the minimum of the prices that appeared before that day. Subtracting today from that minimum gives you the most profit you can get if you sell today. I did this for all n prices and get the maximum profit possible. <br>

Time complexity: O(n)<br>
Space complexity: O(1)
