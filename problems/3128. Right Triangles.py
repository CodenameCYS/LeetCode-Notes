'''
=== 3128. Right Triangles ===

You are given a 2D boolean matrix grid.
Return an integer that is the number of right triangles that can be made with the 3 elements of grid such that all of them have a value of 1.

Note:
    - A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another element and in the same column with the third element. The 3 elements do not have to be next to each other.
 

Example 1:
    Input: grid = [[0,1,0],[0,1,1],[0,1,0]]
    Output: 2
    Explanation:
    There are two right triangles.
Example 2:
    Input: grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
    Output: 0
    Explanation:
    There are no right triangles.
Example 3:
    Input: grid = [[1,0,1],[1,0,0],[1,0,0]]
    Output: 2
    Explanation:
    There are two right triangles.

Constraints:
    1. 1 <= grid.length <= 1000
    2. 1 <= grid[i].length <= 1000
    3. 0 <= grid[i][j] <= 1
'''
# === 2234ms && 37.7MB === #
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rows = [sum(line) for line in grid]
        cols = [sum([grid[i][j] for i in range(n)]) for j in range(m)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                ans += (rows[i]-1) * (cols[j]-1)
        return ans
        