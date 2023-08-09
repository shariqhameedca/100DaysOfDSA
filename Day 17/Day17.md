🎉 Day 17: Array Problems [MEDIUM] 🎉<br><br>
On the 17th day of my #100DaysOfDSA challenge, I solved two challenges related to arrays

### The first problem:
<b>The first problem was to sort an array of positive and negative elements into an array of alternating positive and negative elements</b><br><br>
I solved the problem by iterating through the array and making two seperate arrays pos and neg. <br><br>
After that I rearranged the original array by taking elements from pos and putting them at even while elements from neg at odd positions.
Let's take an array, <br>
arr = [-2, -3, 4, -1, 2, 1,7,3,2]<br><br>
Now, I iterate over the array, and make pos and neg <br><br>
pos = [4,1,5,7,3,2], neg=[-2,-3,-1]
<br><br>After this, we rearrange the original array by taking elements from the pos and neg and putting them in even and odd positions respectively. The elements that are left are added as it is.
<br><br>
arr = [4,-2,1,-3,5,-1,7,3,2]
Time complexity: O(n)<br>
Space complexity: O(n)

### The second problem:
<b> The second problem was to sort an array of positive and negative elements if the array has the same number of positives and negatives. </b><br><br>
I iterated over the array and kept two variables availablePos and availableNeg as the available indices where we can put positive and negative elements respectively. I created a temp array of size equal to array with some garbage values, if during the iteration an element was positive I added it to the temp array at the availablePos position and updated the availablePos position by adding 2 to it, I did similar thing for the negative elements.<br><br>
After this I returned the temp array as my answer<br><br>

Time complexity: O(n)<br>
Space complexity: O(n)
