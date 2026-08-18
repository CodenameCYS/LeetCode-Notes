'''
=== 3559. Number of Ways to Assign Edge Weights II ===

There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.
Initially, all edges have a weight of 0. You must assign each edge a weight of either 1 or 2.
The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.
You are given a 2D integer array queries. For each queries[i] = [ui, vi], determine the number of ways to assign weights to edges in the path such that the cost of the path between ui and vi is odd.
Return an array answer, where answer[i] is the number of valid assignments for queries[i].
Since the answer may be large, apply modulo 109 + 7 to each answer[i].
Note: For each query, disregard all edges not in the path between node ui and vi.

Example 1:
    Input: edges = [[1,2]], queries = [[1,1],[1,2]]
    Output: [0,1]
    Explanation:
    Query [1,1]: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0.
    Query [1,2]: The path from Node 1 to Node 2 consists of one edge (1 → 2). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.
Example 2:
    Input: edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]
    Output: [2,1,4]
    Explanation:
    Query [1,4]: The path from Node 1 to Node 4 consists of two edges (1 → 3 and 3 → 4). Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.
    Query [3,4]: The path from Node 3 to Node 4 consists of one edge (3 → 4). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.
    Query [2,5]: The path from Node 2 to Node 5 consists of three edges (2 → 1, 1 → 3, and 3 → 5). Assigning (1,2,2), (2,1,2), (2,2,1), or (1,1,1) makes the cost odd. Thus, the number of valid assignments is 4.
 
Constraints:
    1. 2 <= n <= 105
    2. edges.length == n - 1
    3. edges[i] == [ui, vi]
    4. 1 <= queries.length <= 105
    5. queries[i] == [ui, vi]
    6. 1 <= ui, vi <= n
    7. edges represents a valid tree.
'''
MOD = 10**9+7
# === 2773ms && 137.3MB === #
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
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        depth = defaultdict(int)
        tree = defaultdict(list)
        def dfs(u, p):
            nonlocal depth, tree
            if u == 1:
                depth[u] = 0
            else:
                depth[u] = depth[p] + 1
            for v in graph[u]:
                if v == p:
                    continue
                tree[u].append(v)
                dfs(v, u)
            return
        
        dfs(1, 0)
        lca = LCA(1, tree)
        
        def query(u, v):
            p = lca.query(u, v)
            d = depth[u] + depth[v] - 2*depth[p]
            return pow(2, d-1, MOD) if d > 0 else 0
        
        return [query(u, v) for u, v in queries]
        
        