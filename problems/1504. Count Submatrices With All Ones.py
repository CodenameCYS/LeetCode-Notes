'''
=== 1504. Count Submatrices With All Ones ===

Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

Example 1:
    Input: mat = [[1,0,1],
                  [1,1,0],
                  [1,1,0]]
    Output: 13
    Explanation:
    There are 6 rectangles of side 1x1.
    There are 2 rectangles of side 1x2.
    There are 3 rectangles of side 2x1.
    There is 1 rectangle of side 2x2. 
    There is 1 rectangle of side 3x1.
    Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:
    Input: mat = [[0,1,1,0],
                  [0,1,1,1],
                  [1,1,1,0]]
    Output: 24
    Explanation:
    There are 8 rectangles of side 1x1.
    There are 5 rectangles of side 1x2.
    There are 2 rectangles of side 1x3. 
    There are 4 rectangles of side 2x1.
    There are 2 rectangles of side 2x2. 
    There are 2 rectangles of side 3x1. 
    There is 1 rectangle of side 3x2. 
    Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:
    Input: mat = [[1,1,1,1,1,1]]
    Output: 21
Example 4:
    Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
    Output: 5
 
Constraints:
    1. 1 <= rows <= 150
    2. 1 <= columns <= 150
    3. 0 <= mat[i][j] <= 1
'''
# === 6724ms && 14.7MB === #
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        cumsum = [[0 for j in range(m+1)] for i in range(n+1)]
        # print(cumsum[0])
        for i in range(1, n+1):
            for j in range(1, m+1):
                cumsum[i][j] = mat[i-1][j-1] + cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1]
            # print(cumsum[i])
        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                ii = i+1
                while ii < n and mat[ii][j] == 1:
                    ii += 1
                jj = j+1
                while jj < m and mat[i][jj] == 1:
                    jj += 1
                for x in range(i+1, ii+1):
                    for y in range(j+1, jj+1):
                        if cumsum[x][y] + cumsum[i][j] -cumsum[x][j] - cumsum[i][y] == (x-i) * (y-j):
                            count += 1
                # print(i, j, ii, jj, count)
        return count