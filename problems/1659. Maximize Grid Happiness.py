'''
=== 1659. Maximize Grid Happiness ===

You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and there are two types of people: introverts and extroverts. There are introvertsCount introverts and extrovertsCount extroverts.
You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you do not have to have all the people living in the grid.
The happiness of each person is calculated as follows:
    - Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
    - Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.
The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.

Example 1:
    Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
    Output: 240
    Explanation: Assume the grid is 1-indexed with coordinates (row, column).
    We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
    - Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
    - Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
    - Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
    The grid happiness is 120 + 60 + 60 = 240.
    The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.
Example 2:
    Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
    Output: 260
    Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
    - Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
    - Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
    - Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
    The grid happiness is 90 + 80 + 90 = 260.
Example 3:
    Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
    Output: 240
 
Constraints:
    1. 1 <= m, n <= 5
    2. 0 <= introvertsCount, extrovertsCount <= min(m * n, 6)
'''
# === 4524ms && 24.3MB === #
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        if m < n:
            return self.getMaxGridHappiness(n, m, introvertsCount, extrovertsCount)
        
        if n >= 5:
            bonus = {0:0, 1:0, 2:40, 3:80, 4:160, 5:200, 6:280}
            return 120 * introvertsCount + 40 * extrovertsCount + bonus[extrovertsCount]
        
        @lru_cache(None)
        def dp(r, intro, extro, prev):
            if r >= m:
                return 0
            ans = 0
            for row in itertools.product(range(3), repeat=n):
                _intro = row.count(1)
                _extro = row.count(2)
                if _intro > intro or _extro > extro:
                    continue
                score = 0
                for i in range(n):
                    if row[i] == 0:
                        continue
                    elif row[i] == 1:
                        score += 120
                        if i-1 >= 0 and row[i-1] != 0:
                            score -= 30
                        if i+1 < n and row[i+1] != 0:
                            score -= 30
                        if prev[i] == 1:
                            score -= 60
                        elif prev[i] == 2:
                            score -= 10
                    else:
                        score += 40
                        if i-1 >= 0 and row[i-1] != 0:
                            score += 20
                        if i+1 < n and row[i+1] != 0:
                            score += 20
                        if prev[i] == 1:
                            score -= 10
                        elif prev[i] == 2:
                            score += 40
                score += dp(r+1, intro - _intro, extro - _extro, tuple(row))
                ans = max(ans, score)
            return ans

        return dp(0, introvertsCount, extrovertsCount, tuple([0] * n))

# === 916ms && 14.2MB === #
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        score = 0
        
        def get_score(r, c):
            nonlocal grid
            if grid[r][c] == 1:
                score = 120
                if r-1 >= 0:
                    if grid[r-1][c] == 1:
                        score -= 60
                    elif grid[r-1][c] == 2:
                        score -= 10
                if c-1 >= 0:
                    if grid[r][c-1] == 1:
                        score -= 60
                    elif grid[r][c-1] == 2:
                        score -= 10
            else:
                score = 40
                if r-1 >= 0:
                    if grid[r-1][c] == 1:
                        score -= 10
                    elif grid[r-1][c] == 2:
                        score += 40
                if c-1 >= 0:
                    if grid[r][c-1] == 1:
                        score -= 10
                    elif grid[r][c-1] == 2:
                        score += 40
            return score
        
        def dfs(r, c, intro, extro, _score):
            nonlocal grid, score
            if c >= n:
                dfs(r+1, 0, intro, extro, _score)
                return
            if r >= m or (intro == 0 and extro == 0):
                score = max(_score, score)
                return
            if _score + 120 * (intro + extro) < score:
                return
            if intro > 0:
                grid[r][c] = 1
                dfs(r, c+1, intro-1, extro, _score + get_score(r,c))
                grid[r][c] = 0
            if extro > 0:
                grid[r][c] = 2
                dfs(r, c+1, intro, extro-1, _score + get_score(r,c))
                grid[r][c] = 0
            if (r > 0 and grid[r-1][c] != 0) or (c > 0 and grid[r][c-1] != 0):
                dfs(r, c+1, intro, extro, _score)
            return
        
        dfs(0, 0, introvertsCount, extrovertsCount, 0)
        return score