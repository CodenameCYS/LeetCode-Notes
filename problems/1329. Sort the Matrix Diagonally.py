'''
=== 1329. Sort the Matrix Diagonally ===

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Example 1:
    Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 
Constraints:
    1. m == mat.length
    2. n == mat[i].length
    3. 1 <= m, n <= 100
    4. 1 <= mat[i][j] <= 100
'''
# === 80ms(89.70%) && 14.8MB(25.18%) === #
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        def change(r, c):
            if r >= n or c >= m:
                return
            if r == 0:
                l = min(n, m-c)
                arr = sorted([mat[i][c+i] for i in range(l)])
                for i in range(l):
                    mat[i][c+i] = arr[i]
            else:
                l = min(m, n-r)
                arr = sorted([mat[r+i][i] for i in range(l)])
                for i in range(l):
                    mat[r+i][i] = arr[i]
            return
        
        for i in range(max(m, n)):
            if i == 0:
                change(0, 0)
            else:
                change(0, i)
                change(i, 0)
        return mat
        