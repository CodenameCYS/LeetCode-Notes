'''
=== 2320. Count Number of Ways to Place Houses ===

There is a street with n * 2 plots, where there are n plots on each side of the street. The plots on each side are numbered from 1 to n. On each plot, a house can be placed.
Return the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street. Since the answer may be very large, return it modulo 109 + 7.
Note that if a house is placed on the ith plot on one side of the street, a house can also be placed on the ith plot on the other side of the street.

Example 1:
    Input: n = 1
    Output: 4
    Explanation: 
    Possible arrangements:
    1. All plots are empty.
    2. A house is placed on one side of the street.
    3. A house is placed on the other side of the street.
    4. Two houses are placed, one on each side of the street.
Example 2:
    Input: n = 2
    Output: 9
    Explanation: The 9 possible arrangements are shown in the diagram above.
 
Constraints:
    1. 1 <= n <= 104
'''
# === 2850ms && 473.8MB === #
class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(idx, pre):
            if idx >= n:
                return 1
            res = 0
            for i in range(4):
                if i & pre == 0:
                    res += dp(idx+1, i)
            return res % MOD
        
        return dp(0, 0)
        