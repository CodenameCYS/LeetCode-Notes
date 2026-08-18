'''
=== 3242. Design Neighbor Sum Service ===

You are given a n x n 2D array grid containing distinct elements in the range [0, n2 - 1].
Implement the neighborSum class:
    - neighborSum(int [][]grid) initializes the object.
    - int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, that is either to the top, left, right, or bottom of value in grid.
    - int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value, that is either to the top-left, top-right, bottom-left, or bottom-right of value in grid.

Example 1:
    Input:
    ["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]
    [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]
    Output: [null, 6, 16, 16, 4]
    Explanation:
    The adjacent neighbors of 1 are 0, 2, and 4.
    The adjacent neighbors of 4 are 1, 3, 5, and 7.
    The diagonal neighbors of 4 are 0, 2, 6, and 8.
    The diagonal neighbor of 8 is 4.
Example 2:
    Input:
    ["neighborSum", "adjacentSum", "diagonalSum"]
    [[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]
    Output: [null, 23, 45]
    Explanation:
    The adjacent neighbors of 15 are 0, 10, 7, and 6.
    The diagonal neighbors of 9 are 4, 12, 14, and 15.
 
Constraints:
    1. 3 <= n == grid.length == grid[0].length <= 10
    2. 0 <= grid[i][j] <= n2 - 1
    3. All grid[i][j] are distinct.
    4. value in adjacentSum and diagonalSum will be in the range [0, n2 - 1].
    5. At most 2 * n2 calls will be made to adjacentSum and diagonalSum.
'''
# === 162ms && 16.8MB === #
class neighborSum:

    def __init__(self, grid: List[List[int]]):
        n = len(grid)
        self.adjacent_sum = defaultdict(int)
        self.diagonal_sum = defaultdict(int)
        
        def _adjacent_sum(i, j):
            ans = 0
            if i-1 >= 0:
                ans += grid[i-1][j]
            if i+1 < n:
                ans += grid[i+1][j]
            if j-1 >= 0:
                ans += grid[i][j-1]
            if j+1 < n:
                ans += grid[i][j+1]
            return ans
        
        def _diagonal_sum(i, j):
            ans = 0
            if i-1 >= 0 and j-1 >= 0:
                ans += grid[i-1][j-1]
            if i-1 >= 0 and j+1 < n:
                ans += grid[i-1][j+1]
            if i+1 < n and j-1 >= 0:
                ans += grid[i+1][j-1]
            if i+1 < n and j+1 < n:
                ans += grid[i+1][j+1]
            return ans
        
        for i in range(n):
            for j in range(n):
                self.adjacent_sum[grid[i][j]] = _adjacent_sum(i, j)
                self.diagonal_sum[grid[i][j]] = _diagonal_sum(i, j)
        return

    def adjacentSum(self, value: int) -> int:
        return self.adjacent_sum[value]

    def diagonalSum(self, value: int) -> int:
        return self.diagonal_sum[value]


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)