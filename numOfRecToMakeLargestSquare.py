#Problem 1725. Number Of Rectangles That Can Form The Largest Square

'''
You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.

 

Example 1:

Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
Output: 3
Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.
Example 2:

Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
Output: 3
 

Constraints:

1 <= rectangles.length <= 1000
rectangles[i].length == 2
1 <= li, wi <= 109
li != wi
'''
from collections import Counter
def countGoodRectangles(rec):
	#bsae case: 
	if not rec:
		return []
	squares = []
	#loop through each rectangle to find the k 
	for rectagle in rec:
		squares.append(min(rectagle))
	
	freq_of_each_dimension = Counter(squares)
	return freq_of_each_dimension[max(squares)]
		
#Time complexity: O(n), we have to loop through the number of rectangles to find the k length.
#Space complexity: O(n), we have to store the the number of squares created



#Main function to run the test cases: 
def main():
	print("TESTING  Number Of Rectangles That Can Form The Largest Square")
	rec_1 = [[5,8],[3,9],[5,12],[16,5]]
	rec_2 =[[2,3],[3,7],[4,3],[3,7]]
	print(countGoodRectangles(rec_1))
	print(countGoodRectangles(rec_2))

	print("END OF TESTING...")


main()


