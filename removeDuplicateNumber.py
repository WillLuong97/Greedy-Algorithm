#Leetcode 316. Remove Duplicate Letters

#Problem statement: 

'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
Example 1:

Input: s = "cdadabcc"
Output: "adbc"
Example 2:

Input: s = "abcd"
Output: "abcd"
Example 3:

Input: s = "ecbacba"
Output: "eacb"
Example 4:

Input: s = "leetcode"
Output: "letcod"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''
# Algorithm: 
#We use a stack to keep track of the unique element from the string but we also built the stack with the idea that we will squeeze the element with the smallest 
#ascii representation to the head of the stack. 
# as we put element into the stack, we will give priority to the element that has smaller ascii value or the value to be pop cannot be repeated in the string anymore.
def removeDuplicateLetters(s):
    #base case: 
    if not s: 
        return ""

    #create a stack to store our answer
    stack = []
    #append the first element into the stack, this way we have an element in the stack to deal with 
    stack.append(s[0])
    #loop through the original string
    for i in range(len(s)):
        if s[i] not in stack:
            while stack and ord(stack[-1]) > ord(s[i]) and stack[-1] in s[i+1:]:
                stack.pop()
            stack.append(s[i])

    return "".join(stack)



#Driver code: 
def main():
    print("TESTING REMOVE DUPLICATE NUMBER...")
    input01 = "cdadabcc"
    input02 = "abcd"
    input03 = "ecbacba"
    input04 = "leetcode"
    print(removeDuplicateLetters(input01))
    print(removeDuplicateLetters(input02))
    print(removeDuplicateLetters(input03))
    print(removeDuplicateLetters(input04))
    print("END OF TESTING")
main()