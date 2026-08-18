'''
=== 3873. Maximum Points Activated with One Addition ===

You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point. All coordinates in points are distinct.
If a point is activated, then all points that have the same x-coordinate or y-coordinate become activated as well.
Activation continues until no additional points can be activated.
You may add one additional point at any integer coordinate (x, y) not already present in points. Activation begins by activating this newly added point.
Return an integer denoting the maximum number of points that can be activated, including the newly added point.

Example 1:
    Input: points = [[1,1],[1,2],[2,2]]
    Output: 4
    Explanation:
    Adding and activating a point such as (1, 3) causes activations:
    (1, 3) shares x = 1 with (1, 1) and (1, 2) -> (1, 1) and (1, 2) become activated.
    (1, 2) shares y = 2 with (2, 2) -> (2, 2) becomes activated.
    Thus, the activated points are (1, 3), (1, 1), (1, 2), (2, 2), so 4 points in total. We can show this is the maximum activated.
Example 2:
    Input: points = [[2,2],[1,1],[3,3]]
    Output: 3
    Explanation:
    Adding and activating a point such as (1, 2) causes activations:
    (1, 2) shares x = 1 with (1, 1) -> (1, 1) becomes activated.
    (1, 2) shares y = 2 with (2, 2) -> (2, 2) becomes activated.
    Thus, the activated points are (1, 2), (1, 1), (2, 2), so 3 points in total. We can show this is the maximum activated.
Example 3:
    Input: points = [[2,3],[2,2],[1,1],[4,5]]
    Output: 4
    Explanation:
    Adding and activating a point such as (2, 1) causes activations:
    (2, 1) shares x = 2 with (2, 3) and (2, 2) -> (2, 3) and (2, 2) become activated.
    (2, 1) shares y = 1 with (1, 1) -> (1, 1) becomes activated.
    Thus, the activated points are (2, 1), (2, 3), (2, 2), (1, 1), so 4 points in total.

Constraints:
    1. 1 <= points.length <= 105
    2. points[i] = [xi, yi]
    3. -109 <= xi, yi <= 109
    4. points contains all distinct coordinates.
'''
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
        return
# === 2657ms && 87.41MB === #
class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        n = len(points)
        xaxis, yaxis = defaultdict(list), defaultdict(list)
        for i, (x, y) in enumerate(points):
            xaxis[x].append(i)
            yaxis[y].append(i)

        dsu = DSU(n)
        status = [0 for _ in range(n)]
        for i in range(n):
            if status[i] == 1:
                continue
            q = [i]
            seen = {i}
            seen_x = set()
            seen_y = set()
            while q:
                u = q.pop(0)
                dsu.union(u, i)
                status[u] = 1
                x, y = points[u]
                if x not in seen_x:
                    seen_x.add(x)
                    for v in xaxis[x]:
                        if v not in seen:
                            q.append(v)
                            seen.add(v)
                if y not in seen_y:
                    seen_y.add(y)
                    for v in yaxis[y]:
                        if v not in seen:
                            q.append(v)
                            seen.add(v)
        
        cnt = defaultdict(int)
        for u in range(n):
            cnt[dsu.find(u)] += 1
        groups = sorted(cnt.values())
        if len(groups) == 1:
            return n+1
        return groups[-1] + groups[-2] + 1
                

