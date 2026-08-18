'''
=== 1568. Minimum Number of Days to Disconnect Island ===

Given a 2D grid consisting of 1s (land) and 0s (water).  An island is a maximal 4-directionally (horizontal or vertical) connected group of 1s.
The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
In one day, we are allowed to change any single land cell (1) into a water cell (0).
Return the minimum number of days to disconnect the grid.

Example 1:
    Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    Output: 2
    Explanation: We need at least 2 days to get a disconnected grid.
    Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:
    Input: grid = [[1,1]]
    Output: 2
    Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
Example 3:
    Input: grid = [[1,0,1,0]]
    Output: 0
Example 4:
    Input: grid = [[1,1,0,1,1],
                   [1,1,1,1,1],
                   [1,1,0,1,1],
                   [1,1,0,1,1]]
    Output: 1
Example 5:
    Input: grid = [[1,1,0,1,1],
                   [1,1,1,1,1],
                   [1,1,0,1,1],
                   [1,1,1,1,1]]
    Output: 2

Constraints:
    1. 1 <= grid.length, grid[i].length <= 30
    2. grid[i][j] is 0 or 1.
'''
# === 1560ms && 13.9MB === #
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def is_isolated():
            have_visited = set()
            counter = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 0 or (i, j) in have_visited:
                        continue
                    stack = [(i, j)]
                    have_visited.add((i, j))
                    counter += 1
                    if counter >= 2:
                        return True
                    while stack != []:
                        x, y = stack.pop(0)
                        if x-1 >= 0 and grid[x-1][y] == 1 and (x-1, y) not in have_visited:
                            stack.append((x-1, y))
                            have_visited.add((x-1, y))
                        if x+1 < n and grid[x+1][y] == 1 and (x+1, y) not in have_visited:
                            stack.append((x+1, y))
                            have_visited.add((x+1, y))
                        if y-1 >= 0 and grid[x][y-1] == 1 and (x, y-1) not in have_visited:
                            stack.append((x, y-1))
                            have_visited.add((x, y-1))
                        if y+1 < m and grid[x][y+1] == 1 and (x, y+1) not in have_visited:
                            stack.append((x, y+1))
                            have_visited.add((x, y+1))
            return counter == 0
        
        if is_isolated():
            return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0
                if is_isolated():
                    return 1
                grid[i][j] = 1
        return 2