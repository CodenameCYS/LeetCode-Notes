'''
=== 1631. Path With Minimum Effort ===

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:
    Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
    Output: 2
    Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
    This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:
    Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
    Output: 1
    Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:
    Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    Output: 0
    Explanation: This route does not require any effort.
 
Constraints:
    1. rows == heights.length
    2. columns == heights[i].length
    3. 1 <= rows, columns <= 100
    4. 1 <= heights[i][j] <= 106
'''
import heapq
# === 620ms && 16.5MB === #
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]):
        n = len(heights)
        m = len(heights[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        q = [(0,0,0)]
        have_seen = set()
        while q:
            c, i, j = heapq.heappop(q)
            if (i, j) in have_seen:
                continue
            else:
                have_seen.add((i, j))
            if i == n-1 and j == m-1:
                return c
            if i-1 >= 0 and (i-1, j) not in have_seen:
                heapq.heappush(q, (max(c, abs(heights[i][j] - heights[i-1][j])), i-1, j))
            if i+1 < n and (i+1, j) not in have_seen:
                heapq.heappush(q, (max(c, abs(heights[i][j] - heights[i+1][j])), i+1, j))
            if j-1 >= 0 and (i, j-1) not in have_seen:
                heapq.heappush(q, (max(c, abs(heights[i][j] - heights[i][j-1])), i, j-1))
            if j+1 < m and (i, j+1) not in have_seen:
                heapq.heappush(q, (max(c, abs(heights[i][j] - heights[i][j+1])), i, j+1))
        return 0