🎉 Day 18: Array Problems [MEDIUM] 🎉<br><br>
On the 18th day of my #100DaysOfDSA challenge, I solved two challenges related to arrays

### The Problem:
<b>The problem was to find the leaders in an array. A leader is an element which is greater than every element to its right.</b><br><br>
In the array, [3,2,1,4,2,0], 4, 2 and 0 are leaders, because they are greater than every element to their right sides. <br><br>
I solved the problem by back iteration. I iterated from the back of the array and kept a minimum max (-inf) at the start of iteration. If an element was greater than the current max, I appended it to the leaders array. During each iteration, I checked if the element was greater than the current max, to update the max. I iterated till I reached the start of the array, at which point I returned the leaders array as my answer. <br><br>
Time complexity: O(N)<br>
Space complexity: O(N)

