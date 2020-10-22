#659. Split Array into Consecutive Subsequences implementation using Greedy approach

#Problem statement: 
'''
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.
Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
Example 3:

Input: [1,2,3,4,4,5]
Output: False
 

Constraints:

1 <= nums.length <= 10000
 
'''
import collections
#Greedy approach: 
def isPossible(nums):
    #base case: 
    if not nums: 
        return False

    #Dictionary to store the element frequency
    counter = collections.Counter(nums)
    #dictionary to store the subarray that can be constructed
    groups = collections.defaultdict(int)

    #loop through the array:
    for num in nums: 
        if counter[num]:
            #append the num ino a current groups if its final element is consecutively before it: 
            if groups[num - 1]:
                groups[num] += 1
                groups[num-1] -= 1

            #create a new group if there is no group that it can joiin
            elif counter[num+1] and counter[num+2]:
                counter[num+1] -= 1
                counter[num+2] -= 1
                groups[num+2] += 1

            else: 
                return False

            counter[num] -= 1

    return True

#Time complexity: O(N) where n is the length of the array, the algorithm will look at every element in the array to count its frequency as well as finding the the approprate subarray to pass them in
#Space complexity: o(n), the dictionary would have to store all element in the array

            





    

#Main function to run the program
def main():
    print("TESTING SPLIT ARRAY INTO CONSECUTVE SUBARRAY...")
    test_nums_1 = [1,2,3,3,4,5]
    test_nums_2 = [1,2,3,3,4,4,5,5]
    test_nums_3 = [1,2,3,4,4,5]
    print(isPossible(test_nums_1))
    print(isPossible(test_nums_2))
    print(isPossible(test_nums_3))

    print("END OF TESTING....")

main()