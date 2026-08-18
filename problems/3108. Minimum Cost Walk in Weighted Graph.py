'''
=== 3108. Minimum Cost Walk in Weighted Graph ===

There is an undirected weighted graph with n vertices labeled from 0 to n - 1.
You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.
A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.
The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.
You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.
Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

Example 1:
    Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]
    Output: [1,-1]
    Explanation:
    To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).
    In the second query, there is no walk between nodes 3 and 4, so the answer is -1.
Example 2:
    Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]
    Output: [0]
    Explanation:
    To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).

Constraints:
    1. 2 <= n <= 105
    2. 0 <= edges.length <= 105
    3. edges[i].length == 3
    4. 0 <= ui, vi <= n - 1
    5. ui != vi
    7. 6. 0 <= wi <= 105
    8. 1 <= query.length <= 105
    9. query[i].length == 2
    10. 0 <= si, ti <= n - 1
    11. si != ti
'''
# === 1184ms && 67.9MB === #
class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.value = [-1 for _ in range(n)]
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, u, v, w):
        x = self.find(u)
        y = self.find(v)
        if x != y:
            self.root[y] = x
        if self.value[x] == -1 and self.value[y] == -1:
            self.value[x] = w
        elif self.value[x] != -1 and self.value[y] == -1:
            self.value[x] = w & self.value[x]
        elif self.value[x] == -1 and self.value[y] != -1:
            self.value[x] = w & self.value[y]
        else:
            self.value[x] = self.value[y] & self.value[x] & w
        return

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        for u, v, w in edges:
            dsu.union(u, v, w)
        
        def _query(u, v):
            x, y = dsu.find(u), dsu.find(v)
            if x != y:
                return -1
            return dsu.value[x]
        # print(dsu.root)
        # print(dsu.value)
        # print("=" * 10)
        return [_query(u, v) for u, v in query]