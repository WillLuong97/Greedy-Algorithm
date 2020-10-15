#Leetcode 621. Task Scheduler

'''
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].

'''
def leastInterval(tasks, n):
    #base case: 
    if not tasks and not n: 
        return 0

    if not n: 
        return len(tasks)

    #create a dictionary to count how many times a task is executed
    taskDict = {}
    minTime = 0
    maxRepeatedTask = 0

    #initialize the dictionary with the element in the task list
    for i in range(len(tasks)):
        taskDict[tasks[i]] = taskDict.get(tasks[i], 0) + 1

    #count the element that appear the most in the dictionary
    maxRepeatedTask = max(taskDict.values())

    #calculate the min amount of time to execute same set of tasks
    #equation: maxReatedTask + (maxRepeatedTask - 1) * n - 1
    minExecuteTime = maxRepeatedTask + (maxRepeatedTask - 1) * n - 1    #this is just one set of repeated tasks

    #calculating how many tasks are repeated at the max
    task_with_same_repeated_times = list(taskDict.values()).count(maxRepeatedTask)
    minExecuteTime += task_with_same_repeated_times

    return max(minExecuteTime, len(tasks))


def main():
    print("TESTING TASK SCHEDULER...")
    tasks_01 = ["A","A","A","B","B","B"]
    n_01 = 2
    print(leastInterval(tasks_01, n_01))

    print("END OF TESTING...")
main()