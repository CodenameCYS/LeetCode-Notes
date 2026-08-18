'''
=== 3710. Maximum Partition Factor ===

You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.
The Manhattan distance between two points points[i] = [xi, yi] and points[j] = [xj, yj] is |xi - xj| + |yi - yj|.
Split the n points into exactly two non-empty groups. The partition factor of a split is the minimum Manhattan distance among all unordered pairs of points that lie in the same group.
Return the maximum possible partition factor over all valid splits.
Note: A group of size 1 contributes no intra-group pairs. When n = 2 (both groups size 1), there are no intra-group pairs, so define the partition factor as 0.

Example 1:
    Input: points = [[0,0],[0,2],[2,0],[2,2]]
    Output: 4
    Explanation:
    We split the points into two groups: {[0, 0], [2, 2]} and {[0, 2], [2, 0]}.
    In the first group, the only pair has Manhattan distance |0 - 2| + |0 - 2| = 4.
    In the second group, the only pair also has Manhattan distance |0 - 2| + |2 - 0| = 4.
    The partition factor of this split is min(4, 4) = 4, which is maximal.
Example 2:
    Input: points = [[0,0],[0,1],[10,0]]
    Output: 11
    Explanation:​​​​​​​
    We split the points into two groups: {[0, 1], [10, 0]} and {[0, 0]}.
    In the first group, the only pair has Manhattan distance |0 - 10| + |1 - 0| = 11.
    The second group is a singleton, so it contributes no pairs.
    The partition factor of this split is 11, which is maximal.

Constraints:
    1. 2 <= points.length <= 500
    2. points[i] = [xi, yi]
    3. -108 <= xi, yi <= 108
'''
# === 1184ms && 33.98MB === #
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0
        distances = []
        for i in range(n-1):
            for j in range(i+1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances.append((d, i, j))
        distances = sorted(distances)

        def is_possible(d):
            graph = defaultdict(list)
            for _d, u, v in distances:
                if _d >= d:
                    break
                graph[u].append(v)
                graph[v].append(u)
            nodes = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
            a, b = set(), set()
            for u in nodes:
                if u in a or u in b:
                    continue
                q = [(u, 0)]
                while q:
                    u, g = q.pop()
                    current, neighbor = (a, b) if g == 0 else (b, a)
                    if u in current:
                        continue
                    if u in neighbor:
                        return False
                    current.add(u)
                    for v in graph[u]:
                        if v in current:
                            return False
                        elif v in neighbor:
                            continue
                        q.append((v, 1-g))
            return True

        i, j = distances[0][0], distances[-1][0]+1
        while j > i+1:
            d = (i+j) // 2
            if is_possible(d):
                i = d
            else:
                j = d
        return i