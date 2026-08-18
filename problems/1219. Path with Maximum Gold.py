'''
=== 1219. Path with Maximum Gold ===

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
Return the maximum amount of gold you can collect under the conditions:
    - Every time you are located in a cell you will collect all the gold in that cell.
    - From your position, you can walk one step to the left, right, up, or down.
    - You can't visit the same cell more than once.
    - Never visit a cell with 0 gold.
    - You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:
    Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
    Output: 24
    Explanation:
    [[0,6,0],
    [5,8,7],
    [0,9,0]]
    Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:
    Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    Output: 28
    Explanation:
    [[1,0,7],
    [2,0,6],
    [3,4,5],
    [0,3,0],
    [9,0,20]]
    Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 15
    4. 0 <= grid[i][j] <= 100
    5. There are at most 25 cells containing gold.
'''
# === 1012ms(98.10%) && 14MB(93.41%) === #
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n:
                return 0
            if j < 0 or j >= m:
                return 0
            if grid[i][j] == 0:
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            res = val + max(dfs(i-1, j), dfs(i+1, j), dfs(i, j-1), dfs(i, j+1))
            grid[i][j] = val
            return res

        return max(dfs(i, j) for i in range(n) for j in range(m))