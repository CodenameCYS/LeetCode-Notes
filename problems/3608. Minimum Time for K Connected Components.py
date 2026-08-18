'''
=== 3608. Minimum Time for K Connected Components ===

You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [ui, vi, timei] indicates an undirected edge between nodes ui and vi that can be removed at timei.
You are also given an integer k.
Initially, the graph may be connected or disconnected. Your task is to find the minimum time t such that after removing all edges with time <= t, the graph contains at least k connected components.
Return the minimum time t.
A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

Example 1:
    Input: n = 2, edges = [[0,1,3]], k = 2
    Output: 3
    Explanation:
    Initially, there is one connected component {0, 1}.
    At time = 1 or 2, the graph remains unchanged.
    At time = 3, edge [0, 1] is removed, resulting in k = 2 connected components {0}, {1}. Thus, the answer is 3.
Example 2:
    Input: n = 3, edges = [[0,1,2],[1,2,4]], k = 3
    Output: 4
    Explanation:
    Initially, there is one connected component {0, 1, 2}.
    At time = 2, edge [0, 1] is removed, resulting in two connected components {0}, {1, 2}.
    At time = 4, edge [1, 2] is removed, resulting in k = 3 connected components {0}, {1}, {2}. Thus, the answer is 4.
Example 3:
    Input: n = 3, edges = [[0,2,5]], k = 2
    Output: 0
    Explanation:
    Since there are already k = 2 disconnected components {1}, {0, 2}, no edge removal is needed. Thus, the answer is 0.
 
Constraints:
    1. 1 <= n <= 105
    2. 0 <= edges.length <= 105
    3. edges[i] = [ui, vi, timei]
    4. 0 <= ui, vi < n
    5. ui != vi
    6. 1 <= timei <= 109
    7. 1 <= k <= n
    8. There are no duplicate edges.
'''
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.cluster = N
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
            self.cluster -= 1
        return
# === 121ms && 60.30MB === #
class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        dsu = DSU(n)
        m = len(edges)
        if m == 0:
            return 0
        edges = sorted(edges, key=lambda x: x[2], reverse=True)
        idx = 0
        while idx < m and dsu.cluster >= k:
            u, v, t = edges[idx]
            ans = t
            dsu.union(u, v)
            idx += 1
        return ans if dsu.cluster < k else 0

            