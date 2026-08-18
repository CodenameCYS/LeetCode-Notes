'''
=== 2536. Increment Submatrices by One ===

You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.
You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:
    - Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.

Example 1:
    Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
    Output: [[1,1,0],[1,2,1],[0,1,1]]
    Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
    - In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
    - In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
Example 2:
    Input: n = 2, queries = [[0,0,1,1]]
    Output: [[1,1],[1,1]]
    Explanation: The diagram above shows the initial matrix and the matrix after the first query.
    - In the first query we add 1 to every element in the matrix.
    
Constraints:
    1. 1 <= n <= 500
    2. 1 <= queries.length <= 104
    3. 0 <= row1i <= row2i < n
    4. 0 <= col1i <= col2i < n
'''
# === 1793ms && 35.4MB === #
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for a, b, c, d in queries:
            matrix[a][b] += 1
            matrix[c+1][b] -= 1
            matrix[a][d+1] -= 1
            matrix[c+1][d+1] += 1
        
        for j in range(n):
            matrix[0][j+1] += matrix[0][j]
        for i in range(1, n):
            matrix[i][0] += matrix[i-1][0]
            for j in range(1, n+1):
                matrix[i][j] = matrix[i][j] + matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        return [line[:-1] for line in matrix[:-1]]
                
            