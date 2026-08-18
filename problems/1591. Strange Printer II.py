'''
=== 1591. Strange Printer II ===

There is a strange printer with the following two special requirements:
    - On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
    - Once the printer has used a color for the above operation, the same color cannot be used again.
You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.
Return true if it is possible to print the matrix targetGrid, otherwise, return false.

Example 1:
    Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
    Output: true
Example 2:
    Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
    Output: true
Example 3:
    Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
    Output: false
    Explanation: It is impossible to form targetGrid because it is not allowed to print the same color in different turns.
Example 4:
    Input: targetGrid = [[1,1,1],[3,1,3]]
    Output: false
 
Constraints:
    1. m == targetGrid.length
    2. n == targetGrid[i].length
    3. 1 <= m, n <= 60
    4. 1 <= targetGrid[row][col] <= 60
'''
# === 348ms && 13.9MB === #
class Solution:
    def isPrintable(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        colors = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] not in colors:
                    colors[grid[i][j]] = [i, j, i, j]
                else:
                    colors[grid[i][j]] = [min(colors[grid[i][j]][0], i), min(colors[grid[i][j]][1], j), max(colors[grid[i][j]][2], i), max(colors[grid[i][j]][3], j)]
        colors = colors.items()
        
        painted = [[0 for _ in range(m)] for _ in range(n)]
        def is_paintable(block):
            c, (x1, y1, x2, y2) = block
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if painted[i][j] == 0 and grid[i][j] != c:
                        return False
            return True
        def paint(blocks):
            nonlocal painted
            c, (x1, y1, x2, y2) = block
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if painted[i][j] == 0:
                        painted[i][j] = c
            return
        
        flag = True
        while flag and colors != []:
            tmp = []
            flag = False
            for block in colors:
                if is_paintable(block):
                    paint(colors)
                    flag = True
                else:
                    tmp.append(block)
            colors = tmp
        
        return flag