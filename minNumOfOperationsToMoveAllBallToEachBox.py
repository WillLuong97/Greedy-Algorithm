#1769. Minimum Number of Operations to Move All Balls to Each Box

'''
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.
Example 1:

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
Example 2:

Input: boxes = "001011"
Output: [11,8,5,4,3,4]
 

Constraints:

n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.
'''
#Brainstorming: 
'''
"110" => There are three box, and two box have one ball each and one box is empty
  (1) (1) 
a -> b -> c
    (2)
"1": 1 ball
"0": no ball

[1, , ] 

how to count the steps to get the ball from one bag to another? 
- steps = abs(j-i)

To save time, we only want to perform the operations on the bags with ball and ignore bags with no balls.
How to only look at the bags with ball? And backtrack if the bags before the current bags has ball. 
- Make a copy of the stirng but in an array form but only put in it the non-empty bags.
Example array = [1,1,NULL]

once we know where to look at, we can perform the search on the new array 
just loop through the new search space and add the count together
 
=>GOALS: Return an array of answer with size n that contains the number of steps each operations would take to carray all the ball into that bag
'''
def minOperations(boxes):
	n = len(boxes) 
	result = [0] * n
	modified = [-1] * n
	#loop through the original string and assign only the inde that containst the 1 value into the modified array 
	for i in range(n):
		if boxes[i] == "1":
			modified[i] = i
	
	#loop through the modified array and count the steps it would take to move all the ball from other bags into it
	for i in range(n):
		result[i] = sum([abs(modified[j] - i) for j in modified if j != -1])
	return result
			


#Main function to test the program: 
def main():
	print("TESTING Minimum Number of Operations to Move All Balls to Each Box...")
	boxes = "110"
	print(minOperations(boxes))
	boxes = "001011"
	print(minOperations(boxes))


	print("END OF TESTING...")

main()
