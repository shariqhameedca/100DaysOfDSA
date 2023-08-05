🎉 Day 14: Array Problems [MEDIUM] 🎉 
<br> On the 14th day of my #100DaysOfDSA challenge, I solved a challenge related to arrays.
<br><br>
The problem was to sort an array of 0s, 1s and 2s in a linear time complexity and constant space complexity. 
<br><br>
I used the Dutch national flag algorithm (DNF). I iterated over the array, keeping three pointers: low, mid and high.
<br>If arr[mid] was:
<ul>
  <li>0: I swapped arr[med] and arr[low] and incremented both med and low pointers</li>
  <li>1: I incremented the med pointer and did nothing else</li>
  <li>2: I swapped arr[med] and arr[high] and decremented the high pointer</li>
</ul>
If at any point, the med and high pointer collide, I returned the array as it gets totally sorted at this point.
<br><br>
<b>Time complexity:</b> O(n)<br>
<b>Space complexity:</b> O(1)
