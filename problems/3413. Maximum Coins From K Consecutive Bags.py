'''
=== 3413. Maximum Coins From K Consecutive Bags ===

There are an infinite amount of bags on a number line, one bag for each coordinate. Some of these bags contain coins.
You are given a 2D array coins, where coins[i] = [li, ri, ci] denotes that every bag from li to ri contains ci coins.
The segments that coins contain are non-overlapping.
You are also given an integer k.
Return the maximum amount of coins you can obtain by collecting k consecutive bags.

Example 1:
    Input: coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4
    Output: 10
    Explanation:
    Selecting bags at positions [3, 4, 5, 6] gives the maximum number of coins: 2 + 0 + 4 + 4 = 10.
Example 2:
    Input: coins = [[1,10,3]], k = 2
    Output: 6
    Explanation:
    Selecting bags at positions [1, 2] gives the maximum number of coins: 3 + 3 = 6.

Constraints:
    1. 1 <= coins.length <= 105
    2. 1 <= k <= 109
    3. coins[i] == [li, ri, ci]
    4. 1 <= li <= ri <= 109
    5. 1 <= ci <= 1000
    6. The given segments are non-overlapping.
'''
# === 855ms && 70.6MB === #
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        n = len(coins)
        coins = sorted(coins)
        # print(coins)
        
        cumsums = [0 for _ in range(n+1)]
        for i, (l, r, c) in enumerate(coins):
            cumsums[i+1] = cumsums[i] + (r-l+1) * c
        
        ans = 0
        for i, (l, r, c) in enumerate(coins):
            # start from l
            j = bisect.bisect_left(coins, [l+k, l+k, 0])
            if coins[j-1][1] < l+k:
                ans = max(ans, cumsums[j]-cumsums[i])
            else:
                ans = max(ans, cumsums[j-1]-cumsums[i] + (l+k - coins[j-1][0]) * coins[j-1][2])
            
            # end by r
            j = bisect.bisect_left(coins, [r-k+1, r-k+1, 0])
            if j > i:
                ans = max(ans, k * coins[i][2])
            elif j == 0 or coins[j-1][1] <= r-k:
                ans = max(ans, cumsums[i+1]-cumsums[j])
            else:
                ans = max(ans, cumsums[i+1]-cumsums[j] + (coins[j-1][1]-(r-k)) * coins[j-1][2])
        # print("=" * 10)
        return ans