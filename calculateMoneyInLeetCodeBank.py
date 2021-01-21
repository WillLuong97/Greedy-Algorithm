#Problem 1716. Calculate Money in Leetcode Bank

'''
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 

Constraints:

1 <= n <= 1000

'''
def totalMoney(n):
	#base case:
	if not n:
		return 0
	result = extra_dollar = 0
	#loop through the n days and calculate the money saved in each days
	for i in range(n):
		if i % 7 == 0:
			extra_dollar += 1
		result += extra_dollar + i % 7

	return result
#Time complexity: 0(n), the algorithm will run through all the elements to calculate the sum of money saved
#Space complexity: O(1)



#Main function to run the test cases: 
def main():
	print("TESTING CALCULATE MONEY IN LEETCODE BANK...")
	n = 4
	n_2 = 10
	n_3 = 20
	#Test cases: 
	print(totalMoney(n))
	print(totalMoney(n_2))
	print(totalMoney(n_3))
	print("END OF TESTING...")

main()
