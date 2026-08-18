'''
=== 2245. Maximum Trailing Zeros in a Cornered Path ===

You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.
A cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.
The product of a path is defined as the product of all the values in the path.
Return the maximum number of trailing zeros in the product of a cornered path found in grid.

Note:
    - Horizontal movement means moving in either the left or right direction.
    - Vertical movement means moving in either the up or down direction.
 
Example 1:
    Input: grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
    Output: 3
    Explanation: The grid on the left shows a valid cornered path.
    It has a product of 15 * 20 * 6 * 1 * 10 = 18000 which has 3 trailing zeros.
    It can be shown that this is the maximum trailing zeros in the product of a cornered path.
    The grid in the middle is not a cornered path as it has more than one turn.
    The grid on the right is not a cornered path as it requires a return to a previously visited cell.
Example 2:
    Input: grid = [[4,3,2],[7,6,1],[8,8,8]]
    Output: 0
    Explanation: The grid is shown in the figure above.
    There are no cornered paths in the grid that result in a product with a trailing zero.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 105
    4. 1 <= m * n <= 105
    5. 1 <= grid[i][j] <= 1000
'''
# === 8274ms && 57.6MB === #
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        twos = [[0 for _ in range(m+1)] for _ in range(n+1)]
        fives = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                x = grid[i][j]
                cnt2, cnt5 = 0, 0
                while x % 2 == 0:
                    x = x // 2
                    cnt2 += 1
                while x % 5 == 0:
                    x = x // 5
                    cnt5 += 1
                twos[i+1][j+1] = twos[i+1][j] + twos[i][j+1] - twos[i][j] + cnt2
                fives[i+1][j+1] = fives[i+1][j] + fives[i][j+1] - fives[i][j] + cnt5
        
        def get_horionzal(matrix, row, i, j):
            if i > j:
                return 0
            return matrix[row+1][j+1] - matrix[row+1][i] - (matrix[row][j+1] - matrix[row][i])
        
        def get_vertical(matrix, col, i, j):
            if i > j:
                return 0
            return matrix[j+1][col+1] - matrix[i][col+1] - (matrix[j+1][col] - matrix[i][col])
        
        res = 0
        for i in range(n):
            for j in range(m):
                s1 = min(get_vertical(twos, j, 0, i-1) + get_horionzal(twos, i, 0, j), get_vertical(fives, j, 0, i-1) + get_horionzal(fives, i, 0, j))
                s2 = min(get_vertical(twos, j, i+1, n-1) + get_horionzal(twos, i, 0, j), get_vertical(fives, j, i+1, n-1) + get_horionzal(fives, i, 0, j))
                s3 = min(get_vertical(twos, j, 0, i-1) + get_horionzal(twos, i, j, m-1), get_vertical(fives, j, 0, i-1) + get_horionzal(fives, i, j, m-1))
                s4 = min(get_vertical(twos, j, i+1, n-1) + get_horionzal(twos, i, j, m-1), get_vertical(fives, j, i+1, n-1) + get_horionzal(fives, i, j, m-1))
                res = max(res, s1, s2, s3, s4)
        return res
                