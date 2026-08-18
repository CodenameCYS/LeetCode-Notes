'''
=== 3148. Maximum Difference Score in a Grid ===

You are given an m x n matrix grid consisting of positive integers. You can move from a cell in the matrix to any other cell that is either to the bottom or to the right (not necessarily adjacent). The score of a move from a cell with the value c1 to a cell with the value c2 is c2 - c1.
You can start at any cell, and you have to make at least one move.
Return the maximum total score you can achieve.

Example 1:
    Input: grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
    Output: 9
    Explanation: We start at the cell (0, 1), and we perform the following moves:
    - Move from the cell (0, 1) to (2, 1) with a score of 7 - 5 = 2.
    - Move from the cell (2, 1) to (2, 2) with a score of 14 - 7 = 7.
    The total score is 2 + 7 = 9.
Example 2:
    Input: grid = [[4,3,2],[3,2,1]]
    Output: -1
    Explanation: We start at the cell (0, 0), and we perform one move: (0, 0) to (0, 1). The score is 3 - 4 = -1.

Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 2 <= m, n <= 1000
    4. 4 <= m * n <= 105
    5. 1 <= grid[i][j] <= 105
'''
# === 994ms && 30MB === #
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        _max = [[-math.inf for _ in range(m)] for _ in range(n)]
        for i in range(n-2, -1, -1):
            _max[i][-1] = max(_max[i+1][-1], grid[i+1][-1])
        for j in range(m-2, -1, -1):
            _max[-1][j] = max(_max[-1][j+1], grid[-1][j+1])
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                _max[i][j] = max(_max[i][j+1], _max[i+1][j], grid[i+1][j], grid[i][j+1])
        return max(_max[i][j]-grid[i][j] for i in range(n) for j in range(m))
                
                
        