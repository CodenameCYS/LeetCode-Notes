'''
=== 1697. Checking Existence of Edge Length Limited Paths ===

An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.
Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .
Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

Example 1:
    Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
    Output: [false,true]
    Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
    For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
    For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
Example 2:
    Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
    Output: [true,false]
    Exaplanation: The above figure shows the given graph.
 
Constraints:
    1. 2 <= n <= 105
    2. 1 <= edgeList.length, queries.length <= 105
    3. edgeList[i].length == 3
    4. queries[j].length == 3
    5. 0 <= ui, vi, pj, qj <= n - 1
    6. ui != vi
    7. pj != qj
    8. 1 <= disi, limitj <= 109
    9. There may be multiple edges between two nodes.
'''
class DSU:
    def __init__(self, n):
        self.dsu = [i for i in range(n)]
    
    def find(self, x):
        if self.dsu[x] != x:
            self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.dsu[y] = x
        return
# === 2028ms && 61.2MB === #
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = sorted(edgeList, key=lambda x: x[2])
        queries = sorted([(idx, u, v, limit) for idx, (u, v, limit) in enumerate(queries)], key=lambda x: x[-1])
        m = len(edges)
        
        res = [False for _ in queries]
        i = 0
        dsu = DSU(n)
        for idx, u, v, limit in queries:
            while i < m and edges[i][2] < limit:
                p, q, _ = edges[i]
                dsu.union(p, q)
                i += 1
            res[idx] = (dsu.find(u) == dsu.find(v))
        return res