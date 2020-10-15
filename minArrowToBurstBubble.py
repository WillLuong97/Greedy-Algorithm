#Python3 implementation of Leetcode 452. Minimum Number of Arrows to Burst Balloons

#Problem statement: 

'''
There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Example 4:

Input: points = [[1,2]]
Output: 1
Example 5:

Input: points = [[2,3],[2,3]]
Output: 1
'''
#Greedy algorithm, we sort the array and then reduce the amount of arrows based on any overlapping intervals
#Function to find the number of arrow to burst the bubble
def findMinArrowShots(points):
    #base case: if no balloon, then return nothing back
    if not points: 
        return None

    #start and end point variables: 
    starting_point = 0
    ending_point = 1
    #sorts the list of coordinate based on its
    points.sort(key = lambda p: (p[starting_point], p[ending_point]))

    #initalize the max number of arrow that can be used to burst the bubble, without an overlapping intervals,
    #then the number of arrow shot would be the same lenght as points
    arrow_shot = len(points)

    #overlapping area that can take out multple balloon at the same time
    areaOfCoverage = points[0]

    #loop through the list of arrow to determine which to burst
    for balloon in points[1:]:
        #determine if there is an overlap
        if(areaOfCoverage[ending_point] >= balloon[starting_point]): #then we will merge these together
            areaOfCoverage = [max(areaOfCoverage[starting_point], balloon[starting_point]), min(areaOfCoverage[ending_point], balloon[ending_point])]
            arrow_shot -= 1
        else: 
            #if not then the bursting area is only the current balloon area
            areaOfCoverage = balloon

    return arrow_shot


#Solution using greedy algorithm: 
def findMinArrowShots_GREEDY(points):
    pass




#driver code to test the program
def main():
    print("TESTING MINIMUM ARROW TO BURST A BUBBLE...")

    test_points_01 = [[10,16],[2,8],[1,6],[7,12]]
    test_points_02 = [[1,2],[3,4],[5,6],[7,8]]
    test_points_03 = [[1,2],[2,3],[3,4],[4,5]]
    test_point_04 = [[1,2]]
    test_point_05 = [[2,3],[2,3]]
    print(findMinArrowShots(test_points_01))
    print(findMinArrowShots(test_points_02))
    print(findMinArrowShots(test_points_03))
    print(findMinArrowShots(test_point_04))
    print(findMinArrowShots(test_point_05))
    print("END OF TESTING...")
main()
    