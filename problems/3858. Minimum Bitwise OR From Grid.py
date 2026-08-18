'''
=== 3858. Minimum Bitwise OR From Grid ===

You are given a 2D integer array grid of size m x n.
You must select exactly one integer from each row of the grid.
Return an integer denoting the minimum possible bitwise OR of the selected integers from each row.

Example 1:
    Input: grid = [[1,5],[2,4]]
    Output: 3
    Explanation:
    Choose 1 from the first row and 2 from the second row.
    The bitwise OR of 1 | 2 = 3​​​​​​​, which is the minimum possible.
Example 2:
    Input: grid = [[3,5],[6,4]]
    Output: 5
    Explanation:
    Choose 5 from the first row and 4 from the second row.
    The bitwise OR of 5 | 4 = 5​​​​​​​, which is the minimum possible.
Example 3:
    Input: grid = [[7,9,8]]
    Output: 7
    Explanation:
    Choosing 7 gives the minimum bitwise OR.
 
Constraints:
    1. 1 <= m == grid.length <= 105
    2. 1 <= n == grid[i].length <= 105
    3. m * n <= 105
    4. 1 <= grid[i][j] <= 105
'''
# === 183ms && 41.98MB === #
class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(16, -1, -1):
            mask = ans | ((1 << i) - 1)  # mask 低于 i 的比特位全是 1
            if all(any((x | mask) == mask for x in row) for row in grid):
                ans = ans
            else:
                ans |= 1 << i
            print(bin(mask)[2:], ans)
        return ans