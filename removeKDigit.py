#Python3 program to solve Leetcode 402.Remove K Digits 

#Problem statement: 

'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''
#Greedy approach: we only take out the smallest elemt from the current iteration and add it into the stack and 
#formulate the result string from there. 

#Time complexity: O(n) we have to go through every element in the string. 
#space complexity: O(n) - worst case - best case would be O(1) some element from the final string would not be included in the stack
def removeKdigits(nums, k):
    #base case: 
    if not nums: 
        return None
    
    if len(nums) < k: 
        return None

    if k == 0:
        return nums

    #create a stack structure that will ideally store all the smallest element in the string 
    result = []
    #loop through the string and add each element into the stack
    for i in nums: 
        #if k still has digit for us to take out of the string and the stack still has element and 
        #the current element in the stack is greater than the element taken out from the string
        #then replace it from the stack.
        while(k and result and result[-1] > i):
            result.pop()
            k -= 1
        result.append(i)

    #if the sting traversal has been finished but k still has element
    while k:
        result.pop()
        k -= 1
    return "".join(result).lstrip('0') or '0'
    

#main function to run the code:
def main():
    print("TESTING REMOVE K INTEGER...")
    test_string_1= "1432219"
    test_k_1 = 3
    test_string_2 = "10200"
    test_k_2 = 1
    test_string_3 = "10"
    test_k_3 = 2
    test_string_4 = "112"
    test_k_4 = 1
    #Testing the value: 
    print(removeKdigits(test_string_1, test_k_1))
    print(removeKdigits(test_string_2, test_k_2))
    print(removeKdigits(test_string_3, test_k_3))
    print(removeKdigits(test_string_4, test_k_4))



    print("END OF TESTING...")

main()