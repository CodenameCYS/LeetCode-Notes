'''
=== 309. Best Time to Buy and Sell Stock with Cooldown ===

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
    - You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    - After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
    Input: [1,2,3,0,2]
    Output: 3 
    Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''
import math
# === 4332ms && 572.8MB === #
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @lru_cache(None)
        def dp(i: int, have_stock: bool, bought_price: int) -> int:
            if i >= n:
                return 0 if not have_stock else -math.inf
            if not have_stock:
                return max(dp(i+1, True, prices[i]), dp(i+1, False, 0))
            else:
                if prices[i] > bought_price:
                    return max(dp(i+1, True, bought_price), prices[i]-bought_price + dp(i+2, False, 0))
                else:
                    return dp(i+1, True, bought_price)
                
        return dp(0, False, 0)