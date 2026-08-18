'''
=== 1293. Shortest Path in a Grid with Obstacles Elimination ===

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.
Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Example 1:
    Input: 
    grid = 
    [[0,0,0],
    [1,1,0],
    [0,0,0],
    [0,1,1],
    [0,0,0]], 
    k = 1
    Output: 6
    Explanation: 
    The shortest path without eliminating any obstacle is 10. 
    The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:
    Input: 
    grid = 
    [[0,1,1],
    [1,1,1],
    [1,0,0]], 
    k = 1
    Output: -1
    Explanation: 
    We need to eliminate at least two obstacles to find such a walk.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 40
    4. 1 <= k <= m * n
    5. grid[i][j] == 0 or 1
    6. grid[0][0] == grid[m - 1][n - 1] == 0
'''
# === 104ms(72.14%) && 14.4MB(95.84%) === #
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        seen = {(0, 0): 0}
        
        def is_valid(i, j, rm):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if grid[i][j] == 1:
                rm += 1
            if rm > k:
                return False
            if (i, j) in seen and seen[(i, j)] <= rm:
                return False
            return True
        
        s = [(0, 0, 0, 0)]
        while s != []:
            # print(s, seen)
            dis, rm, i, j = heapq.heappop(s)
            if i == n-1 and j == m-1:
                return dis
            if is_valid(i-1, j, rm):
                if grid[i-1][j] == 0:
                    heapq.heappush(s, (dis+1, rm, i-1, j))
                    seen[(i-1, j)] = rm
                else:
                    heapq.heappush(s, (dis+1, rm+1, i-1, j))
                    seen[(i-1, j)] = rm + 1
            if is_valid(i+1, j, rm):
                if grid[i+1][j] == 0:
                    heapq.heappush(s, (dis+1, rm, i+1, j))
                    seen[(i+1, j)] = rm
                else:
                    heapq.heappush(s, (dis+1, rm+1, i+1, j))
                    seen[(i+1, j)] = rm + 1
            if is_valid(i, j-1, rm):
                if grid[i][j-1] == 0:
                    heapq.heappush(s, (dis+1, rm, i, j-1))
                    seen[(i, j-1)] = rm
                else:
                    heapq.heappush(s, (dis+1, rm+1, i, j-1))
                    seen[(i, j-1)] = rm + 1
            if is_valid(i, j+1, rm):
                if grid[i][j+1] == 0:
                    heapq.heappush(s, (dis+1, rm, i, j+1))
                    seen[(i, j+1)] = rm
                else:
                    heapq.heappush(s, (dis+1, rm+1, i, j+1))
                    seen[(i, j+1)] = rm + 1
        return -1
        
        