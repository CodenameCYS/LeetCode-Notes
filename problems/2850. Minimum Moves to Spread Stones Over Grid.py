'''
=== 2850. Minimum Moves to Spread Stones Over Grid ===

You are given a 0-indexed 2D integer matrix grid of size 3 * 3, representing the number of stones in each cell. The grid contains exactly 9 stones, and there can be multiple stones in a single cell.
In one move, you can move a single stone from its current cell to any other cell if the two cells share a side.
Return the minimum number of moves required to place one stone in each cell.

Example 1:
    Input: grid = [[1,1,0],[1,1,1],[1,2,1]]
    Output: 3
    Explanation: One possible sequence of moves to place one stone in each cell is: 
    1- Move one stone from cell (2,1) to cell (2,2).
    2- Move one stone from cell (2,2) to cell (1,2).
    3- Move one stone from cell (1,2) to cell (0,2).
    In total, it takes 3 moves to place one stone in each cell of the grid.
    It can be shown that 3 is the minimum number of moves required to place one stone in each cell.
Example 2:
    Input: grid = [[1,3,0],[1,0,0],[1,0,3]]
    Output: 4
    Explanation: One possible sequence of moves to place one stone in each cell is:
    1- Move one stone from cell (0,1) to cell (0,2).
    2- Move one stone from cell (0,1) to cell (1,1).
    3- Move one stone from cell (2,2) to cell (1,2).
    4- Move one stone from cell (2,2) to cell (2,1).
    In total, it takes 4 moves to place one stone in each cell of the grid.
    It can be shown that 4 is the minimum number of moves required to place one stone in each cell.
 
Constraints:
    1. grid.length == grid[i].length == 3
    2. 0 <= grid[i][j] <= 9
    3. Sum of grid is equal to 9.
'''
# === 1171ms && 16.4MB === #
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        _from = [0 for _ in range(9)]
        _to = [0 for _ in range(9)]
        for i in range(3):
            for j in range(3):
                idx = i * 3 + j
                if grid[i][j] == 0:
                    _to[idx] = 1
                elif grid[i][j] > 1:
                    _from[idx] = grid[i][j] - 1
                    
        def cal_distance(i, j):
            r1, c1 = i//3, i%3
            r2, c2 = j//3, j%3
            return abs(r1-r2) + abs(c1-c2)
                    
        def dfs(idx):
            if idx >= 9:
                return 0
            if _from[idx] == 0:
                return dfs(idx+1)
            res = math.inf
            _from[idx] -= 1
            for i in range(9):
                if _to[i] == 0:
                    continue
                _to[i] = 0
                res = min(res, cal_distance(idx, i) + dfs(idx))
                _to[i] = 1
            _from[idx] += 1
            return res
        
        return dfs(0)
                    
                