'''
=== 1034. Coloring A Border ===

Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.
Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.
The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).
Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square with the given color, and return the final grid.

Example 1:
    Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
    Output: [[3, 3], [3, 2]]
Example 2:
    Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
    Output: [[1, 3, 3], [2, 3, 3]]
Example 3:
    Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
    Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
 
Note:
    1. 1 <= grid.length <= 50
    2. 1 <= grid[0].length <= 50
    3. 1 <= grid[i][j] <= 1000
    4. 0 <= r0 < grid.length
    5. 0 <= c0 < grid[0].length
    6. 1 <= color <= 1000
'''
# === 96ms(96.21%) & 13.5MB === #
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        mystack = [(r0, c0)]
        connected = set([r0, c0])
        border = set()
        flag = 0
        R = len(grid)
        C = len(grid[0])
        while flag < len(mystack):
            for delta in [(0,1), (0,-1), (1,0), (-1,0)]:
                r = mystack[flag][0] + delta[0]
                c = mystack[flag][1] + delta[1]
                if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] != grid[r0][c0]:
                    border.add(mystack[flag])
                else:
                    if grid[r][c] == grid[r0][c0] and (r,c) not in connected:
                        mystack.append((r,c))
                        connected.add((r,c))
            flag += 1
        for r,c in border:
            grid[r][c] = color
        return grid
                        