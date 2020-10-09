#LEETCODE 435. Non-overlapping Intervals

#Problem statement

'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

'''
#function to remove non overlapping intervals (DOES NOT WORK IF THE END POINT OF THE OVERLAPPING ELEMENT IS NOT REPEATED)
# def eraseOverlapIntervals(intervals):
#     #base case: 
#     if not intervals:
#         return 0
#     #result counter
#     counter = 0
#     #dictionary to store the starting point and ending point of the intervals
#     coordinateDict = {}
#     #endpoint : startpoint hashmap
#     coordinateDict[intervals[0][1]] = intervals[0][0]
#     #loop through the intervals list
#     for i in range(1, len(intervals)):
#         #extract the endpoints and startpoints from the intervals list
#         endPoint = intervals[i][1]  
#         startPoint = intervals[i][0]
#         if endPoint in coordinateDict:
#             if startPoint <= coordinateDict[endPoint]:
#                 counter += 1
        
#         coordinateDict[endPoint] = startPoint

#     return counter

#sorted the intervals list and use 2 pointer.
#there will be an overlapping intervals if previous interval enpoint is lesser than the next interval starting point. 
def eraseOverlapIntervals(intervals):
    #base case: 
    if not intervals:
        return 0

    #two pointers: 
    i = 0
    j = 1
    counter = 1
    #sort the list of interval
    sortedInterval = sorted(intervals,key=lambda x : x[1])
    
    while i < len(sortedInterval) and j < len(sortedInterval):
        if sortedInterval[i][1] <= sortedInterval[j][0]:
            counter += 1
            i = j
            j += 1

        else:
            j+= 1

    return len(intervals) - counter
            

#main function to test the program 
def main():
    print("TESTING NON-OVERLAPING INTERVALS...")
    print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    
    print(eraseOverlapIntervals([[1,2],[2,3]]))
    print('END OF TESTING...')
main()