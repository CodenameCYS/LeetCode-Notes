'''
=== 1536. Minimum Swaps to Arrange a Binary Grid ===

Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
A grid is said to be valid if all the cells above the main diagonal are zeros.
Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

Example 1:
    Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
    Output: 3
Example 2:
    Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
    Output: -1
    Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:
    Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
    Output: 0
 
Constraints:
    1. n == grid.length
    2. n == grid[i].length
    3. 1 <= n <= 200
    4. grid[i][j] is 0 or 1
'''
# === 572ms && 14.6MB === #
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def get_zero_num(arr):
            return n - len("".join([str(i) for i in arr]).rstrip('0'))
        counter = [get_zero_num(arr) for arr in grid]
        ans = 0
        for i in range(n-1):
            idx = -1
            for j, count in enumerate(counter):
                if count >= n-1-i:
                    idx = j
                    break
            if idx == -1:
                return -1
            ans += idx
            counter.pop(idx)
        return ans
                    