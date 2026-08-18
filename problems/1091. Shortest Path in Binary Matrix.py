'''
=== 1091. Shortest Path in Binary Matrix ===

In an N by N square grid, each cell is either empty (0) or blocked (1).
A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:
    - Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
    - C_1 is at location (0, 0) (ie. has value grid[0][0])
    - C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
    = If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

Example 1:
    Input: [[0,1],[1,0]]
    Output: 2
Example 2:
    Input: [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4

Note:
    1. 1 <= grid.length == grid[0].length <= 100
    2. grid[r][c] is 0 or 1
'''
# === === #
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        seen = {(0, 0): 1}
        stack = [(0, 0, 1)]
        n, m = len(grid), len(grid[0])
        while stack:
            x, y, dis = stack.pop(0)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if 0 <= x+i < n and 0 <= y+j < m and grid[x+i][y+j] == 0 and seen.get((x+i, y+j), math.inf) > dis+1:
                        stack.append((x+i, y+j, dis+1))
                        seen[(x+i, y+j)] = dis+1
        return seen.get((n-1, m-1), -1)