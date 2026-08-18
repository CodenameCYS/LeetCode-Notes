'''
=== 3548. Equal Sum Grid Partition II ===

You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
    - Each of the two resulting sections formed by the cut is non-empty.
    - The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
    - If a cell is discounted, the rest of the section must remain connected.
Return true if such a partition exists; otherwise, return false.
Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

Example 1:
    Input: grid = [[1,4],[2,3]]
    Output: true
    Explanation:
    A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.
Example 2:
    Input: grid = [[1,2],[3,4]]
    Output: true
    Explanation:
    A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
    By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.
Example 3:
    Input: grid = [[1,2,4],[2,3,5]]
    Output: false
    Explanation:
    A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
    By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.
Example 4:
    Input: grid = [[4,1,8],[3,2,6]]
    Output: false
    Explanation:
    No valid cut exists, so the answer is false.

Constraints:
    1. 1 <= m == grid.length <= 105
    2. 1 <= n == grid[i].length <= 105
    3. 2 <= m * n <= 105
    4. 1 <= grid[i][j] <= 105
'''
# === 847ms && 57.9MB === #
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # print("=" * 10)
        n, m = len(grid), len(grid[0])
        cnt = defaultdict(int)
        tot = 0
        for i in range(n):
            for j in range(m):
                cnt[grid[i][j]] += 1
                tot += grid[i][j]
        # print(tot)
                
        _cnt = defaultdict(int)
        _tot = 0
        for i in range(n-1):
            for j in range(m):
                _cnt[grid[i][j]] += 1
                _tot += grid[i][j]

            delta = 2 * _tot - tot
            # print(f"row={i}, delta={delta}")
            if delta == 0:
                return True
            elif delta > 0:
                if _cnt[delta] > 0 and i > 0 and m > 1:
                    return True
                elif i > 0 and m == 1 and (grid[0][0] == delta or grid[i][0] == delta):
                    return True
                elif i == 0 and (grid[0][0] == delta or grid[0][-1] == delta):
                    return True
            else:
                if cnt[-delta] - _cnt[-delta] > 0 and i < n-2 and m > 1:
                    return True
                elif i < n-2 and m == 1 and (grid[-1][0] == -delta or grid[i+1][0] == -delta):
                    return True
                elif i == n-2 and (grid[-1][0] == -delta or grid[-1][-1] == -delta):
                    return True
        
        _cnt = defaultdict(int)
        _tot = 0
        for j in range(m-1):
            for i in range(n):
                _cnt[grid[i][j]] += 1
                _tot += grid[i][j]

            delta = 2 * _tot - tot
            # print(f"col={j}, delta={delta}")
            if delta == 0:
                return True
            elif delta > 0:
                if _cnt[delta] > 0 and j > 0 and n > 1:
                    return True
                elif j > 0 and n == 1 and (grid[0][0] == delta or grid[0][j] == delta):
                    return True
                elif j == 0 and (grid[0][0] == delta or grid[-1][0] == delta):
                    return True
            else:
                if cnt[-delta] - _cnt[-delta] > 0 and j < m-2 and n > 1:
                    return True
                elif j < m-2 and n == 1 and (grid[0][-1] == -delta or grid[0][j+1] == -delta):
                    return True
                elif j == m-2 and (grid[0][-1] == -delta or grid[-1][-1] == -delta):
                    return True
        return False
                    