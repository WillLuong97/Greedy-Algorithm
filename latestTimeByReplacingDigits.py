#Problem 1736. Latest Time by Replacing Hidden Digits


'''
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

 

Example 1:

Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:

Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"
 

Constraints:

time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.
'''
def maximumTime(time):
	# first digit: if second_digit >= 4: [0, 1], else: [0, 2]
	# second digit: if first_digit == 2: [0, 3], else: [0, 9]
	# third digit: always [0, 5]
	# fourth digit: always [0, 9]
	time = list(time)
	#first digit
	if time[0] == '?' and (time[1] == '?' or time[1] < '4'):
		time[0] = '2'
	elif time[0] == '?':
		time[0] = '1'
	#second digit
	if time[1] == '?' and time[0] == '2':
		time[1] = '3'
	elif time[1] == '?':
		time[1] = '9'

	#third digit:
	if time[3] == '?':
		time[3] = '5'
	if time[4] == '?':
		time[4] = '9'

	return ''.join(time)

		
	


	




#Main function to run the test cases:
def main():
	print("TESTING LASTEST TIME BY REPLACING DIGITS...")
	time_1 = "2?:?0"
	time_2 = "0?:3?"
	time_3 = "1?:22"
	print(maximumTime(time_1))
	print(maximumTime(time_2))
	print(maximumTime(time_3))


	print("END OF TESTING...")

main()
