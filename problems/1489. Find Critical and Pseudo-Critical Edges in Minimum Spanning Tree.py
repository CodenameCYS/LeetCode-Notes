'''
=== 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree ===

Given a weighted undirected connected graph with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between nodes fromi and toi. A minimum spanning tree (MST) is a subset of the edges of the graph that connects all vertices without cycles and with the minimum possible total edge weight.
Find all the critical and pseudo-critical edges in the minimum spanning tree (MST) of the given graph. An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. A pseudo-critical edge, on the other hand, is that which can appear in some MSTs but not all.
Note that you can return the indices of the edges in any order.

Example 1:
    Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    Output: [[0,1],[2,3,4,5]]
    Explanation: The figure above describes the graph.
    The following figure shows all the possible MSTs:
    Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
    The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
Example 2:
    Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
    Output: [[],[0,1,2,3]]
    Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 
Constraints:
    1. 2 <= n <= 100
    2. 1 <= edges.length <= min(200, n * (n - 1) / 2)
    3. edges[i].length == 3
    4. 0 <= fromi < toi < n
    5. 1 <= weighti <= 1000
    6. All pairs (fromi, toi) are distinct.
'''
class DSU:
    def __init__(self, n):
        self.dsu = [i for i in range(n)]
        
    def find(self, x):
        if x != self.dsu[x]:
            self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        self.dsu[yr] = xr
        return True
# === 2500ms(33.70%) && 14.2MB(8.29%) === #
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted((w, u, v, i) for i, (u, v, w) in enumerate(edges))
        critical = []
        pseudo = []
        for w0, u0, v0, i in edges:
            dsu1 = DSU(n)
            dsu2 = DSU(n)
            dsu1.union(u0, v0)
            s1, s2 = w0, 0
            for w, u, v, j in edges:
                if i == j:
                    continue
                if dsu1.union(u, v):
                    s1 += w
                if dsu2.union(u, v):
                    s2 += w
            if s1 == s2:
                pseudo.append(i)
            elif s1 < s2 or dsu2.union(u0, v0):
                critical.append(i)
            # print(u, v, w, dsu1.dsu, dsu2.dsu, critical, pseudo)
        return critical, pseudo
        
        
        