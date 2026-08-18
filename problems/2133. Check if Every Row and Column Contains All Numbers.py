'''
=== 2133. Check if Every Row and Column Contains All Numbers ===

An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

Example 1:
    Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
    Output: true
    Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
    Hence, we return true.
Example 2:
    Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
    Output: false
    Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
    Hence, we return false.
 
Constraints:
    1. n == matrix.length == matrix[i].length
    2. 1 <= n <= 100
    3. 1 <= matrix[i][j] <= n
'''
# === 1161ms && 14.8MB === #
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        if any(len(set(l)) != n for l in matrix):
            return False
        if any(len(set([matrix[j][i] for j in range(n)])) != n for i in range(n)):
            return False
        return True
        