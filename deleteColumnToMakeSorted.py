#Problem 944. Delete Columns to Make Sorted

'''
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]]).

Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.

 

Example 1:

Input: A = ["cba","daf","ghi"]
Output: 1
Explanation: 
After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
Example 2:

Input: A = ["a","b"]
Output: 0
Explanation: D = {}
Example 3:

Input: A = ["zyx","wvu","tsr"]
Output: 3
Explanation: D = {0, 1, 2}
 

Constraints:

1 <= A.length <= 100
1 <= A[i].length <= 1000
'''
#Solution function: 
#Basic greedy approach, loop through the array to check for any column that are not sorted. The greedy part is to only account for
#any element that are not sorted
def minDeletionSize(A):
    #base case: 
    if not A: #no list not value
        return 0
    result = 0
    #loop through the outer column 
    for i in range(len(A[0])):
        prev = A[0][i]
        #loop through the inner column to compare it with the outer column
        for j in range(1, len(A)):
            if prev > A[j][i]:
                result += 1
                break
            else:
                prev = A[j][i]

    return result



#Main function to run the program:
def main():
    print("TESTING DELETING THE COLUMN TO MAKE SORTED...")
    input01 = ["cba","daf","ghi"]
    input02 = ["a","b"]
    input03 = ["zyx","wvu","tsr"]
    print(minDeletionSize(input01))
    print(minDeletionSize(input02))
    print(minDeletionSize(input03))
    print("END OF TESTING...")

main()