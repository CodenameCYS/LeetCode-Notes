'''
=== 2435. Paths in Matrix Whose Sum Is Divisible by K ===

You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.
Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
    Output: 2
    Explanation: There are two paths where the sum of the elements on the path is divisible by k.
    The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
    The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.
Example 2:
    Input: grid = [[0,0]], k = 5
    Output: 1
    Explanation: The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.
Example 3:
    Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
    Output: 10
    Explanation: Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 5 * 104
    4. 1 <= m * n <= 5 * 104
    5. 0 <= grid[i][j] <= 100
    6. 1 <= k <= 50
'''
# === 8647ms && 94MB === #
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        
        n, m = len(grid), len(grid[0])
        dp = [[[0 for _ in range(k)] for _ in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(n):
            for j in range(m):
                for mod in range(k):
                    if i-1 >= 0:
                        dp[i][j][mod] = (dp[i][j][mod] + dp[i-1][j][(mod-grid[i][j]) % k]) % MOD
                    if j-1 >= 0:
                        dp[i][j][mod] = (dp[i][j][mod] + dp[i][j-1][(mod-grid[i][j]) % k]) % MOD
        return dp[n-1][m-1][0]
        
        # @lru_cache(None)
        # def dp(i, j, mod):
        #     if i == n-1 and j == m-1:
        #         return 1 if (mod + grid[i][j]) % k == 0 else 0
        #     elif i >= n or j >= m:
        #         return 0
        #     mod = (mod + grid[i][j]) % k
        #     return (dp(i+1, j, mod) + dp(i, j+1, mod)) % MOD
        # return dp(0, 0, 0)