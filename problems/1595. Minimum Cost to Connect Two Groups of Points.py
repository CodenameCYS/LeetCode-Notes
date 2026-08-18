'''
=== 1595. Minimum Cost to Connect Two Groups of Points ===

You are given two groups of points where the first group has size1 points, the second group has size2 points, and size1 >= size2.
The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of connecting point i of the first group and point j of the second group. The groups are connected if each point in both groups is connected to one or more points in the opposite group. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.
Return the minimum cost it takes to connect the two groups.

Example 1:
    Input: cost = [[15, 96], [36, 2]]
    Output: 17
    Explanation: The optimal way of connecting the groups is:
    1--A
    2--B
    This results in a total cost of 17.
Example 2:
    Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
    Output: 4
    Explanation: The optimal way of connecting the groups is:
    1--A
    2--B
    2--C
    3--A
    This results in a total cost of 4.
    Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.
Example 3:
    Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
    Output: 10
 
Constraints:
    1. size1 == cost.length
    2. size2 == cost[i].length
    3. 1 <= size1, size2 <= 12
    4. size1 >= size2
    5. 0 <= cost[i][j] <= 100
'''
import math
# === 5036ms && 199.9MB === #
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        n = len(cost)
        m = len(cost[0])
        
        @lru_cache(None)
        def dfs(i, j, a, b):
            if i >= n:
                return 0 if all(y == 1 for y in b) else math.inf
            if j >= m:
                return dfs(i+1, 0, a, b) if a[i] == 1 else math.inf
            if a[i] == 1 and b[j] == 1:
                return dfs(i, j+1, a, b)
            else:
                anext, bnext = list(a), list(b)
                anext[i] = 1
                bnext[j] = 1
                anext, bnext = tuple(anext), tuple(bnext)
                return min(cost[i][j] + dfs(i, j+1, anext, bnext), dfs(i, j+1, a, b))
        
        a = tuple([0 for _ in range(n)])
        b = tuple([0 for _ in range(m)])
        return dfs(0, 0, a, b)