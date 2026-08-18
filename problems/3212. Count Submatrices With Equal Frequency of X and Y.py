'''
=== 3212. Count Submatrices With Equal Frequency of X and Y ===

Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contains:
    - grid[0][0]
    - an equal frequency of 'X' and 'Y'.
    - at least one 'X'.

Example 1:
    Input: grid = [["X","Y","."],["Y",".","."]]
    Output: 3
    Explanation:
Example 2:
    Input: grid = [["X","X"],["X","Y"]]
    Output: 0
    Explanation:
    No submatrix has an equal frequency of 'X' and 'Y'.
Example 3:
    Input: grid = [[".","."],[".","."]]
    Output: 0
    Explanation:
    No submatrix has at least one 'X'.

Constraints:
    1. 1 <= grid.length, grid[i].length <= 1000
    2. grid[i][j] is either 'X', 'Y', or '.'.
'''
# === 3560ms && 108.8MB === #
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def count(ch):
            cnt = [[0 for _ in range(m)] for _ in range(n)]
            cnt[0][0] = 0 if grid[0][0] != ch else 1
            for j in range(1, m):
                cnt[0][j] = cnt[0][j-1] if grid[0][j] != ch else cnt[0][j-1]+1
            for i in range(1, n):
                cnt[i][0] = cnt[i-1][0] if grid[i][0] != ch else cnt[i-1][0]+1
                for j in range(1, m):
                    cnt[i][j] = cnt[i-1][j] + cnt[i][j-1] - cnt[i-1][j-1]
                    if grid[i][j] == ch:
                        cnt[i][j] += 1
            return cnt
        
        cntx = count("X")
        cnty = count("Y")
        ans = 0
        for i in range(n):
            for j in range(m):
                if cntx[i][j] == cnty[i][j] and cntx[i][j] > 0:
                    ans += 1
        return ans