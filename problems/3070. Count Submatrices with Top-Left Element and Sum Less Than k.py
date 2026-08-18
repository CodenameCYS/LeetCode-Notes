'''
=== 3070. Count Submatrices with Top-Left Element and Sum Less Than k ===

You are given a 0-indexed integer matrix grid and an integer k.
Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.

Example 1:
    Input: grid = [[7,6,3],[6,6,1]], k = 18
    Output: 4
    Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.
Example 2:
    Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
    Output: 6
    Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= n, m <= 1000
    4. 0 <= grid[i][j] <= 1000
    5. 1 <= k <= 109
'''
# === 1591ms && 65.8MB === #
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        s = [[0 for _ in range(m+1)] for _ in range(n+1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                s[i+1][j+1] = grid[i][j] + s[i+1][j] + s[i][j+1] - s[i][j]
                if s[i+1][j+1] <= k:
                    ans += 1
                else:
                    break
        return ans