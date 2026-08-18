'''
=== 123. Best Time to Buy and Sell Stock III ===

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
    Input: [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
                 Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:
    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                 Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                 engaging multiple transactions at the same time. You must sell before buying again.
Example 3:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
# === 376ms && 58MB === #
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @lru_cache(None)
        def dp(idx, k, bought):
            if k == 0 and bought == -1:
                return 0
            if idx >= n:
                return 0
            if bought == -1:
                while idx < n-1 and prices[idx+1] <= prices[idx]:
                    idx += 1
                if idx < n-1:
                    return max(dp(idx+1, k-1, prices[idx]), dp(idx+1, k, -1))
                else:
                    return 0
            else:
                while idx < n and prices[idx] <= bought:
                    idx += 1
                if idx < n:
                    return max(prices[idx] - bought + dp(idx+1, k, -1), dp(idx+1, k, bought))
                else:
                    return 0
            
        return dp(0, 2, -1)