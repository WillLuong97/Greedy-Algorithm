#Python3 implementation of the Leetcode problem 376, Wiggle Subsequences
#The problem will mainly focus on the Greedy approach

'''
Problem statement: 
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. 
The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. 
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. 
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

Follow up: 
Can you do it in O(n) time?
'''


def wiggleLength(nums):
	#base case: 
	if not nums: 
		return 0
	# If the nums lenght is lesser than 2, then it is trivially a wiggle sequence
	if len(nums) < 2: 
		return len(nums)

	return 1 + max(calculate(nums, 0, True), calculate(nums, 0, False))

#Recursive helper method that takes in the array nums, the index from which we need 
#to find the length of the longest wiggle subsequent, boolean variable isUp to tell 
# whether we need to find a decreasing or increaseing wiggle.
def calculate(nums, index, isUp):
	maxLenghtCount = 0
	for i in range(index + 1, len(nums)):
		if (isUp and nums[i] > nums[index]) or (not isUp and nums[i] < nums[index]):
			maxLenghtCount = max(maxLenghtCount, 1 + calculate(nums, i, not isUp))

	return maxLenghtCount

#main function to test and run the algorithm 
def main():
	print("TESTING WIGGLE SUBSEQUENCE...")

	test_case_1 = [1,7,4,9,2,5]
	test_case_2 = [1,17,5,10,13,15,10,5,16,8]
	test_case_3 = [1,2,3,4,5,6,7,8,9]

	print(wiggleLength(test_case_1))
	print(wiggleLength(test_case_2))
	print(wiggleLength(test_case_3))


	print("END OF PROGRAM...")
main()




