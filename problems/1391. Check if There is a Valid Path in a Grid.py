'''
=== 1391. Check if There is a Valid Path in a Grid ===

Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
    - 1 which means a street connecting the left cell and the right cell.
    - 2 which means a street connecting the upper cell and the lower cell.
    - 3 which means a street connecting the left cell and the lower cell.
    - 4 which means a street connecting the right cell and the lower cell.
    - 5 which means a street connecting the left cell and the upper cell.
    - 6 which means a street connecting the right cell and the upper cell.
You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.
Notice that you are not allowed to change any street.
Return true if there is a valid path in the grid or false otherwise.

Example 1:
    Input: grid = [[2,4,3],[6,5,2]]
    Output: true
    Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:
    Input: grid = [[1,2,1],[1,2,1]]
    Output: false
    Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:
    Input: grid = [[1,1,2]]
    Output: false
    Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:
    Input: grid = [[1,1,1,1,1,1,3]]
    Output: true
Example 5:
    Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
    Output: true
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 300
    4. 1 <= grid[i][j] <= 6
'''
# === 1788ms && 27.8MB === #
class Solution:
    def __init__(self):
        self.direction = {
            1: [(0, -1), (0, 1)],
            2: [(1, 0), (-1, 0)],
            3: [(1, 0), (0, -1)],
            4: [(0, 1), (1, 0)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)]
        }
        
    def is_valid_position(self, grid, loc, last_loc):
        if loc[0] < 0 or loc[0] >= len(grid) or loc[1] < 0 or loc[1] >= len(grid[0]):
            return False
        for direction in self.direction[grid[loc[0]][loc[1]]]:
            if loc[0] + direction[0] == last_loc[0] and loc[1] + direction[1] == last_loc[1]:
                return True
        return False
    
    def go_by_one_direction(self, grid, direction):
        trace = {(0,0)}
        m = len(grid); n= len(grid[0])
        if m == 1 and n == 1:
            return True
        
        last_loc = (0, 0)
        loc = direction
        while self.is_valid_position(grid, loc, last_loc):
            trace.add(loc)
            if loc == (m-1, n-1):
                return True
            last_loc = loc
            loc = self.go_to_next_loc(grid, loc, trace)
        return False
    
    def go_to_next_loc(self, grid, loc, trace):
        next_loc = (-1, -1)
        for direction in self.direction[grid[loc[0]][loc[1]]]:
            tmp = (loc[0] + direction[0], loc[1] + direction[1])
            if tmp not in trace:
                next_loc = tmp
        return next_loc
        
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        for direction in self.direction[grid[0][0]]:
            if self.go_by_one_direction(grid, direction):
                return True
        return False
        