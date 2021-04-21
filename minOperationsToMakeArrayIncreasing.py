#Problem 1827. Minimum Operations to Make the Array Increasing

'''
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.
Example 1:
Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].
Example 2:

Input: nums = [1,5,2,4,1]
Output: 14
Example 3:

Input: nums = [8]
Output: 0

Constraints:

1 <= nums.length <= 5000
1 <= nums[i] <= 104

Approach: check if nums[i] <= nums[i-1], meaning that the array is not strictly increasing, so therefore we will try to calculate the difference between them
and then add 1 to it to and then we will add that computed difference to final result


Time complexity: O(n), where n is the length of the array
Space complexity: O(1), we do not need to store any extra space for 
'''
def minOperations(nums):
	#base case: 
	if not nums: 
		return None
	if len(nums) == 1:
		return 0
	#difference between two values in the array 
	difference = 0
	#variable to count the minimum operations
	result = 0
	for i in range(1, len(nums)):
		#this part of the array is already increasing
		if nums[i-1] < nums[i]:
			continue
		difference = nums[i-1] - nums[i] + 1
		#adding the difference to the result to determine how many operations it would take 	
		result += difference
		#update the curernt value to make sure that the array is really increasing, this is 
		#good for the next pairs 
		nums[i] += difference
	return result


def main():
	print("TETSING Minimum Operations to Make the Array Increasing...")
	nums = [1,1,1]
	print(minOperations(nums))

	nums = [1,5,2,4,1]
	print(minOperations(nums))


	nums = [8]
	print(minOperations(nums))

	print("END OF TESTING...")



main()
