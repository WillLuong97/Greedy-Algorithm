#Problem 763. Partition Labels
'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

'''
def partitionLabels(S):
	#base case: 
	if not S: 
		return [0]

	result = []
	#the dictionary that store the characters and its final index in the string. 
	last = {c: i  for i, c in enumerate(S)} 
	anchor = j = 0	#keep track of the final index that the char appear in the string. 
	#loop through the string to construct the substring: 
	for index, char in enumerate(S):
		j = max(j, last[char])
		#we have reached the substring length, all chars have appeared in her enough time. 
		if index == j: 
			result.append(index - anchor + 1)
			anchor = index + 1
				
	return result

#Time complexity: O(n), where n being the length of the stirng, because the algorithm has to run through every element in the string.
#Space complexity: O(1), to keep data structure last of not more than 26 characters. 			


#main function to run the test cases: 
def main():
    print("TESTING PARTITION LABEL...")
    S = "ababcbacadefegdehijhklij"
    print(partitionLabels(S))

    print("END OF TESTING...")
main()
