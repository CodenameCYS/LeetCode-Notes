'''
=== 2428. Maximum Sum of an Hourglass ===

You are given an m x n integer matrix grid.
We define an hourglass as a part of the matrix with the following form:
Return the maximum sum of the elements of an hourglass.
Note that an hourglass cannot be rotated and must be entirely contained within the matrix.

Example 1:
    Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
    Output: 30
    Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.
Example 2:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
    Output: 35
    Explanation: There is only one hourglass in the matrix, with the sum: 1 + 2 + 3 + 5 + 7 + 8 + 9 = 35.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 3 <= m, n <= 150
    4. 0 <= grid[i][j] <= 106
'''
# === 899ms && 17.3MB === #
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        s = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                s[i][j] = grid[i-1][j-1] + s[i-1][j] + s[i][j-1] - s[i-1][j-1]
        # print(s)
        
        def get_sum(i, j):
            return s[i+3][j+3] - s[i][j+3] - s[i+3][j] + s[i][j] - grid[i+1][j] - grid[i+1][j+2]
        
        return max([get_sum(i, j) for i in range(n-2) for j in range(m-2)])