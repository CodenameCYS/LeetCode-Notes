'''
=== 1584. Min Cost to Connect All Points ===

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:
    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20
    Explanation:
    We can connect the points as shown above to get the minimum cost of 20.
    Notice that there is a unique path between every pair of points.
Example 2:
    Input: points = [[3,12],[-2,5],[-4,1]]
    Output: 18
Example 3:
    Input: points = [[0,0],[1,1],[1,0],[-1,1]]
    Output: 4
Example 4:
    Input: points = [[-1000000,-1000000],[1000000,1000000]]
    Output: 4000000
Example 5:
    Input: points = [[0,0]]
    Output: 0
 
Constraints:
    1. 1 <= points.length <= 1000
    2. -106 <= xi, yi <= 106
    3. All pairs (xi, yi) are distinct.
'''
# === 2192ms && 105.6MB === #
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = [[abs(x[0] - y[0]) + abs(x[1] - y[1]) for y in points] for x in points]
        distances = sorted((distances[x][y], x, y) for x in range(n-1) for y in range(x+1, n))
        ans = 0
        have_connected = [set([i]) for i in range(n)]
        for d, x, y in distances:
            if any(x in s and y in s for s in have_connected):
                continue
            s1 = -1
            s2 = -1
            for j, s in enumerate(have_connected):
                if x in s:
                    s1 = j
                if y in s:
                    s2 = j
            if s1 > s2:
                s1, s2 = s2, s1
            have_connected.append(have_connected[s1] | have_connected[s2])
            have_connected.pop(s2)
            have_connected.pop(s1)
            ans += d
            if len(have_connected) == 1:
                break
        return ans