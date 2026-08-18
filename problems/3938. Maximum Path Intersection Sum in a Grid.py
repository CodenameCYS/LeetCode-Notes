'''
=== 3938. Maximum Path Intersection Sum in a Grid ===

You are given an m x n integer matrix grid.
Two players move across the grid:
    - Player 1 starts at the top-left cell (0, 0) and can move only right or down. Their destination is the bottom-right cell (m - 1, n - 1).
    - Player 2 starts at the bottom-left cell (m - 1, 0) and can move only right or up. Their destination is the top-right cell (0, n - 1).
Each player must choose a valid path from their respective starting cell to their destination.
A cell is called shared if it belongs to both chosen paths.
Return an integer denoting the maximum possible sum of values of all shared cells.

Example 1:​​​​​​​​​​​​​​​​​​​​​
    Input: grid = [[1,2,0,-3],[1,-2,1,0],[-4,2,-1,3],[3,-3,3,-2],[-1,-5,0,1]]
    Output: 4
    Explanation:
    The diagram shows one optimal choice of paths.
    Player 1 follows the red/purple path from the top-left cell to the bottom-right cell:
    (0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3) → (3, 3) → (4, 3)
    Player 2 follows the blue/purple path from the bottom-left cell to the top-right cell:
    (4, 0) → (4, 1) → (3, 1) → (2, 1) → (2, 2) → (2, 3) → (1, 3) → (0, 3)
    The shared cells are (2, 1), (2, 2), and (2, 3).
    The sum is 2 + (-1) + 3 = 4, which is the maximum possible sum.
Example 2:
    Input: grid = [[4,-2,-3],[-1,-3,-1],[-4,2,-1]]
    Output: 3
    Explanation:
    One optimal pair of paths is shown in the diagram.
    Player 1 follows the red/purple path:
    (0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)
    Player 2 follows the blue/purple path:
    (2, 0) → (1, 0) → (0, 0) → (0, 1) → (0, 2)
    The shared cells are (0, 0) and (1, 0).
    The sum is 4 + (-1) = 3, which is the maximum possible.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 2 <= m, n <= 1000
    4. 4 <= m * n <= 5 * 105
    5. -100 <= grid[i][j] <= 100
'''
# === 1209ms && 59.69MB === #
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        def get_max_score(nums, is_edge):
            n = len(nums)
            if n == 2:
                return sum(nums)
            cumsum = list(accumulate(nums, initial = 0))
            rmax = [x for x in cumsum[1:]]
            for i in range(n-1, 0, -1):
                rmax[i-1] = max(rmax[i], cumsum[i])
            if is_edge:
                return max(rmax[i+1]-cumsum[i] for i in range(n-1))
            else:
                return max(max(rmax[i]-cumsum[i] for i in range(1, n-1)), rmax[1]-cumsum[0], rmax[n-1]-cumsum[n-2])

        n, m = len(grid), len(grid[0])
        cols = [[grid[i][j] for i in range(n)] for j in range(m)]
        return max(
            max(get_max_score(row, i==0 or i==n-1) for i, row in enumerate(grid)),
            max(get_max_score(col, i==0 or i==m-1) for i, col in enumerate(cols)),
        )


        