'''
=== 3585. Find Weighted Median Node in Tree ===

You are given an integer n and an undirected, weighted tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates an edge from node ui to vi with weight wi.
The weighted median node is defined as the first node x on the path from ui to vi such that the sum of edge weights from ui to x is greater than or equal to half of the total path weight.
You are given a 2D integer array queries. For each queries[j] = [uj, vj], determine the weighted median node along the path from uj to vj.
Return an array ans, where ans[j] is the node index of the weighted median for queries[j].

Example 1:
    Input: n = 2, edges = [[0,1,7]], queries = [[1,0],[0,1]]
    Output: [0,1]
Example 2:
    Input: n = 3, edges = [[0,1,2],[2,0,4]], queries = [[0,1],[2,0],[1,2]]
    Output: [1,0,2]
Example 3:
    Input: n = 5, edges = [[0,1,2],[0,2,5],[1,3,1],[2,4,3]], queries = [[3,4],[1,2]]
    Output: [2,2]

Constraints:
    1. 2 <= n <= 105
    2. edges.length == n - 1
    3. edges[i] == [ui, vi, wi]
    4. 0 <= ui, vi < n
    5. 1 <= wi <= 109
    6. 1 <= queries.length <= 105
    7. queries[j] == [uj, vj]
    8. 0 <= uj, vj < n
    9. The input is generated such that edges represents a valid tree.
'''
import math
from collections import deque
from typing import List, Tuple

class Tree:
    def __init__(self, n: int, edges: List[Tuple[int, int, int]], root: int = 0):
        self.n = n
        self.max_log = math.floor(math.log2(n)) + 1  # 最大跳跃步数的对数
        self.graph = [[] for _ in range(n)]
        self.distances = [0 for _ in range(n)]
        self.depth = [-1] * n
        self.parent = [[-1] * n for _ in range(self.max_log)]  # parent[k][i]: i 的第 2^k 级祖先
        
        # 构建邻接表
        for u, v, w in edges:
            self.graph[u].append((v, w))
            self.graph[v].append((u, w))
        
        # 预处理深度和祖先表
        self._bfs(root)
    
    def _bfs(self, root: int):
        """BFS 初始化深度和直接父节点（即 2^0 级祖先）"""
        queue = deque([root])
        self.depth[root] = 0
        self.distances[root] = 0
        self.parent[0][root] = -1  # 根节点无父节点
        
        while queue:
            u = queue.popleft()
            for v, w in self.graph[u]:
                if v == self.parent[0][u]:
                    continue
                self.depth[v] = self.depth[u] + 1
                self.distances[v] = self.distances[u] + w
                self.parent[0][v] = u
                queue.append(v)
        
        # 递推计算 2^k 级祖先
        for k in range(1, self.max_log):
            for i in range(self.n):
                if self.parent[k-1][i] != -1:
                    self.parent[k][i] = self.parent[k-1][self.parent[k-1][i]]
    
    def query(self, u: int, v: int) -> int:
        """查询节点 u 和 v 的最近公共祖先"""
        # 确保 u 是深度较大的节点
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # 将 u 上跳到与 v 同深度
        diff = self.depth[u] - self.depth[v]
        k = 0
        while diff:
            if diff & 1:
                u = self.parent[k][u]
            diff >>= 1
            k += 1
        
        if u == v:
            return u
        
        # 同步上跳，寻找最近公共祖先
        for k in range(self.max_log - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]

    def query_distance(self, u):
        return self.distances[u]

    def query_closest_parent(self, u: int, d: float):
        h = self.max_log-1
        while h >= 0:
            if self.parent[h][u] != -1 and self.distances[self.parent[h][u]] >= d:
                u = self.parent[h][u]
            h -= 1
        return u
# === 1292ms && 102.01MB === #
class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        tree = Tree(n, edges, 0)

        def query(u, v):
            p = tree.query(u, v)
            du, dv, dp = tree.query_distance(u), tree.query_distance(v), tree.query_distance(p)
            d1, d2 = du-dp, dv-dp
            d = (d1+d2) / 2
            if d <= d2:
                return tree.query_closest_parent(v, dv-d)
            else:
                w = tree.query_closest_parent(u, du-d)
                dw = tree.query_distance(w)
                # print(u, v, d1, d2, d, w, dw)
                return tree.parent[0][w] if du-dw != d else w

        return [query(u, v) for u, v in queries]