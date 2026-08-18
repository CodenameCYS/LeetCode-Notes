'''
=== 2328. Number of Increasing Paths in a Grid ===

You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.
Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.
Two paths are considered different if they do not have exactly the same sequence of visited cells.

Example 1:
    Input: grid = [[1,1],[3,4]]
    Output: 8
    Explanation: The strictly increasing paths are:
    - Paths with length 1: [1], [1], [3], [4].
    - Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
    - Paths with length 3: [1 -> 3 -> 4].
    The total number of paths is 4 + 3 + 1 = 8.
Example 2:
    Input: grid = [[1],[2]]
    Output: 3
    Explanation: The strictly increasing paths are:
    - Paths with length 1: [1], [2].
    - Paths with length 2: [1 -> 2].
    The total number of paths is 2 + 1 = 3.
    
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 1000
    4. 1 <= m * n <= 105
    5. 1 <= grid[i][j] <= 105
'''
# === 3547ms && 107.4MB === #
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n, m = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dp(i, j):
            res = 1
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] > grid[i][j]:
                    res += dp(x, y)
            return res % MOD
        
        s = sum(dp(i, j) for i in range(n) for j in range(m))
        return s % MOD