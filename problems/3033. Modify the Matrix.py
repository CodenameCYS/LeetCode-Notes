'''
=== 3033. Modify the Matrix ===

Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make answer equal to matrix, then replace each element with the value -1 with the maximum element in its respective column.
Return the matrix answer.

Example 1:
    Input: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
    Output: [[1,2,9],[4,8,6],[7,8,9]]
    Explanation: The diagram above shows the elements that are changed (in blue).
    - We replace the value in the cell [1][1] with the maximum value in the column 1, that is 8.
    - We replace the value in the cell [0][2] with the maximum value in the column 2, that is 9.
Example 2:
    Input: matrix = [[3,-1],[5,2]]
    Output: [[3,2],[5,2]]
    Explanation: The diagram above shows the elements that are changed (in blue).
 
Constraints:
    1. m == matrix.length
    2. n == matrix[i].length
    3. 2 <= m, n <= 50
    4. -1 <= matrix[i][j] <= 100
    5. The input is generated such that each column contains at least one non-negative integer.
'''
# === 87ms && 16.6MB === #
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        _max = [-1 for _ in range(m)]
        to_change = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    to_change.append((i, j))
                else:
                    _max[j] = max(_max[j], matrix[i][j])
        for i, j in to_change:
            matrix[i][j] = _max[j]
        return matrix