'''
=== 2290. Minimum Obstacle Removal to Reach Corner ===

You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
    - 0 represents an empty cell,
    - 1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.
Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

Example 1:
    Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
    Output: 2
    Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
    It can be shown that we need to remove at least 2 obstacles, so we return 2.
    Note that there may be other ways to remove 2 obstacles to create a path.
Example 2:
    Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    Output: 0
    Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 105
    4. 2 <= m * n <= 105
    5. grid[i][j] is either 0 or 1.
    6. grid[0][0] == grid[m - 1][n - 1] == 0
'''
# === 8747ms && 40MB === #
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        distance = [[math.inf for _ in range(m)] for _ in range(n)]
        distance[0][0] = 0
        q = [(0, 0)]
        
        def inside(x, y):
            return 0 <= x < n and 0 <= y < m
        
        while q:
            x0, y0 = q.pop(0)
            for x, y in [(x0-1, y0), (x0+1, y0), (x0, y0-1), (x0, y0+1)]:
                if not inside(x, y):
                    continue
                if distance[x][y] > distance[x0][y0] + grid[x][y]:
                    distance[x][y] = distance[x0][y0] + grid[x][y]
                    if grid[x][y]:
                        q.append((x, y))
                    else:
                        q.insert(0, (x, y))
        return distance[-1][-1]
        