'''
=== 3240. Minimum Number of Flips to Make Binary Grid Palindromic II ===

You are given an m x n binary matrix grid.
A row or column is considered palindromic if its values read the same forward and backward.
You can flip any number of cells in grid from 0 to 1, or from 1 to 0.
Return the minimum number of cells that need to be flipped to make all rows and columns palindromic, and the total number of 1's in grid divisible by 4.

Example 1:
    Input: grid = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
    Explanation:
Example 2:
    Input: grid = [[0,1],[0,1],[0,0]]
    Output: 2
    Explanation:
Example 3:
    Input: grid = [[1],[1]]
    Output: 2
    Explanation:

Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m * n <= 2 * 105
    4. 0 <= grid[i][j] <= 1
'''
# === 2341ms && 70.4MB === #
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n//2):
            for j in range(m//2):
                s = grid[i][j] + grid[n-1-i][j] + grid[i][m-1-j] + grid[n-1-i][m-1-j]
                if s == 1 or s == 3:
                    ans += 1
                elif s == 2:
                    ans += 2

        cnt, changed = 0, 0
        if n % 2 == 1:
            for j in range(m // 2):
                s = grid[n//2][j] + grid[n//2][m-1-j]
                if s == 1:
                    changed += 1
                    ans += 1
                else:
                    cnt += s
        if m % 2 == 1:
            for i in range(n//2):
                s = grid[i][m//2] + grid[n-1-i][m//2]
                if s == 1:
                    changed += 1
                    ans += 1
                else:
                    cnt += s
        if cnt % 4 == 2 and changed == 0:
            ans += 2
            
        if n % 2 == 1 and m % 2 == 1:
            ans += grid[n//2][m//2]
        return ans