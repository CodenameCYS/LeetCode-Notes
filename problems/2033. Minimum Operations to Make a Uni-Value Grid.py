'''
=== 2033. Minimum Operations to Make a Uni-Value Grid ===

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
A uni-value grid is a grid where all the elements of it are equal.
Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

Example 1:
    Input: grid = [[2,4],[6,8]], x = 2
    Output: 4
    Explanation: We can make every element equal to 4 by doing the following: 
    - Add x to 2 once.
    - Subtract x from 6 once.
    - Subtract x from 8 twice.
    A total of 4 operations were used.
Example 2:
    Input: grid = [[1,5],[2,3]], x = 1
    Output: 5
    Explanation: We can make every element equal to 3.
Example 3:
    Input: grid = [[1,2],[3,4]], x = 2
    Output: -1
    Explanation: It is impossible to make every element equal.
    
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 105
    4. 1 <= m * n <= 105
    5. 1 <= x, grid[i][j] <= 104
'''
# === 1488ms && 49.1MB === #
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        cnt = defaultdict(int)
        for row in grid:
            for k in row:
                cnt[k] += 1
        y0 = min(cnt.keys())
        if any((y - y0) % x != 0 for y in cnt.keys()):
            return -1
        nums = sorted([((k-y0)//x, v) for k, v in cnt.items()])
        # print(nums)
        n, s = len(nums), sum(k*v for k, v in nums)
        vlist = [it[0] for it in nums]
        nlist = list(accumulate([it[1] for it in nums]))
        # print(vlist, nlist)
        res = s
        # print(s)
        for i in range(1, n):
            s = s - (nlist[-1] - nlist[i-1]) * (vlist[i] - vlist[i-1]) + nlist[i-1] * (vlist[i] - vlist[i-1])
            res = min(res, s)
            # print(s)
        # print("=" * 10)
        return res