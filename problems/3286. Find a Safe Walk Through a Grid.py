'''
=== 3286. Find a Safe Walk Through a Grid ===

You are given an m x n binary matrix grid and an integer health.
You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).
You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.
Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.
Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

Example 1:
    Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1
    Output: true
    Explanation:
    The final cell can be reached safely by walking along the gray cells below.
Example 2:
    Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3
    Output: false
    Explanation:
    A minimum of 4 health points is needed to reach the final cell safely.
Example 3:
    Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5
    Output: true
    Explanation:
    The final cell can be reached safely by walking along the gray cells below.
    Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 50
    4. 2 <= m * n
    5. 1 <= health <= m + n
    6. grid[i][j] is either 0 or 1.
'''
# === 238ms && 17.3MB === #
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        if health - grid[0][0] < 1:
            return False
        q = [(-health+grid[0][0], 0, 0)]
        seen = set()
        while q:
            h, x, y = heapq.heappop(q)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            h = -h
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen and h - grid[nx][ny] > 0:
                    if nx == n-1 and ny == m-1:
                        return True
                    heapq.heappush(q, (-(h-grid[nx][ny]), nx, ny))
        return False
                    
        