🎉 Day 15: Array Problems [MEDIUM] 🎉<br><br>
On the 15th day of my #100DaysOfDSA challenge, I solved two challenges related to arrays

### The first problem was to find the majority element in an array that appears more than n/2 times.
I solved the problem using Moore's Voting Algorithm. <br><br>
Let's take an array, <br>
arr = [1,1,4,4,4,1,1,1]<br>
<br>Now, I iterate over the array. I keep two variables, count and element. In the begining, I set element to the first element and set the count to 1. Now, next when the element reappears I increment the count otherwise I decrement it. When the count becomes 0 at any instant, I change the element that appears after this instant and begin doing the same steps for that element. In the end, I iterate over the whole array and hold a specific element in the array. This element is my potential answer, then I check if this element appears more than n//2 times in the array. I do that with a single iteration. 
<br>

Time complexity: O(n)<br>
Space complexity: O(1)

### The second problem was to find the maximum sub array sum.
I solved the problem using Kadane's Algorithm <br><br>
Let's take an array, <br>
arr = [-2, -3, 4, -1, -2, 1, 5, -3]<br><br>
Now, I iterate over the array, keeping a sum variable and a max_sum variable and aggregating it. Whenever, the sum is less than 0, we set it to 0 because we don't want negative sum to decrease the sum of a subarray if we carry it further. We also check if the sum gets greater than max_sum, we set the sum to max_sum.
<br><br>After the iteration is complete, we return the max_sum.
<br><br>
Time complexity: O(n)<br>
Space complexity: O(1)
