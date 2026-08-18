'''
=== 3665. Twisted Mirror Path Count ===

Given an m x n binary grid grid where:
    - grid[i][j] == 0 represents an empty cell, and
    - grid[i][j] == 1 represents a mirror.
A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:
    - If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
    - If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.
    - If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.
Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).
Since the answer may be very large, return it modulo 109 + 7.
Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.

Example 1:
    Input: grid = [[0,1,0],[0,0,1],[1,0,0]]
    Output: 5
    Explanation:
    Number	Full Path
    1	(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
    2	(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
    3	(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
    4	(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
    5	(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
    [M] indicates the robot attempted to enter a mirror cell and instead reflected.
Example 2:
    Input: grid = [[0,0],[0,0]]
    Output: 2
    Explanation:
    Number	Full Path
    1	(0, 0) → (0, 1) → (1, 1)
    2	(0, 0) → (1, 0) → (1, 1)
Example 3:
    Input: grid = [[0,1,1],[1,1,0]]
    Output: 1
    Explanation:
    Number	Full Path
    1	(0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
    (0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1) goes out of bounds, so it is invalid.

Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 2 <= m, n <= 500
    4. grid[i][j] is either 0 or 1.
    5. grid[0][0] == grid[m - 1][n - 1] == 0
'''
MOD = 10**9+7
# === 2733ms && 306.37MB === #
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        DIRECTION = {0: (1, 0), 1: (0, 1)}

        @lru_cache(None)
        def dp(i, j, direction):
            if i == n-1 and j == m-1:
                return 1
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            if grid[i][j] == 0:
                return (dp(i+1, j, 0) + dp(i, j+1, 1)) % MOD
            while 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
                direction = 1-direction
                dx, dy = DIRECTION[direction]
                i, j = i+dx, j+dy
            return dp(i, j, direction) % MOD

        return dp(0, 0, 0)
