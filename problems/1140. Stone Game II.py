'''
=== 1140. Stone Game II ===

Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

Example 1:
    Input: piles = [2,7,9,4,4]
    Output: 10
    Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
 
Constraints:
    1. 1 <= piles.length <= 100
    2. 1 <= piles[i] <= 10 ^ 4
'''
# === 84ms(72.31%) && 14.5MB(58.15%) === #
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        @lru_cache(None)
        def dp(st, M):
            ans = 0
            tot = sum(piles[st:])
            for i in range(1, 2*M+1):
                ed = st + i
                if ed > n:
                    break
                ans = max(ans, tot - dp(ed, max(M, i)))
            return ans
        
        return dp(0, 1)