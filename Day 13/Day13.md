🎉 Day 13: Array Problems [MEDIUM] 🎉 
<br> On the 13th day of my #100DaysOfDSA challenge, I solved a challenge related to arrays.
<br><br>
The problem was to find if two numbers in an unsorted array adds upto a target number.
<br><br>
I used the two pointer approach. I first sorted the array in nlogn time complexity and then I kept left and right pointers and found the sum of numbers at those indices. 
<br><br>If the sum was
<ul>
  <li>Equal to target: I returned True</li>
  <li>Less than target: I incremented left pointer</li>
  <li>Greater than target: I decremented right pointer</li>
</ul>
If at any point the left pointer and right pointer colide, I return False.<br><br>
<b>Time complexity:</b> O(n+nlogn)<br>
<b>Space complexity:</b> O(1)
