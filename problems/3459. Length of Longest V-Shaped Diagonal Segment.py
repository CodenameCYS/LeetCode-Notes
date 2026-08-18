'''
=== 3459. Length of Longest V-Shaped Diagonal Segment ===

You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.
A V-shaped diagonal segment is defined as:
    - The segment starts with 1.
    - The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
    - The segment:
        - Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
        - Continues the sequence in the same diagonal direction.
        - Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.
Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

Example 1:
    Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
    Output: 5
    Explanation:
    The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).
Example 2:
    Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
    Output: 4
    Explanation:
    The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).
Example 3:
    Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
    Output: 5
    Explanation:
    The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).
Example 4:
    Input: grid = [[1]]
    Output: 1
    Explanation:
    The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

Constraints:
    1. n == grid.length
    2. m == grid[i].length
    3. 1 <= n, m <= 500
    4. grid[i][j] is either 0, 1 or 2.
'''
# === 10677ms && 186.3MB === #
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        next_direction = {
            (1, 1): (-1, 1),
            (1, -1): (1, 1),
            (-1, 1): (-1, -1),
            (-1, -1): (1, -1)
        }

        @lru_cache(None)
        def dp(i, j, turn, dx, dy):
            if turn == 0:
                ans = 1
                while 0 <= i+dy < n and 0 <= j+dx < m and grid[i+dy][j+dx] == 2-grid[i][j]:
                    ans += 1
                    i, j = i+dy, j+dx
                return ans
            if grid[i][j] == 1:
                ans = 1
                for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    if 0 <= i+dy < n and 0 <= j+dx < m and grid[i+dy][j+dx] == 2:
                        ans = max(ans, 1 + dp(i+dy, j+dx, 1, dx, dy))
                return ans
            
            ans = 1
            if 0 <= i+dy < n and 0 <= j+dx < m and grid[i+dy][j+dx] == 2-grid[i][j]:
                ans = max(ans, 1 + dp(i+dy, j+dx, 1, dx, dy))
            dx, dy = next_direction[(dx, dy)]
            if 0 <= i+dy < n and 0 <= j+dx < m and grid[i+dy][j+dx] == 2-grid[i][j]:
                ans = max(ans, 1 + dp(i+dy, j+dx, 0, dx, dy))
            return ans
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, dp(i, j, 1, 1, 1))
                    if ans == max(min(n, 2*m-1), min(m, 2*n-1)):
                        break
        return ans
    
# === 8412ms && 156MB === #
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        next_direction = {
            (1, 1): (-1, 1),
            (1, -1): (1, 1),
            (-1, 1): (-1, -1),
            (-1, -1): (1, -1)
        }

        @lru_cache(None)
        def dp(i, j, turn, dx, dy):
            if turn == 0:
                ans = 1
                while 0 <= i+dy < n and 0 <= j+dx < m and grid[i+dy][j+dx] == 2-grid[i][j]:
                    ans += 1
                    i, j = i+dy, j+dx
                return ans
            if grid[i][j] == 1:
                ans = 1
                for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    if 0 <= i+dy < n and 0 <= j+dx < m and grid[i+dy][j+dx] == 2:
                        ans = max(ans, 1 + dp(i+dy, j+dx, 1, dx, dy))
                return ans
            
            ans = 1
            if 0 <= i+dy < n and 0 <= j+dx < m and grid[i+dy][j+dx] == 2-grid[i][j]:
                ans = max(ans, 1 + dp(i+dy, j+dx, 1, dx, dy))
            dx, dy = next_direction[(dx, dy)]
            if 0 <= i+dy < n and 0 <= j+dx < m and grid[i+dy][j+dx] == 2-grid[i][j]:
                ans = max(ans, 1 + dp(i+dy, j+dx, 0, dx, dy))
            return ans
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if ans >= max(min(n-i+1, m-j+m), min(i+1, j+m), min(i+n, m-j+1), min(n-i+n, j+1)):
                        continue
                    ans = max(ans, dp(i, j, 1, 1, 1))
                    if ans == max(min(n, 2*m-1), min(m, 2*n-1)):
                        break
        return ans