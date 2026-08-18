'''
=== 1582. Special Positions in a Binary Matrix ===

Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.
A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
    Input: mat = [[1,0,0],
                  [0,0,1],
                  [1,0,0]]
    Output: 1
    Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:
    Input: mat = [[1,0,0],
                  [0,1,0],
                  [0,0,1]]
    Output: 3
    Explanation: (0,0), (1,1) and (2,2) are special positions. 
Example 3:
    Input: mat = [[0,0,0,1],
                  [1,0,0,0],
                  [0,1,1,0],
                  [0,0,0,0]]
    Output: 2
Example 4:
    Input: mat = [[0,0,0,0,0],
                  [1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,1]]
    Output: 3
 
Constraints:
    1. rows == mat.length
    2. cols == mat[i].length
    3. 1 <= rows, cols <= 100
    4. mat[i][j] is 0 or 1.
'''
# === 168ms && 14.1MB === #
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            eff = []
            for j in range(m):
                if mat[i][j] == 1:
                    eff.append((i, j))
            if len(eff) == 1:
                j = eff[0][1]
                count = 0
                for k in range(n):
                    if mat[k][j] == 1:
                        count += 1
                if count == 1:
                    ans += 1
        return ans