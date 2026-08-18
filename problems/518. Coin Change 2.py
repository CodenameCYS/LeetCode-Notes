'''
=== 518. Coin Change 2 ===

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:
    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
Example 2:
    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:
    Input: amount = 10, coins = [10] 
    Output: 1
 
Note:
    You can assume that
    1. 0 <= amount <= 5000
    2. 1 <= coin <= 5000
    3. the number of coins is less than 500
    4. the answer is guaranteed to fit into signed 32-bit integer
'''
# === 208ms(51.67%) && 22.6MB(16.67%) === #
class Solution:
    def my_change(self, amount, coins, n):
        if (amount, n) in self.cache.keys():
            return self.cache[(amount, n)]
        if n == 1:
            ans = 1 if amount % coins[0] == 0 else 0
            self.cache[(amount, n)] = ans
            return ans
        if amount == 0:
            return 1
        ans = self.my_change(amount, coins[1:], n-1)
        if amount >= coins[0]:
            ans += self.my_change(amount-coins[0], coins, n)
        self.cache[(amount, n)] = ans
        return ans
        
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if coins == []:
            return 0
        coins = sorted(coins, reverse=True)
        self.cache = {}
        return self.my_change(amount, coins, len(coins))