'''
=== 2132. Stamping the Grid ===

You are given an m x n binary matrix grid where each cell is either 0 (empty) or 1 (occupied).
You are then given stamps of size stampHeight x stampWidth. We want to fit the stamps such that they follow the given restrictions and requirements:
    1. Cover all the empty cells.
    2. Do not cover any of the occupied cells.
    3. We can put as many stamps as we want.
    4. Stamps can overlap with each other.
    5. Stamps are not allowed to be rotated.
    6. Stamps must stay completely inside the grid.
Return true if it is possible to fit the stamps while following the given restrictions and requirements. Otherwise, return false.

Example 1:
    Input: grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
    Output: true
    Explanation: We have two overlapping stamps (labeled 1 and 2 in the image) that are able to cover all the empty cells.
Example 2:
    Input: grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2 
    Output: false 
    Explanation: There is no way to fit the stamps onto all the empty cells without the stamps going outside the grid.
 
Constraints:
    1. m == grid.length
    2. n == grid[r].length
    3. 1 <= m, n <= 105
    4. 1 <= m * n <= 2 * 105
    5. grid[r][c] is either 0 or 1.
    6. 1 <= stampHeight, stampWidth <= 105
'''
# === 4408ms && 55.9MB === #
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        n, m = len(grid), len(grid[0])
        cumsum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                cumsum[i+1][j+1] = grid[i][j] + cumsum[i+1][j] + cumsum[i][j+1] - cumsum[i][j]
        # print(cumsum)
        
        status = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n-stampHeight+1):
            for j in range(m-stampWidth+1):
                if cumsum[i+stampHeight][j+stampWidth] + cumsum[i][j] - cumsum[i+stampHeight][j] - cumsum[i][j+stampWidth] != 0:
                    continue
                status[i][j] = 1
        # print(status)
        
        for i in range(n-1):
            status[i+1][0] += status[i][0]
        for j in range(m-1):
            status[0][j+1] += status[0][j]
        for i in range(n-1):
            for j in range(m-1):
                status[i+1][j+1] += status[i+1][j] + status[i][j+1] - status[i][j]
        # print(status)
                
        def is_paint(i, j):
            if i < stampHeight and j < stampWidth:
                return status[i][j]
            elif i < stampHeight:
                return status[i][j] - status[i][j-stampWidth]
            elif j < stampWidth:
                return status[i][j] - status[i-stampHeight][j]
            else:
                return status[i][j] - status[i][j-stampWidth] - status[i-stampHeight][j] + status[i-stampHeight][j-stampWidth]
                
        return all(is_paint(i, j) + grid[i][j] > 0 for i in range(n) for j in range(m))
                
        
                
        
        