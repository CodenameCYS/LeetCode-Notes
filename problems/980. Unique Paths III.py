'''
=== 980. Unique Paths III ===

On a 2-dimensional grid, there are 4 types of squares:
    - 1 represents the starting square.  There is exactly one starting square.
    - 2 represents the ending square.  There is exactly one ending square.
    - 0 represents empty squares we can walk over.
    - -1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
    Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    Output: 2
    Explanation: We have the following two paths: 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:
    Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    Output: 4
    Explanation: We have the following four paths: 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
    2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
    3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
    4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:
    Input: [[0,1],[2,0]]
    Output: 0
    Explanation: 
    There is no path that walks over every empty square exactly once.
    Note that the starting and ending square can be anywhere in the grid.
 
Note:
    1. 1 <= grid.length * grid[0].length <= 20
'''
# === 40ms(99.60%) && 13.9MB(43.79%) === #
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    r0, c0 = i, j
        
        ans = 0
        def dfs(r, c):
            nonlocal ans
            grid[r][c] = 3
            if r-1 >= 0:
                if grid[r-1][c] == 0:
                    dfs(r-1, c)
                elif grid[r-1][c] == 2 and all(grid[i][j] != 0 for i in range(n) for j in range(m)):
                    ans += 1
            if r+1 < n:
                if grid[r+1][c] == 0:
                    dfs(r+1, c)
                elif grid[r+1][c] == 2 and all(grid[i][j] != 0 for i in range(n) for j in range(m)):
                    ans += 1
            if c-1 >= 0:
                if grid[r][c-1] == 0:
                    dfs(r, c-1)
                elif grid[r][c-1] == 2 and all(grid[i][j] != 0 for i in range(n) for j in range(m)):
                    ans += 1
            if c+1 < m:
                if grid[r][c+1] == 0:
                    dfs(r, c+1)
                elif grid[r][c+1] == 2 and all(grid[i][j] != 0 for i in range(n) for j in range(m)):
                    ans += 1
            grid[r][c] = 0
            return
        
        dfs(r0, c0)
        return ans
                