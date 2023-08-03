🎉 Day 12: Array Problems [EASY] 🎉 
<br> On the 12th day of my #100DaysOfDSA challenge, I solved a challenge related to arrays.
<br><br>
The problem was to find the length of the longest contigious subarray that adds to a number k in a given non-negative array.
<br><br>
I used the two pointer approach. I kept both pointers at the beginning of the array and if the sum from l to r was less than k, I would increment r and change sum accordingly and if the sum from l to r got bigger than k, I would increment l and decrement sum accordingly. If sum from l to r got equal to k, I would update maxLen to max(maxLen, r-l+1).
<br><br>
After this process the maxLen is returned as our answer.
<br><br>
<b>Time complexity:</b> O(n)<br>
<b>Space complexity:</b> O(1)
