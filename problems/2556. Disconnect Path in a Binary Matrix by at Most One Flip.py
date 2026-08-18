'''
=== 2556. Disconnect Path in a Binary Matrix by at Most One Flip ===

You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).
You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).
Return true if it is possible to make the matrix disconnect or false otherwise.
Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.

Example 1:
    Input: grid = [[1,1,1],[1,0,0],[1,1,1]]
    Output: true
    Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.
Example 2:
    Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
    Output: false
    Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 1000
    4. 1 <= m * n <= 105
    5. grid[i][j] is either 0 or 1.
    6. grid[0][0] == grid[m - 1][n - 1] == 1
'''
# === 1970ms && 107.1MB === #
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        def show(grid):
            for line in grid:
                print(line)
            print("=" * 5)
            return
        
        @lru_cache(None)
        def query_from(i, j):
            if i >= n or j >= m:
                return 0
            if grid[i][j] == 0:
                return 0
            if i == n-1 and j == m-1:
                return 1
            return query_from(i+1, j) + query_from(i, j+1)
        
        @lru_cache(None)
        def query_to(i, j):
            if i < 0 or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return query_to(i-1, j) + query_to(i, j-1)

        from_paths = [[query_from(i, j) for j in range(m)] for i in range(n)]
        to_paths = [[query_to(i, j) for j in range(m)] for i in range(n)]
        tot_path = from_paths[0][0]

        return any(from_paths[i][j] * to_paths[i][j] == tot_path for i in range(n) for j in range(m) if (i, j) not in [(0,0), (n-1, m-1)])
        