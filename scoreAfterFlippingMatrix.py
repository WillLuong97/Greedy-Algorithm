#Problem 861. Score After Flipping Matrix

'''
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 
Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.

Go through the 2 matrix and at each row, the 

The number at the ith position will determin the value of 2^i, to convert a binary number into a decimal number, for example, a number like 1001, we would do it like this: 1 * 2^3 + 0*2^2 + 0*2^1 + 1*2^0 

to create the highest sum we, ideally want to add the biggest number together and this is where the greedy algorithm would come into play, we will only want to pick the highest decimal
to create the highest sum, therefore, to create the highest decimal number we will have to toggle to a 1s on the left-most column of the matrix, because the left most column would have the highest 2^i value.

The idea here is to make greedy algorithm to put 
'''
def matrixScore(A):
	#base caes: 
	if not len(A):
		return None
	row = len(A)
	col = len(A[0])
	result = 0
	#loop through the matrix in a col and row manner
	for c in range(col):
		column = 0
		for r in range(row):
			column += A[r][c] ^ A[r][0]
		result += max(column, row - column) * 2 ** (col - 1 - c)
	
	return result
#Main function to run the test case: 
def main():
	print("TESTING SCORE AFTER FLIPPING MATRIX...")
	A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
	print(matrixScore(A))
		
	print("END OF TESTING...")

main()
