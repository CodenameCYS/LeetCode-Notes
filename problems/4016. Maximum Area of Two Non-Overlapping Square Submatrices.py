'''
=== 4016. Maximum Area of Two Non-Overlapping Square Submatrices ===

You are given a 2D integer matrix mat of size m × n, where:
    - mat[r][c] == 1 means the cell at row r and column c is usable.
    - mat[r][c] == 0 means it is not usable.
Your task is to find two submatrices that satisfy the following conditions:
    - Both submatrices must be squares of the same side length k.
    - The two submatrices must not share any cell.
    - Each submatrix can only cover cells where mat[r][c] == 1.
Return the maximum possible area of each of the two squares. If it is not possible to choose two such squares, return 0.

Example 1:
    Input: mat = [[1,1,1,0],[1,1,1,1],[0,0,1,1]]
    Output: 4
    Explanation:
    The largest equal non-overlapping squares have side length k = 2 with area 4.
    First square starts at top-left (0, 0) and covers cells (0, 0), (0, 1), (1, 0), and (1, 1).
    Second square starts at top-left (1, 2) and covers cells (1, 2), (1, 3), (2, 2), and (2, 3).
    Thus, the answer is 4.
Example 2:
    Input: mat = [[0,1],[1,0]]
    Output: 1
    Explanation:
    The largest equal non-overlapping squares have side length k = 1 with area 1.
    First square starts at top-left (0, 1) and covers cell (0, 1).
    Second square starts at top-left (1, 0) and covers cell (1, 0).
    Thus, the answer is 1.
Example 3:
    Input: mat = [[0,0],[0,1]]
    Output: 0
    Explanation:
    There is only one usable cell, so it is impossible to choose two non-overlapping squares. Thus, the answer is 0.

Constraints:
    1. mat.length == m
    2. mat[i].length == n
    3. 1 <= m, n <= 500
    4. mat[i][j] is either 0 or 1.
'''
# === 1648ms && 39.48MB === #
class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        cumsum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                cumsum[i+1][j+1] = mat[i][j] + cumsum[i][j+1] + cumsum[i+1][j] - cumsum[i][j] 
        if cumsum[n][m] <= 1:
            return 0

        # for line in mat:
        #     print(" ".join([str(x) for x in line]))

        def get_area(i, j, k):
            return cumsum[i+k][j+k]-cumsum[i][j+k]-cumsum[i+k][j]+cumsum[i][j]

        def is_possible(k):
            corners = []
            for i in range(min(k, n-k+1)):
                for j in range(min(k, m-k+1)):
                    if get_area(i, j, k) == k*k:
                        corners.append((i, j))
            for i in range(n-k+1):
                for j in range(m-k+1):
                    if i < k and j < k:
                        continue
                    if get_area(i, j, k) == k*k:
                        if any(abs(i-x) >= k or abs(j-y) >= k for x, y in corners):
                            return True
                        corners.append((i, j))
            # print(k, corners)
            return False

        i, j = 1, max(n, m) // 2 + 1
        while j-i>1:
            k = (i+j)//2
            if is_possible(k):
                i = k
            else:
                j = k
        return i*i
        
