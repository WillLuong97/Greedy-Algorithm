#Problem statement: 

'''
You are given n activities with their start and finish times.
Select the maximum number of activities that can be performed by a single person 
assuming that a person can only work on a single activity at a time.
'''


#Example 1: Consider the following 3 activities sorted by finish time. 
#   start[] = {10, 12, 20}, finish[] = {20, 25, 30}
# A person can perform at most two activities. The 
# maximum set of activities that can be executed 
# is {0, 2} [ These are indexes in start[] and 
# finish[] ]


#Algorithm: 
# 1. Sort the activities according to their finishing time
# 2. Select the first activity from the sorted array and print it
# 3. Do the following for remaining activities in the sorted array: 
#      If the start time of this activity is greater than or equal to the finish time of previously selected activity 
#     then select this activity and print it


#This python implementation assume that the activites are already sorted by its finiishing time
def findMaxActivities(start, finish):
    n = len(finish)

    #The first activity is always selected becasue it would take the least amount of time
    i = 0 
    print(i)
    res_array = []
    #Loop through the finishing time array: 
    for j in range(n):
        #If this activity has the start time greater than or equal to the finish time of previously selected activity, then selec it. 
        if start[j] >= finish[i]:
            print(j)
            i = j

#Driver code: 
s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 

findMaxActivities(s, f)