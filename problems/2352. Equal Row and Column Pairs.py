'''
=== 2352. Equal Row and Column Pairs ===

Given a 0-indexed n x n integer matrix grid, return the number of pairs (Ri, Cj) such that row Ri and column Cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e. an equal array).

Example 1:
    Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
    Output: 1
    Explanation: There is 1 equal row and column pair:
    - (Row 2, Column 1): [2,7,7]
Example 2:
    Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    Output: 3
    Explanation: There are 3 equal row and column pairs:
    - (Row 0, Column 0): [3,1,2,2]
    - (Row 2, Column 2): [2,4,2,2]
    - (Row 3, Column 2): [2,4,2,2]
 
Constraints:
    1. n == grid.length == grid[i].length
    2. 1 <= n <= 200
    3. 1 <= grid[i][j] <= 105
'''
# === 809ms && 18.9MB === #
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = defaultdict(int)
        cols = defaultdict(int)
        for i in range(n):
            rows[tuple(grid[i])] += 1
            cols[tuple([x[i] for x in grid])] += 1
        # print(rows, cols)
        res = 0
        for row in rows:
            res += rows[row] * cols[row]
        return res