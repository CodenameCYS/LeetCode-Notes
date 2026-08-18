'''
=== 3619. Count Islands With Total Value Divisible by K ===

You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).
The total value of an island is the sum of the values of all cells in the island.
Return the number of islands with a total value divisible by k.

Example 1:
    Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
    Output: 2
    Explanation:
    The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.
Example 2:
    Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
    Output: 6
    Explanation:
    The grid contains six islands, each with a total value that is divisible by 3.

Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 1000
    4. 1 <= m * n <= 105
    5. 0 <= grid[i][j] <= 106
    6. 1 <= k <= 106
'''
# === 311ms && 37.94MB === #
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        status = [[0 for _ in range(m)] for _ in range(n)]

        def dfs(i, j):
            nonlocal status
            s = [(i, j)]
            seen = {(i, j)}
            ans = 0
            while s:
                i, j = s.pop(0)
                # if status[i][j] != 0:
                #     continue
                ans += grid[i][j]
                status[i][j] = 1
                if i-1 >= 0 and grid[i-1][j] != 0 and status[i-1][j] == 0 and (i-1, j) not in seen:
                    seen.add((i-1, j))
                    s.append((i-1, j))
                if i+1 < n and grid[i+1][j] != 0 and status[i+1][j] == 0 and (i+1, j) not in seen:
                    seen.add((i+1, j))
                    s.append((i+1, j))
                if j-1 >= 0 and grid[i][j-1] != 0 and status[i][j-1] == 0 and (i, j-1) not in seen:
                    seen.add((i, j-1))
                    s.append((i, j-1))
                if j+1 < m and grid[i][j+1] != 0 and status[i][j+1] == 0 and (i, j+1) not in seen:
                    seen.add((i, j+1))
                    s.append((i, j+1))
            return ans

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and status[i][j] == 0:
                    val = dfs(i, j)
                    if val % k == 0:
                        ans += 1
        return ans