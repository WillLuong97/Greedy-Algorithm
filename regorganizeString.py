#Leetcode 767. Reorganize String

'''
Problem statement: 
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

'''
import heapq
#Sort and extends method: linear search
def reorganizeString(S):
    #base case: 
    if not S: 
        return None
    N = len(S)
    result = [None] * N
    new_string = []
    #sort the array based on the amount of times that they have
    for word, frequency in sorted((S.count(x), x) for x in set(S)):
        #base case: 
        if word > (N+1)/2:
            return ""
        #append the character with the most frequency into the new string
        new_string.extend(word*frequency)

    #interleave the contents into the array
    result[::2], result[1::2] = new_string[N//2:], new_string[:N//2]

    return "".join(result)
#time complexity: O(n)
#space complexity:O(n)


#Greedy and Heap approach: 
def reorganizeString_GREEDY_HEAP(S):
    #base case: 
    if not S: 
        return None

    #create a queue that store all the character from the string into
    #based on its frequency
    queue = [(-S.count(x), x) for x in set(S)]
    heapq.heapify(queue)
    #base case: if the frequency of the charater is greater than half of the array then, return "" because it is impossible to produce an acurate answer
    if any(-freq > (len(S)+1)/2 for freq, word in queue):
        return ""

    answer = []
    while len(queue) >= 2:
        #Pop out the current two most repeated elemenet from the array
        freq_1, word_1 = heapq.heappop(queue)
        freq_2, word_2 = heapq.heappop(queue)

        answer.extend([word_1, word_2])
        if freq_1+1:
            heapq.heappush(queue, (freq_1+1, word_1))    
        if freq_2+1: 
            heapq.heappush(queue, (freq_2+1, word_2))

    return "".join(answer) + (queue[0][1] if queue else "")

#main function to run the program
def main():
    print("TESTING Reorganzing A String...")
    S_1 = "aab"
    S_2 = "aaab"

    # print(reorganizeString(S_1))
    # print(reorganizeString(S_2))
    print(reorganizeString_GREEDY_HEAP(S_1))
    print(reorganizeString_GREEDY_HEAP(S_2))
    print("END OF TESTING...")
main()