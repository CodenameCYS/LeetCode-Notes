'''
=== 3924. Minimum Threshold Path With Limited Heavy Edges ===

There is an undirected weighted graph with n nodes labeled from 0 to n - 1.
The graph is represented by a 2D integer array edges, where each edge edges[i] = [ui, vi, w​​​​​​​i] indicates that there is an undirected edge between nodes ui and vi with weight w​​​​​​​i.
You are also given integers source, target and k.
A threshold value determines whether an edge is considered light or heavy:
An edge is light if its weight is less than or equal to threshold.
An edge is heavy if its weight is greater than threshold.
A path from source to target is valid if it contains at most k heavy edges.
Return the minimum integer threshold such that at least one valid path exists from source to target. If no such path exists, return -1.

Example 1:​​​​​​​​​​​​​​
    Input: n = 6, edges = [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], source = 0, target = 3, k = 1
    Output: 4
    Explanation:
    The minimum threshold such that a path from node 0 to node 3 uses at most 1 heavy edge is 4.
    Light edges: [1, 2, 3], [3, 4, 4], [4, 5, 1], [1, 4, 2]
    Heavy edges: [0, 1, 5]
    A valid path is 0 → 1 → 4 → 3. It uses only 1 heavy edge ([0, 1, 5]), which satisfies the limit k = 1.
    Any smaller threshold would make it impossible to reach node 3 without exceeding 1 heavy edge.
Example 2:
    Input: n = 6, edges = [[0,1,3],[1,2,4],[3,4,5],[4,5,6]], source = 0, target = 4, k = 1
    Output: -1
    Explanation:
    There is no path from node 0 to node 4. Since the target cannot be reached, the output is -1.
Example 3:
    Input: n = 4, edges = [[0,1,2],[1,2,2],[2,3,2],[3,0,2]], source = 0, target = 0, k = 0
    Output: 0
    Explanation:
    The source and target are the same node. No edges need to be traversed, so the minimum threshold is 0.

Constraints:
    1. 1 <= n <= 103​​​​​​​
    2. 0 <= edges.length <= 103​​​​​​​
    3. edges[i] = [ui, vi, wi]
    4. 0 <= ui, vi​​​​​​​ <= n - 1
    5. 1 <= wi​​​​​​​ <= 109
    6. 0 <= source, target <= n - 1
    7. 0 <= k <= edges.length
'''
# === 658ms && 20.24MB === #
class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x != y:
            self.root[x] = y
        return True

class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if n == 1:
            return 0 if source == target == 0 else -1
        elif len(edges) == 0:
            return 0 if source == target else -1
        
        def is_possible(m):
            dsu = DSU(n)
            for u, v, w in edges:
                if w <= m:
                    dsu.union(u, v)
            src, tgt = dsu.find(source), dsu.find(target)
            # print(m, src, tgt)
            if src == tgt:
                return True
            
            graph = defaultdict(set)
            for u, v, w in edges:
                if w > m:
                    graph[dsu.find(v)].add(dsu.find(u))
                    graph[dsu.find(u)].add(dsu.find(v))
            graph = {k: list(v) for k, v in graph.items()}
            q = [(src, 0)]
            seen = {src}
            while q:
                u, deg = q.pop(0)
                if u == tgt:
                    return True
                if deg + 1 > k:
                    continue
                for v in graph.get(u, []):
                    if v in seen:
                        continue
                    q.append((v, deg+1))
                    seen.add(v)
            return False

        l, r = 0, max(e[2] for e in edges) + 1
        if not is_possible(r):
            return -1
        if is_possible(l):
            return 0
        while r-l > 1:
            m = (r+l)//2
            # print(l, r, m)
            if is_possible(m):
                r = m
            else:
                l = m
        return r