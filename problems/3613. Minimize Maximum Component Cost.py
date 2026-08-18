'''
=== 3613. Minimize Maximum Component Cost ===

You are given an undirected connected graph with n nodes labeled from 0 to n - 1 and a 2D integer array edges where edges[i] = [ui, vi, wi] denotes an undirected edge between node ui and node vi with weight wi, and an integer k.
You are allowed to remove any number of edges from the graph such that the resulting graph has at most k connected components.
The cost of a component is defined as the maximum edge weight in that component. If a component has no edges, its cost is 0.
Return the minimum possible value of the maximum cost among all components after such removals.

Example 1:
    Input: n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2
    Output: 4
    Explanation:
    Remove the edge between nodes 3 and 4 (weight 6).
    The resulting components have costs of 0 and 4, so the overall maximum cost is 4.
Example 2:
    Input: n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 1
    Output: 5
    Explanation:
    No edge can be removed, since allowing only one component (k = 1) requires the graph to stay fully connected.
    That single component’s cost equals its largest edge weight, which is 5.
 
Constraints:
    1. 1 <= n <= 5 * 104
    2. 0 <= edges.length <= 105
    3. edges[i].length == 3
    4. 0 <= ui, vi < n
    5. 1 <= wi <= 106
    6. 1 <= k <= n
    7. The input graph is connected.
'''
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.n = N
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
            self.n -= 1
        return
# === 123ms && 65.55MB === #
class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges = sorted(edges, key=lambda x: x[2])
        dsu = DSU(n)
        ans = 0
        for u,v,w in edges:
            if dsu.n <= k:
                break
            ans = w
            dsu.union(u, v)
        return ans