'''
=== 867. Transpose Matrix ===

Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:
    Input: matrix = [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]
 
Constraints:
    1. m == matrix.length
    2. n == matrix[i].length
    3. 1 <= m, n <= 1000
    4. 1 <= m * n <= 105
    5. -109 <= matrix[i][j] <= 109
'''
# === 76ms(41.42%) && 15MB(33.54%) === #
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        res = []
        for j in range(m):
            res.append([matrix[i][j] for i in range(n)])
        return res
