#Python program to implement the Leetcode medium #55 Jump Game

#Importing enum: 
from enum import Enum

'''
Problem Statement: 
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''



#Solution #1: Backtracking

'''
This is an inefficient solution where we try every single jump pattern that takes us from the first position to the last. 
We start from the first position and jump to every index that is reacheable. We repeat the process until the last index is reached. 
When stuck, backtrack 
'''
def canJump_BACKTRACKING(nums):
    return canJumpFromtThisPosition(0, nums)


#Function to check if the current position int the array can be jumped to the last element in the array
def canJumpFromtThisPosition(position, nums):
    #base case: nums and position are both null
    # if not position or not nums:
    #     return False
    #the position is currently already at the last element in the array
    if position == len(nums) - 1:
        return True
    #to calculate the furthest a particular position in the array can jump to
    furthestJump = min(position + nums[position], len(nums) - 1)
    nextPosition = position + 1
    for i in range(nextPosition, furthestJump + 1):
        if(canJumpFromtThisPosition(i, nums)):
            return True

    return False

#Time complexity: O(2^n). There are 2^n (Upper Bound) ways of jumping from the first position to the last, where n is the length of the array nums. We get this recursively
#Space complexity: O(n). Recursion requires additional memory for the stack frames.


# Solution 2:  Greedy approach, instead of starting out from the beginning, we can try to start out from the ending index. 
#From the last index, we will go backward along the array and as we go through them, we will check to see if the current element can jump to the last index,
#store them and move on to the next. Then, you will check to see if the next element can be jumped to the previously stored element in the array [Because the previously stored index can be jumped to the last element, so if you jump to the element, you can jump the last index]
def canJump_GREEDY(nums):
    if not nums: 
        return False

    lastGoodIndexPosition = 0
    #going to the array backward and start out from the last index: 
    for i in range(len(nums) - 1, -1, -1):
        if(i + nums[i] >= lastGoodIndexPosition):
            lastGoodIndexPosition = i
    
    return lastGoodIndexPosition == 0



#Main function to test the program
def main():
    print("Testing Jump Game...")
    nums = [2,3,1,1,4]
    nums02 = [3,2,1,0,4]


    print(canJump_GREEDY(nums))
    print(canJump_GREEDY(nums02))
    print("")
    print("Testing Jump Game (BACKTRACKING)...")
    print(canJump_BACKTRACKING(nums))
    print(canJump_BACKTRACKING(nums02))
    print("")
    print("Testing Jump Game (TOP-DOWN)...")
    print(canJump_BACKTRACKING(nums))
    print(canJump_BACKTRACKING(nums02))


main()