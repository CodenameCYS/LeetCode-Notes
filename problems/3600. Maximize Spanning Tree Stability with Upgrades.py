'''
=== 3600. Maximize Spanning Tree Stability with Upgrades ===

You are given an integer n, representing n nodes numbered from 0 to n - 1 and a list of edges, where edges[i] = [ui, vi, si, musti]:
    - ui and vi indicates an undirected edge between nodes ui and vi.
    - si is the strength of the edge.
    - musti is an integer (0 or 1). If musti == 1, the edge must be included in the spanning tree. These edges cannot be upgraded.
You are also given an integer k, the maximum number of upgrades you can perform. Each upgrade doubles the strength of an edge, and each eligible edge (with musti == 0) can be upgraded at most once.
The stability of a spanning tree is defined as the minimum strength score among all edges included in it.
Return the maximum possible stability of any valid spanning tree. If it is impossible to connect all nodes, return -1.
Note: A spanning tree of a graph with n nodes is a subset of the edges that connects all nodes together (i.e. the graph is connected) without forming any cycles, and uses exactly n - 1 edges.

Example 1:
    Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1
    Output: 2
    Explanation:
    Edge [0,1] with strength = 2 must be included in the spanning tree.
    Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
    The resulting spanning tree includes these two edges with strengths 2 and 6.
    The minimum strength in the spanning tree is 2, which is the maximum possible stability.
Example 2:
    Input: n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2
    Output: 6
    Explanation:
    Since all edges are optional and up to k = 2 upgrades are allowed.
    Upgrade edges [0,1] from 4 to 8 and [1,2] from 3 to 6.
    The resulting spanning tree includes these two edges with strengths 8 and 6.
    The minimum strength in the tree is 6, which is the maximum possible stability.
Example 3:
    Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0
    Output: -1
    Explanation:
    All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.
 
Constraints:
    1. 2 <= n <= 105
    2. 1 <= edges.length <= 105
    3. edges[i] = [ui, vi, si, musti]
    4. 0 <= ui, vi < n
    5. ui != vi
    6. 1 <= si <= 105
    7. musti is either 0 or 1.
    8. 0 <= k <= n
    9. There are no duplicate edges.
'''
# === 1271ms && 74.06MB === #
class DSU:
    def __init__(self, N):
        self.node = N
        self.cluster = N
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
            self.cluster -= 1
        return
    
def copy_dsu(dsu):
    n = dsu.node
    new_dsu = DSU(n)
    new_dsu.root = deepcopy(dsu.root)
    new_dsu.cluster = dsu.cluster
    return new_dsu

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # edges = sorted(edges, key=lambda x: (x[3], x[2]), reverse=True)
        must = [(u,v,w) for u, v, w, m in edges if m == 1]
        candi = [(u,v,w) for u, v, w, m in edges if m == 0]
        candi = sorted(candi, key=lambda x: x[2], reverse=True)
        # print(candi)
        dsu = DSU(n)
        l, r = 0, math.inf
        for u, v, w in must:
            if dsu.find(u) == dsu.find(v):
                return -1
            dsu.union(u, v)
            r = min(r, w)
        r = 2*candi[0][2] if r == math.inf else r
        
        def is_possible(m):
            _dsu = copy_dsu(dsu)
            # print(m, _dsu.cluster, _dsu.node, _dsu.root)
            cnt = 0
            for u, v, w in candi:
                if w * 2 < m or (w < m and cnt >= k):
                    break
                if _dsu.find(u) == _dsu.find(v):
                    continue
                if w < m:
                    cnt += 1
                _dsu.union(u, v)
                if _dsu.cluster == 1:
                    break
            # print(_dsu.cluster, _dsu.node, _dsu.root)
            # print("=" * 5)
            return _dsu.cluster == 1

        if is_possible(r):
            return r
        elif not is_possible(l):
            return -1
        while r-l > 1:
            m = (l+r) // 2
            if is_possible(m):
                l = m
            else:
                r = m
        return l
