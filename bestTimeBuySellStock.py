#Problem 714. Best Time to Buy and Sell Stock with Transaction Fee

'''
Problem statement: 
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
'''
#Function to solve the problem: 
#DP+Greedy approach
def maxProfit(prices, fee):
    #base case: no stock, no buying
    if not prices:
        return None
    #variable to store the profits from buying and selling
    actualProfit = 0 #actual profit from buying a certain stock
    projectProfit = -prices[0]#profit from selling a certain stock

    #loop through the array of stock prices to perform the transactions
    for i in range(1, len(prices)):
        actualProfit = max(actualProfit, projectProfit + prices[i] - fee)
        projectProfit = max(projectProfit, actualProfit - prices[i])

    return actualProfit
#Time complexity: O(N), the algorithm will still need to go through the entire array to analyzes all stock prices
#Space complexity: O(1) we just need space for "actualProfit" and  "projectProfit"

#Main function to run the solution
def main():
    print("TESTING BEST TIME TO BUY AND SELL STOCK WITH TRANSACTION FEES...")
    test_input = [1, 3, 2, 8, 4, 9]
    test_price = 2
    print(maxProfit(test_input, test_price))
    print("END OF TESTING...")
main()