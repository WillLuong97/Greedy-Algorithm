#Python3 implementaion to solve leetcode 406. Queue Reconstruction by Height

#Problem statement: 

'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

#Algorithm: 
#Sort the array based on the person height (descendingly)
#the k number can also be known as the index that it can be placed in the new queue
#add element into the index base on k into the new queue but we will give priority to those that are shorter to be placed in first. (Greedy)
def reconstructQueue(people):
    #base case: 
    if not people: 
        return [[]]
    #a result queue after reconstruction:
    result = []
    #sort the queue in a descendding order based on the person height
    people = sorted(people, key = lambda x: (-x[0], x[1])) #sort any array ascendingly
    #we will reconstruct the new queue
    for i in people: 
        result.insert(i[1], i)

    return result


#driver code to run the program 
def main():
    print("TESTING QUEUE HEIGHT RECONSTRUCTION...")
    test_array = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(reconstructQueue(test_array))
    print("END OF TESTING...")
main()