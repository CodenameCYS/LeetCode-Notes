'''
=== 4046. Minimum Cost Path With At Most K Turns ===

You are given a 2D integer array grid of size m x n, where grid[i][j] represents the cost of visiting cell (i, j), and an integer k.
You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
From each cell, you may move one step in any of the four directions: up, down, left, or right.
The cost of a path is the sum of the values of all visited cells, including the starting and ending cells. If a cell is visited more than once, its value is included each time it is visited.
Return the minimum possible path cost to reach (m - 1, n - 1) using at most k turns. If no such path exists, return -1.
A turn occurs when the direction changes between two consecutive moves. For example, moving right and then down counts as one turn, while moving right and then right does not.

Example 1:
    Input: grid = [[2,7,3],[1,4,5]], k = 1
    Output: 12
    Explanation:
    An optimal path is (0, 0) → (1, 0) → (1, 1) → (1, 2). The moves are down, right, right.
    The direction changes from down to right once, so the path uses exactly k = 1 turn.
    The total path cost is 2 + 1 + 4 + 5 = 12.
Example 2:
    Input: grid = [[4,1,9],[3,2,5],[4,8,6]], k = 2
    Output: 20
    Explanation:​​​​​​​
    An optimal path is (0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2). The moves are down, right, right, down.
    The direction changes from down to right and from right to down, so the path uses exactly k = 2 turns.
    The total path cost is 4 + 3 + 2 + 5 + 6 = 20.
Example 3:
    Input: grid = [[1,9],[3,4]], k = 0
    Output: -1
    Explanation:
    It is impossible to reach (1, 1) using k = 0 turns. Thus, the answer is -1.
 
Constraints:
    1. 1 <= m == grid.length <= 75
    2. 1 <= n == grid[i].length <= 75
    3. 0 <= grid[i][j] <= 1000
    4. 0 <= k < min(m, n)
'''
DIRECTION = {
    "up": (1, 0),
    "down": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
# === 1503ms && 32.21MB === #
class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        q = []
        seen = {}

        def add_state(prev, turn, x, y, d):
            nonlocal q, seen
            # print(prev, turn, x, y, d)
            if x < 0 or x >= n or y < 0 or y >= m:
                return
            if turn > k:
                return
            cost = prev + grid[x][y]
            if (x, y, d) in seen and any(cost >= c and turn >= t for c, t in seen[(x,y,d)]):
                return
            if (x, y, d) not in seen:
                seen[(x, y, d)] = [(cost, turn)]
            else:
                seen[(x, y, d)].append((cost, turn))
            heapq.heappush(q, (cost, turn, x, y, d))
            return

        for d in ["up", "down", "left", "right"]:
            add_state(0, 0, 0, 0, d)

        while q:
            # print(q)
            # print("=" * 10)
            cost, turn, x, y, d = heapq.heappop(q)
            if x == n-1 and y == m-1:
                return cost
            for _d in ["up", "down", "left", "right"]:
                dx, dy = DIRECTION[_d]
                # print(_d, dx, dy)
                t = turn if _d == d else turn+1
                add_state(cost, t, x+dx, y+dy, _d)
        return -1