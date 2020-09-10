#Python implementation of the Job Sequencing problem using Greedy Algorithm approach 

#Problem statement: 

'''
Given an array ofjobs where every job has a deadline and associated with profit if the job is finished before the deadlines. 
It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1. Write 
a function that would return the maximum total of profits if only one job can be scheduled at a time. 
Example: 
Job:		A	B	C	D	E
Deadline:	2	1	2	1	3
Profit		100	19	27	25	15
'''

#Solution: through greedy algorithm: 
'''
1. Sort all jobs in the decreasing order of profit
2. Iterate on jobs in decreasing order of profit. For each job, do the following: 
a. Find a time slot i, such that slot is empty and i < deadline and i is greatest. Put the job in the this slot and mark this slot filled
b. if no such i exist, then ignore the job
'''

def jobScheduling(arr, numOfJob):
	#base case: the array of jobs is empty
	if not arr: 
		return None	
	
	n = len(arr)
	#sort the array in the descending order of the profit
	for i in range(n):
		for j in range(n - 1 - i):
			if arr[j][2] < arr[j + 1][2]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	#create an array that stores the free time slot allocated to the number of jobs that we are going to work for
	timeSlot = [False] * numOfJob

	#final result string: 
	result = 0

	for i in range(n):
		for j in range(min(numOfJob - 1, arr[i][1] - 1), -1, -1):
			if timeSlot[j] == False:
				timeSlot[j] = True
				result += int(arr[i][2])
				break

	return result




#main function to run and execute the implementation: 
def main(): 
	print("TESTING JOB SEQUENCING...")
	test_array = [['a', 2, 100], # Job Array 
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]]
	test_num = 3
	print(jobScheduling(test_array, test_num))
	print("END OF TESTING...")
main()
