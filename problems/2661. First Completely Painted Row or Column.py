'''
=== 2661. First Completely Painted Row or Column ===

You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
Return the smallest index i at which either a row or a column will be completely painted in mat.

Example 1:
    image explanation for example 1
    Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
    Output: 2
    Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:
    image explanation for example 2
    Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
    Output: 3
    Explanation: The second column becomes fully painted at arr[3].
 
Constraints:
    1. m == mat.length
    2. n = mat[i].length
    3. arr.length == m * n
    4. 1 <= m, n <= 105
    5. 1 <= m * n <= 105
    6. 1 <= arr[i], mat[r][c] <= m * n
    7. All the integers of arr are unique.
    8. All the integers of mat are unique.
'''
# === 1245ms && 51.7MB === #
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        index = {x: i for i, x in enumerate(arr)}
        row = min(max(index[mat[i][j]] for j in range(m)) for i in range(n))
        col = min(max(index[mat[i][j]] for i in range(n)) for j in range(m))
        return min(row, col)
        
        