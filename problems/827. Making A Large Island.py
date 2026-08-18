'''
=== 827. Making A Large Island ===

In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:
    Input: [[1, 0], [0, 1]]
    Output: 3
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:
    Input: [[1, 1], [1, 0]]
    Output: 4
    Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:
    Input: [[1, 1], [1, 1]]
    Output: 4
    Explanation: Can't change any 0 to 1, only one island with area = 4.
 
Notes:
    1. 1 <= grid.length = grid[0].length <= 50.
    2. 0 <= grid[i][j] <= 1.
'''
# === 6228ms(5.08%) && 14.1MB(100%) === #
class Solution:
    def get_island_size(self, grid, x0, y0):
        have_seen = {(x0, y0)}
        stack = [(x0, y0)]
        ans = 0
        n = len(grid)
        m = len(grid[0])
        while stack != []:
            x, y = stack.pop()
            ans += 1
            if x > 0 and grid[x-1][y] == 1 and (x-1, y) not in have_seen:
                stack.append((x-1, y))
                have_seen.add((x-1, y))
            if y > 0 and grid[x][y-1] == 1 and (x, y-1) not in have_seen:
                stack.append((x, y-1))
                have_seen.add((x, y-1))
            if x < n-1 and grid[x+1][y] == 1 and (x+1, y) not in have_seen:
                stack.append((x+1, y))
                have_seen.add((x+1, y))
            if y < m-1 and grid[x][y+1] == 1 and (x, y+1) not in have_seen:
                stack.append((x, y+1))
                have_seen.add((x, y+1))
        return ans
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    ans = max(ans, self.get_island_size(grid, i, j))
                    grid[i][j] = 0
        if ans == 0:
            ans = len(grid) * len(grid[0])
        return ans