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

#RECURSION METHOD WOULD RUN INTO TIME COMPELXITY PROBLEM IF THE STRING IS TOO BIG
# def wiggleLength(nums):
# 	#base case: 
# 	if not nums: 
# 		return 0
# 	# If the nums lenght is lesser than 2, then it is trivially a wiggle sequence
# 	if len(nums) < 2: 
# 		return len(nums)

# 	return 1 + max(calculate(nums, 0, True), calculate(nums, 0, False))

# #Recursive helper method that takes in the array nums, the index from which we need 
# #to find the length of the longest wiggle subsequent, boolean variable isUp to tell 
# # whether we need to find a decreasing or increaseing wiggle.
# def calculate(nums, index, isUp):
# 	maxLenghtCount = 0
# 	for i in range(index + 1, len(nums)):
# 		if (isUp and nums[i] > nums[index]) or (not isUp and nums[i] < nums[index]):
# 			maxLenghtCount = max(maxLenghtCount, 1 + calculate(nums, i, not isUp))

# 	return maxLenghtCount

#Time complexity: O(n^2)
#Space complexity: O(N), the recursion stack would create space until it reaches the the end of the array


#Optimeze result: One-pass check
#Time complexity: O(n) as we only look through every element in the array once
#Space complexity: O(1) constant times as we do not create any extra spaces. 
def wiggleLength_OPTIMIZED(nums):
	#base case: 
	if not nums: 
		return 0
	if len(nums) < 2: 
		return len(nums)
	#variable to hold subsequent length
	result = 1
	prev_difference = 0
	#loop through the array from 1 to the end of the array
	for i in range(1, len(nums)):
		#each iteration: find the difference between the current element with the previous element
		curr_difference = nums[i] - nums[i-1]
		#if there is a change in sign happens between the current and next differences.
		if(curr_difference < 0 and prev_difference >= 0) or (curr_difference > 0 and prev_difference <= 0):
			result += 1
			prev_diff = curr_difference

	return result


	
#main function to test and run the algorithm 
def main():
	print("TESTING WIGGLE SUBSEQUENCE...")

	test_case_1 = [1,7,4,9,2,5]
	test_case_2 = [1,17,5,10,13,15,10,5,16,8]
	test_case_3 = [1,2,3,4,5,6,7,8,9]
	test_case_4 = [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]

	print(wiggleLength_OPTIMIZED(test_case_1))
	print(wiggleLength_OPTIMIZED(test_case_2))
	print(wiggleLength_OPTIMIZED(test_case_3))
	print(wiggleLength_OPTIMIZED(test_case_4))



	print("END OF PROGRAM...")
main()




