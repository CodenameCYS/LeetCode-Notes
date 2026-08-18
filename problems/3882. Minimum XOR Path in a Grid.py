'''
=== 3882. Minimum XOR Path in a Grid ===

You are given a 2D integer array grid of size m * n.
You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
At each step, you may move either right or down.
The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.
Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

Example 1:
    Input: grid = [[1,2],[3,4]]
    Output: 6
    Explanation:
    There are two valid paths:
    (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
    (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
    The minimum XOR value among all valid paths is 6.
Example 2:
    Input: grid = [[6,7],[5,8]]
    Output: 9
    Explanation:
    There are two valid paths:
    (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
    (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11
    The minimum XOR value among all valid paths is 9.
Example 3:
    Input: grid = [[2,7,5]]
    Output: 0
    Explanation:
    There is only one valid path:
    (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0
    The XOR value of this path is 0, which is the minimum possible.

Constraints:
    1. 1 <= m == grid.length <= 1000
    2. 1 <= n == grid[i].length <= 1000
    3. m * n <= 1000
    4. 0 <= grid[i][j] <= 1023​
'''
# === 2716ms && 113.52MB === #
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        seen = {(0, 0, grid[0][0])}
        q = [(grid[0][0], 0, 0)]
        ans = math.inf
        while q:
            val, i, j = heapq.heappop(q)
            if i == n-1 and j == m-1:
                ans = min(ans, val)
                if ans == 0:
                    break
            if i+1 < n and (i+1, j, val ^ grid[i+1][j]) not in seen:
                seen.add((i+1, j, val ^ grid[i+1][j]))
                heapq.heappush(q, (val ^ grid[i+1][j], i+1, j))
            if j+1 < m and (i, j+1, val ^ grid[i][j+1]) not in seen:
                seen.add((i, j+1, val ^ grid[i][j+1]))
                heapq.heappush(q, (val ^ grid[i][j+1], i, j+1))
        return ans
                


