#Leetcode 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
'''
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
Example 2:

Input: n = "82734"
Output: 8
Example 3:

Input: n = "27346209830709182346"
Output: 9
 

Constraints:

1 <= n.length <= 105
n consists of only digits.
n does not contain any leading zeros and represents a positive integer.
'''
def minPartitions(n):
    #base case: 
    if not n: 
        return None
    
    return max(n)
#Time complexity: O(n), we need to loop through the n-size array to find the largest digit
#Space complexity: O(1), we need to store an array with the size of n


#main function: 
def main():
    print("TESTING PARTITIONING INTO MINIMUM NUMBER OF DECI-BINARY NUMBERS...")
    n_1 = "32"
    n_2 = "82734"
    n_3 = "27346209830709182346"
    print(minPartitions(n_1))
    print(minPartitions(n_2))
    print(minPartitions(n_3))

    print("END OF TESTING...")
main()