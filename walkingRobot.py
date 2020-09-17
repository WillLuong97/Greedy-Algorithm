#python3 program to solve the leetcode problem of Water Bottles 
#Problem statement
'''
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.

Example 1
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Example 2
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.

Example 3:
Input: numBottles = 5, numExchange = 5
Output: 6

Example 4:
Input: numBottles = 2, numExchange = 3
Output: 2
'''
def numWaterBottles(numBottle, numExchange):
    #base case:
    if not numBottle: 
        return None
    
    total = 0
    empty = 0

    while numBottle: 
        #drink all given bottle to us
        total += numBottle

        #find out how many bottle we can trade in and how many would remain
        total, empty = divmod(empty + numBottle, numExchange)
    return total




# #Main function to execute the program 
# def main():
#     print("TESTING WATER BOTTLE...")
#     test_val_3 = 15
#     test_exchange_3 = 4

#     print()
#     print(numWaterBottles(test_val_3, test_exchange_3))
#     print("END OF TESTING...")

# main() 


