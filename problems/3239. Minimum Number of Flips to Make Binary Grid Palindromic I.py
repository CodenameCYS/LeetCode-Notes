'''
=== 3239. Minimum Number of Flips to Make Binary Grid Palindromic I ===

You are given an m x n binary matrix grid.
A row or column is considered palindromic if its values read the same forward and backward.
You can flip any number of cells in grid from 0 to 1, or from 1 to 0.
Return the minimum number of cells that need to be flipped to make either all rows palindromic or all columns palindromic.

Example 1:
    Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
    Output: 2
    Explanation:
    Flipping the highlighted cells makes all the rows palindromic.
Example 2:
    Input: grid = [[0,1],[0,1],[0,0]]
    Output: 1
    Explanation:
    Flipping the highlighted cell makes all the columns palindromic.
Example 3:
    Input: grid = [[1],[0]]
    Output: 0
    Explanation:
    All rows are already palindromic.

Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m * n <= 2 * 105
    4. 0 <= grid[i][j] <= 1
'''
# === 2382ms && 70.1MB === #
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def fn(arr):
            ans = 0
            l = len(arr)
            for i in range(l // 2):
                if arr[i] != arr[l-1-i]:
                    ans += 1
            return ans
        
        ans1 = sum(fn(grid[i]) for i in range(n))
        
        cols = [[grid[i][j] for i in range(n)] for j in range(m)]
        ans2 = sum(fn(cols[j]) for j in range(m))
        return min(ans1, ans2)