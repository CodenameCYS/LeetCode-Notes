'''
=== 2608. Shortest Cycle in a Graph ===

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges in the graph are represented by a given 2D integer array edges, where edges[i] = [ui, vi] denotes an edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
Return the length of the shortest cycle in the graph. If no cycle exists, return -1.
A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.

Example 1:
    Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
    Output: 3
    Explanation: The cycle with the smallest length is : 0 -> 1 -> 2 -> 0 
Example 2:
    Input: n = 4, edges = [[0,1],[0,2]]
    Output: -1
    Explanation: There are no cycles in this graph.
 
Constraints:
    1. 2 <= n <= 1000
    2. 1 <= edges.length <= 1000
    3. edges[i].length == 2
    4. 0 <= ui, vi < n
    5. ui != vi
    6. There are no repeated edges.
'''
# === 1960ms && 14.6MB === #
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)
        
        seen = set()
        res = n+1
        for u in range(n):
            q = [(u, -1, 0)]
            distances = {}
            loop = False
            while (not loop) and q:
                # print(q)
                u, pre, d = q.pop(0)
                seen.add(u)
                distances[u] = d
                for v in graph[u]:
                    if v in distances:
                        if v == pre:
                            continue
                        res = min(res, d+1 + distances[v])
                        loop = True
                    else:
                        q.append((v, u, d+1))
        #     print(distances, res, q)
        # print("=" * 10)
        return res if res <= n else -1