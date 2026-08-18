'''
=== 2617. Minimum Number of Visited Cells in a Grid ===

You are given a 0-indexed m x n integer matrix grid. Your initial position is at the top-left cell (0, 0).
Starting from the cell (i, j), you can move to one of the following cells:
    - Cells (i, k) with j < k <= grid[i][j] + j (rightward movement), or
    - Cells (k, j) with i < k <= grid[i][j] + i (downward movement).
Return the minimum number of cells you need to visit to reach the bottom-right cell (m - 1, n - 1). If there is no valid path, return -1.

Example 1:
    Input: grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
    Output: 4
    Explanation: The image above shows one of the paths that visits exactly 4 cells.
Example 2:
    Input: grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
    Output: 3
    Explanation: The image above shows one of the paths that visits exactly 3 cells.
Example 3:
    Input: grid = [[2,1,0],[1,0,0]]
    Output: -1
    Explanation: It can be proven that no path exists.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 105
    4. 1 <= m * n <= 105
    5. 0 <= grid[i][j] < m * n
    6. grid[m - 1][n - 1] == 0
'''
# === 5822ms && 56.5MB === #
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = [(1, 0, 0)]
        seen = {(0, 0)}
        while q:
            step, i, j = heapq.heappop(q)
            i, j = -i, -j
            if i == n-1 and j == m-1:
                return step
            for k in range(1, grid[i][j]+1):
                if i+k < n and (i+k, j) not in seen:
                    seen.add((i+k, j))
                    heapq.heappush(q, (step+1, -(i+k), -j))
                if j+k < m and (i, j+k) not in seen:
                    seen.add((i, j+k))
                    heapq.heappush(q, (step+1, -i, -(j+k)))
        return -1
        