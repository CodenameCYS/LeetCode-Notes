'''
=== 2713. Maximum Strictly Increasing Cells in a Matrix ===

Given a 1-indexed m x n integer matrix mat, you can select any cell in the matrix as your starting cell.
From the starting cell, you can move to any other cell in the same row or column, but only if the value of the destination cell is strictly greater than the value of the current cell. You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.
Your task is to find the maximum number of cells that you can visit in the matrix by starting from some cell.
Return an integer denoting the maximum number of cells that can be visited.

Example 1:
    Input: mat = [[3,1],[3,4]]
    Output: 2
    Explanation: The image shows how we can visit 2 cells starting from row 1, column 2. It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2. 
Example 2:
    Input: mat = [[1,1],[1,1]]
    Output: 1
    Explanation: Since the cells must be strictly increasing, we can only visit one cell in this example. 
Example 3:
    Input: mat = [[3,1,6],[-9,5,7]]
    Output: 4
    Explanation: The image above shows how we can visit 4 cells starting from row 2, column 1. It can be shown that we cannot visit more than 4 cells no matter where we start from, so the answer is 4. 
 
Constraints:
    1. m == mat.length 
    2. n == mat[i].length 
    3. 1 <= m, n <= 105
    4. 1 <= m * n <= 105
    5. -105 <= mat[i][j] <= 105
'''
# === 7044ms && 101.1MB === #
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        
        rows = [[(math.inf, 0)] for _ in range(n)]
        cols = [[(math.inf, 0)] for _ in range(m)]
        
        res = [[1 for _ in range(m)] for _ in range(n)]
        vals = sorted([[mat[i][j], i, j] for i in range(n) for j in range(m)], reverse=True)
        # print(vals)
        for v, i, j in vals:
            c = bisect.bisect_left(rows[i], (v, 0))
            r = bisect.bisect_left(cols[j], (v, 0))
            res[i][j] = 1 + max(-rows[i][c][1], -cols[j][r][1])
            bisect.insort(rows[i], (v, -res[i][j]))
            bisect.insort(cols[j], (v, -res[i][j]))
            # print(v, i, j, rows[i], cols[j])
        # print(res)
        return max(res[i][j] for i in range(n) for j in range(m))
                
                
        