'''
=== 2503. Maximum Number of Points From Grid Queries ===

You are given an m x n integer matrix grid and an array queries of size k.
Find an array answer of size k such that for each integer queres[i] you start in the top left cell of the matrix and repeat the following process:
    - If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
    - Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
Return the resulting array answer.

Example 1:
    Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
    Output: [5,8,1]
    Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:
    Input: grid = [[5,2,1],[1,1,2]], queries = [3]
    Output: [0]
    Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 2 <= m, n <= 1000
    4. 4 <= m * n <= 105
    5. k == queries.length
    6. 1 <= k <= 104
    7. 1 <= grid[i][j], queries[i] <= 106
'''
# === 2829ms && 42.1MB === #
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(grid), len(grid[0])
        seen = {(0, 0)}
        q = [(grid[0][0], 0, 0)]
        _max = grid[0][0]
        ans = {}
        cnt = 0
        while q:
            v, i, j = heapq.heappop(q)
            cnt += 1
            if v > _max:
                _max = v
            ans[_max] = cnt
            if i-1 >= 0 and (i-1, j) not in seen:
                heapq.heappush(q, (grid[i-1][j], i-1, j))
                seen.add((i-1, j))
            if i+1 < n and (i+1, j) not in seen:
                heapq.heappush(q, (grid[i+1][j], i+1, j))
                seen.add((i+1, j))
            if j-1 >= 0 and (i, j-1) not in seen:
                heapq.heappush(q, (grid[i][j-1], i, j-1))
                seen.add((i, j-1))
            if j+1 < m and (i, j+1) not in seen:
                heapq.heappush(q, (grid[i][j+1], i, j+1))
                seen.add((i, j+1))
        
        ans = sorted(ans.items())
        n = len(ans)
        
        def query(q):
            idx = bisect.bisect_left(ans, (q, 0))
            if idx == 0:
                return 0
            else:
                return ans[idx-1][1]
            
        return [query(q) for q in queries]
            
                