'''
=== 3276. Select Cells in Grid With Maximum Score ===

You are given a 2D matrix grid consisting of positive integers.
You have to select one or more cells from the matrix such that the following conditions are satisfied:
    - No two selected cells are in the same row of the matrix.
    - The values in the set of selected cells are unique.
Your score will be the sum of the values of the selected cells.
Return the maximum score you can achieve.

Example 1:
    Input: grid = [[1,2,3],[4,3,2],[1,1,1]]
    Output: 8
    Explanation:
    We can select the cells with values 1, 3, and 4 that are colored above.
Example 2:
    Input: grid = [[8,7,6],[8,3,2]]
    Output: 15
    Explanation:
    We can select the cells with values 7 and 8 that are colored above.

Constraints:
    1. 1 <= grid.length, grid[i].length <= 10
    2. 1 <= grid[i][j] <= 100
'''
# === 555ms && 121.9MB === #
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        elems = [(grid[i][j], i, j) for i in range(n) for j in range(m)]
        elems = sorted(elems, reverse=True)
        if n == 1:
            return elems[0][0]
        N = len(elems)
        
        @lru_cache(None)
        def dp(idx, status):
            if idx >= N or status == 1023:
                return 0
            x, i, j = elems[idx]
            if status & (1 << i) > 0:
                return dp(idx+1, status)
            nxt = idx+1
            while nxt < N and elems[nxt][0] == x:
                nxt += 1
            return max(x + dp(nxt, status | (1<<i)), dp(idx+1, status))
        
        return dp(0, 0)