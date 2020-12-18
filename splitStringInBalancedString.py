#Leetcode 1221. Split a String in Balanced Strings

'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
Constraints:
1 <= s.length <= 1000
s[i] = 'L' or 'R'
'''
def balancedStringSplit(s):
    numOfL = 0
    numOfR = 0
    result = 0
    #loop through the string to count the amount of balanced substring that we can make 
    for i in s:
        if i == 'R':
            numOfR += 1

        if i == 'L':
            numOfL += 1

        if numOfL == numOfR:
            result += 1
            numOfL = 0
            numOfR = 0

    return result

#time complexity: O(n), we have to loop through the entire string s to count the number of l and r
#space complexity: O(1), constant space 

#main function to test the test cases: 
def main():
    print("TESTING SPLIT STRING BALANCED STRING...")
    #test cases: 
    s_01 = "RLRRLLRLRL"
    s_02 = "RLLLLRRRLR"
    s_03 = "LLLLRRRR"
    s_04 = "RLRRRLLRLL"

    print(balancedStringSplit(s_01))
    print(balancedStringSplit(s_02))
    print(balancedStringSplit(s_03))
    print(balancedStringSplit(s_04))
    
    print("END OF TESTING...")

main()