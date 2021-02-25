#1758. Minimum Changes To Make Alternating Binary String
'''
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.
'''
def minOperations(s):
	#helper method to check how many operations it would take if we were going to start out
	#alternating the string value with either 0 or 1
	def checkAlternation(starter):
		#count the number of operations:
		count = 0 
		for current_bit in s: 
			if starter != current_bit:
				count += 1
			#alternate the starter value to be the opposite value
			starter = "1" if starter == "0" else "0"
		
		return count
		
	return min(checkAlternation("1"), checkAlternation("0"))
 
#Time complexity: O(n), n is the number of all element in the current string, we have to look through all of them to check for the alternation
#Space complexity: O(1), we dont have to store any extra space except of the count variable. 
			

#Main function to run the test case: 
def main():
	print("TESTING MINIMUM CHANGES TO MAKE ALTERNATING BINARY STRING...")
	s = "0100"
	print(minOperations(s))
	s = "10"
	print(minOperations(s))
	s = "1111"
	print(minOperations(s))
	print("END OF TESTING...")
main()




