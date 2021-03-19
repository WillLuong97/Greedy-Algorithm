#Problem 921. Minimum Add to Make Parentheses Valid
'''
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
 

Note:

S.length <= 1000
S only consists of '(' and ')' characters.


Approach: bruteforce + stack data structure 
we will loop through the parantheses array and at any point, only add the" (" into the stack and count the number of")"
- if the two open and closed parentheses can make a valid parentheses, the we will pop the "(" out of the stack and not count the ")"
 
Time complexity: O(n), the solution will need to look through all element in the array.
Space complexity: O(n), we need to maintain a stack data structure to store all the "(" 
'''
def minAddToMakeValid(S):
	#base case: 
	if not len(S):
		return 0
	stack = []
	#variable to count the number of closed parentheses: 
	closed_count = 0
	#loop through the string to find see the element
	for symbol in S:
		#add the parentheses into the stack
		if symbol == "(":
			stack.append(symbol)
		if symbol == ")":
			#check to see if we can make a valid string if the current stack has a "(" 
			if stack: 
				stack.pop()
			else: 
				closed_count += 1
	return len(stack) + closed_count
		

#Main function to run the test case: 
def main():
	print("TESTING MINIMUM ADD TO MAKE PARENTHESES VALID...")
	#test case: 
	print(minAddToMakeValid("())"))
	print(minAddToMakeValid("((("))
	print(minAddToMakeValid("()"))
	print(minAddToMakeValid("()))(("))

	print("END OF TESTING...")

main()
