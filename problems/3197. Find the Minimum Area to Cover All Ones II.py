'''
=== 3197. Find the Minimum Area to Cover All Ones II === 

You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.
Return the minimum possible sum of the area of these rectangles.
Note that the rectangles are allowed to touch.

Example 1:
    Input: grid = [[1,0,1],[1,1,1]]
    Output: 5
    Explanation:
    The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
    The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
    The 1 at (1, 1) is covered by a rectangle of area 1.
Example 2:
    Input: grid = [[1,0,1,0],[0,1,0,1]]
    Output: 5
    Explanation:
    The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
    The 1 at (1, 1) is covered by a rectangle of area 1.
    The 1 at (1, 3) is covered by a rectangle of area 1.
    
Constraints:
    1. 1 <= grid.length, grid[i].length <= 30
    2. grid[i][j] is either 0 or 1.
    3. The input is generated such that there are at least three 1's in grid.
'''
# === 3981ms && 16.6MB === #
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        @lru_cache
        def solve1(i1, i2, j1, j2):
            imin = jmin = inf
            imax = jmax = -1
            for i in range(i1, i2):
                for j in range(j1, j2):
                    if grid[i][j]:
                        imin = min(imin, i)
                        imax = max(imax, i)
                        jmin = min(jmin, j)
                        jmax = max(jmax, j)
            if imax == -1:
                return 0
            return (imax - imin + 1) * (jmax - jmin + 1)
        
        def solve2(i1, i2, j1, j2):
            ans = inf
            for i in range(i1+1, i2):
                ans = min(ans, solve1(i1, i, j1, j2) + solve1(i, i2, j1, j2))
            for j in range(j1+1, j2):
                ans = min(ans, solve1(i1, i2, j1, j) + solve1(i1, i2, j, j2))
            return ans
        
        def solve3(i1, i2, j1, j2):
            ans = inf
            for i in range(i1+1, i2):
                ans = min(ans, solve2(i1, i, j1, j2) + solve1(i, i2, j1, j2))
                ans = min(ans, solve1(i1, i, j1, j2) + solve2(i, i2, j1, j2))
            for j in range(j1+1, j2):
                ans = min(ans, solve2(i1, i2, j1, j) + solve1(i1, i2, j, j2))
                ans = min(ans, solve1(i1, i2, j1, j) + solve2(i1, i2, j, j2))
            return ans
        
        return solve3(0, len(grid), 0, len(grid[0]))