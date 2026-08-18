'''
=== 3195. Find the Minimum Area to Cover All Ones I ===

You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.
Return the minimum possible area of the rectangle.

Example 1:
    Input: grid = [[0,1,0],[1,0,1]]
    Output: 6
    Explanation:
    The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.
Example 2:
    Input: grid = [[0,0],[1,0]]
    Output: 1
    Explanation:
    The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

Constraints:
    1. 1 <= grid.length, grid[i].length <= 1000
    2. grid[i][j] is either 0 or 1.
    3. The input is generated such that there is at least one 1 in grid.
'''
# === 2844ms && 46.2MB === #
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        lb, rb = m, -1
        ub, db = n, -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    lb = min(lb, j)
                    rb = max(rb, j)
                    ub = min(ub, i)
                    db = max(db, i)
        return (rb-lb+1) * (db-ub+1)