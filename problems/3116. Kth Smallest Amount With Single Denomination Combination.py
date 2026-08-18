'''
=== 3116. Kth Smallest Amount With Single Denomination Combination ===

You are given an integer array coins representing coins of different denominations and an integer k.
You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.
Return the kth smallest amount that can be made using these coins.

Example 1:
    Input: coins = [3,6,9], k = 3
    Output:  9
    Explanation: The given coins can make the following amounts:
    Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
    Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
    Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
    All of the coins combined produce: 3, 6, 9, 12, 15, etc.
Example 2:
    Input: coins = [5,2], k = 7
    Output: 12 
    Explanation: The given coins can make the following amounts:
    Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
    Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
    All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.

Constraints:
    1. 1 <= coins.length <= 15
    2. 1 <= coins[i] <= 25
    3. 1 <= k <= 2 * 109
    4. coins contains pairwise distinct integers.
'''
# === 77ms && 17.2MB === #
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        if 1 in coins:
            return k
        
        def filter_coins(coins):
            coins = sorted(coins)
            fcoins = []
            for c in coins:
                if any(c % x == 0 for x in fcoins):
                    continue
                fcoins.append(c)
            return coins
        
        coins = filter_coins(coins)
        n = len(coins)
        lcms = defaultdict(list)
        
        def dfs(idx, used, _lcm):
            nonlocal lcms
            if idx >= n:
                return
            dfs(idx+1, used, _lcm)
            _lcm = lcm(_lcm, coins[idx])
            lcms[used+1].append(_lcm)
            dfs(idx+1, used+1, _lcm)
            return
        
        dfs(0, 0, 1)
        
        def count(x):
            ans = 0
            flag = 1
            for i in range(1, n+1):
                for v in lcms[i]:
                    ans += flag * (x // v)
                flag = -flag
            return ans
        
        l, r = 0, coins[-1] * k + 1
        while r-l > 1:
            m = (l+r) // 2
            if count(m) >= k:
                r = m
            else:
                l = m
        return r