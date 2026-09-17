'''
=== 4052. Cyclically Shift Rows and Columns ===

You are given an integer n, a 2D integer array grid of size n x n, and two integer arrays rowShift and colShift, each of length n, where:
    - rowShift[i] represents the number of positions to cyclically shift the ith row of grid to the left.
    - colShift[j] represents the number of positions to cyclically shift the jth column of grid upward.
First, cyclically shift each row according to rowShift, then cyclically shift each column of the resulting grid according to colShift.
Return the resulting grid after performing all the shifts.
A cyclic left shift of a row by k positions moves the element at column j to column (j - k + n) % n. All other rows remain unchanged.
A cyclic upward shift of a column by k positions moves the element at row i to row (i - k + n) % n. All other columns remain unchanged.

Example 1:
    Input: n = 2, grid = [[1,2],[3,4]], rowShift = [1,0], colShift = [0,1]
    Output: [[2,4],[3,1]]
    Explanation:
    The grid changes as follows:
Example 2:
    Input: n = 3, grid = [[1,2,3],[4,5,6],[7,8,9]], rowShift = [1,2,0], colShift = [2,2,1]
    Output: [[7,8,5],[2,3,9],[6,4,1]]
    Explanation:
    The grid changes as follows:

Constraints:
    1. 1 <= n == grid.length == grid[i].length <= 10
    2. 1 <= grid[i][j] <= 100
    3. rowShift.length == colShift.length == n
    4. 0 <= rowShift[i], colShift[i] < n
'''
# === 7ms && 19.55MB === #
class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        n, m = len(grid), len(grid[0])

        def row_shift(rid, k):
            row = grid[rid]
            k = k % m
            row = row[k:] + row[:k]
            grid[rid] = row
            return

        def col_shift(cid, k):
            col = [grid[i][cid] for i in range(n)]
            k = k % m
            col = col[k:] + col[:k]
            for i in range(n):
                grid[i][cid] = col[i]
            return

        for rid, k in enumerate(rowShift):
            row_shift(rid, k)
        for cid, k in enumerate(colShift):
            col_shift(cid, k)
        return grid