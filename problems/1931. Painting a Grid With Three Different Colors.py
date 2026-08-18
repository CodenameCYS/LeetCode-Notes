'''
=== 1931. Painting a Grid With Three Different Colors ===

You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.
Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

Example 1:
    Input: m = 1, n = 1
    Output: 3
    Explanation: The three possible colorings are shown in the image above.
Example 2:
    Input: m = 1, n = 2
    Output: 6
    Explanation: The six possible colorings are shown in the image above.
Example 3:
    Input: m = 5, n = 5
    Output: 580986
 
Constraints:
    1. 1 <= m <= 5
    2. 1 <= n <= 1000
'''
# === 1092ms && 35.5MB === #
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9+7
        nxt = {"init": [s for s in product([0,1,2], repeat=m) if all(s[i] != s[i+1] for i in range(m-1))]}
        for s in nxt["init"]:
            nxt[s] = [t for t in nxt["init"] if all(s[i] != t[i] for i in range(m))]
        
        @lru_cache(None)
        def dp(i, status):
            if i == n:
                return 1
            res = 0
            for s in nxt[status]:
                res = res + dp(i+1, s)
            return res % MOD
        
        return dp(0, "init")
                
            
        