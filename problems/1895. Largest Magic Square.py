'''
=== 1895. Largest Magic Square ===

A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.
Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

Example 1:
    Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
    Output: 3
    Explanation: The largest magic square has a size of 3.
    Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
    - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
    - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
    - Diagonal sums: 5+4+3 = 6+4+2 = 12
Example 2:
    Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
    Output: 2
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 50
    4. 1 <= grid[i][j] <= 106
'''
# === 896ms && 14.5MB === #
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        sgrid = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                sgrid[i+1][j+1]=grid[i][j] + sgrid[i+1][j] + sgrid[i][j+1] - sgrid[i][j]
        # for line in grid:
        #     print(line)
        # for line in sgrid:
        #     print(line)
        
        k = min(n, m)
        while k > 1:
            for i in range(n-k+1):
                for j in range(m-k+1):
                    s1 = sum(grid[i+l][j+l] for l in range(k))
                    s2 = sum(grid[i+l][j+k-1-l] for l in range(k))
                    if s1 != s2:
                        continue
                    s = s1
                    if all(sgrid[i+l+1][j+k]-sgrid[i+l+1][j]-sgrid[i+l][j+k]+sgrid[i+l][j] == s for l in range(k)) and all(sgrid[i+k][j+l+1]-sgrid[i+k][j+l]-sgrid[i][j+l+1]+sgrid[i][j+l] == s for l in range(k)):
                        # print(i, j, k, s)
                        return k
            k -= 1
        return k
                        