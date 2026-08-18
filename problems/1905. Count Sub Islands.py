'''
=== 1905. Count Sub Islands ===

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.

Example 1:
    Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    Output: 3
    Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
    The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:
    Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    Output: 2 
    Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
    The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 
Constraints:
    1. m == grid1.length == grid2.length
    2. n == grid1[i].length == grid2[i].length
    3. 1 <= m, n <= 500
    4. grid1[i][j] and grid2[i][j] are either 0 or 1.
'''
# === 2808ms && 22.7MB === #
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 0:
                    continue
                grid2[i][j] = 0
                s = [(i, j)]
                seen = []
                while s != []:
                    x, y = s.pop(0)
                    seen.append((x, y))
                    if x-1 >= 0 and grid2[x-1][y] == 1:
                        grid2[x-1][y] = 0
                        s.append((x-1, y))
                    if x+1 < n and grid2[x+1][y] == 1:
                        grid2[x+1][y] = 0
                        s.append((x+1, y))
                    if y-1 >= 0 and grid2[x][y-1] == 1:
                        grid2[x][y-1] = 0
                        s.append((x, y-1))
                    if y+1 < m and grid2[x][y+1] == 1:
                        grid2[x][y+1] = 0
                        s.append((x, y+1))
                if all(grid1[x][y] == 1 for x, y in seen):
                    cnt += 1
        return cnt