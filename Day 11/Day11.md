🎉 Day 11: Array Problems [EASY] 🎉 
<br> On the 11th day of my #100DaysOfDSA challenge, I solved a challenge related to arrays.
<br><br>
The problem was to find the length of the longest contigious subarray that adds to a number k in a given array (with zeroes and negatives).
<br><br>
I used hashmap for the solution. I looped through the array accumulating the sum and adding the sum to the hashmap with the index upto which the sum is calculated, (sum=key, index=value).
<br><br>
Also, I checked at a particular index if sum - k existed in the hashmap becuase if that exists I change the maxLength to max(maxLen, i - hashmap[sum-k]). 
<br><br>
After this process the maxLen is returned as our answer.
<br><br>
<b>Time complexity:</b> O(n^2)<br>
<b>Space complexity:</b> O(n)
