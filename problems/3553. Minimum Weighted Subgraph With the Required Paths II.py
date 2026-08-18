'''
=== 3553. Minimum Weighted Subgraph With the Required Paths II ===

You are given an undirected weighted tree with n nodes, numbered from 0 to n - 1. It is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates that there is an edge between nodes ui and vi with weight wi.​
Additionally, you are given a 2D integer array queries, where queries[j] = [src1j, src2j, destj].
Return an array answer of length equal to queries.length, where answer[j] is the minimum total weight of a subtree such that it is possible to reach destj from both src1j and src2j using edges in this subtree.
A subtree here is any connected subset of nodes and edges of the original tree forming a valid tree.

Example 1:
    Input: edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]
    Output: [12,11]
    Explanation:
    The blue edges represent one of the subtrees that yield the optimal answer.
    answer[0]: The total weight of the selected subtree that ensures a path from src1 = 2 and src2 = 3 to dest = 4 is 3 + 5 + 4 = 12.
    answer[1]: The total weight of the selected subtree that ensures a path from src1 = 0 and src2 = 2 to dest = 5 is 2 + 3 + 6 = 11.
Example 2:
    Input: edges = [[1,0,8],[0,2,7]], queries = [[0,1,2]]
    Output: [15]
    Explanation:
    answer[0]: The total weight of the selected subtree that ensures a path from src1 = 0 and src2 = 1 to dest = 2 is 8 + 7 = 15.

Constraints:
    1. 3 <= n <= 105
    2. edges.length == n - 1
    3. edges[i].length == 3
    4. 0 <= ui, vi < n
    5. 1 <= wi <= 104
    6. 1 <= queries.length <= 105
    7. queries[j].length == 3
    8. 0 <= src1j, src2j, destj < n
    9. src1j, src2j, and destj are pairwise distinct.
    10. The input is generated such that edges represents a valid tree.
'''
# === 5339ms && 174.4MB === #
class LCA:
    def __init__(self, root, tree):
        self.max_level = 20  # 根据树的高度调整
        self.parent = defaultdict(lambda: [-1]*self.max_level)
        self.depth = {}
        self.preprocess(root, tree)

    def preprocess(self, root, tree):
        stack = [(root, -1, 0)]  # (node, parent, depth)
        while stack:
            node, par, d = stack.pop()
            self.depth[node] = d
            self.parent[node][0] = par
            for k in range(1, self.max_level):
                if self.parent[node][k-1] != -1:
                    self.parent[node][k] = self.parent[self.parent[node][k-1]][k-1]
            for child in tree[node]:
                if child != par:
                    stack.append((child, node, d+1))

    def query(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        # 对齐深度
        for k in range(self.max_level-1, -1, -1):
            if self.depth[u] - (1 << k) >= self.depth[v]:
                u = self.parent[u][k]
        if u == v:
            return u
        # 同步跳转
        for k in range(self.max_level-1, -1, -1):
            if self.parent[u][k] != -1 and self.parent[u][k] != self.parent[v][k]:
                u = self.parent[u][k]
                v = self.parent[v][k]
        return self.parent[u][0]

class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        seen = {0}
        parents = defaultdict(int)
        dist = defaultdict(int)
        tree = defaultdict(list)
        parents[0] = -1
        q = [(0, 0)]
        while q:
            d, u = q.pop(0)
            for v, w in graph[u]:
                if v in seen:
                    continue
                seen.add(v)
                tree[u].append(v)
                parents[v] = u
                dist[v] = d + w
                q.append((d+w, v))
                
        # @lru_cache(None)
        # def get_same_parent(u, v):
        #     if dist[u] > dist[v]:
        #         return get_same_parent(v, u)
        #     path = set()
        #     while u != -1 and v != u:
        #         path.add(u)
        #         u = parents[u]
        #     if u == v:
        #         return v
        #     while v not in path:
        #         v = parents[v]
        #     return v
        
        lca = LCA(0, tree)
        
        def get_dist(u, v):
            # p = get_same_parent(u, v)
            p = lca.query(u, v)
            return dist[u] + dist[v] - 2*dist[p]
        
        def query(u, v, w):
            return (get_dist(u, v) + get_dist(u, w) + get_dist(v, w)) // 2
        
        return [query(u, v, w) for u, v, w in queries]
                
        