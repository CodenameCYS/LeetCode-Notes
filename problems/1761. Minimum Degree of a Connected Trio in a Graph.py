'''
=== 1761. Minimum Degree of a Connected Trio in a Graph ===

You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.
A connected trio is a set of three nodes where there is an edge between every pair of them.
The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.
Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.

Example 1:
    Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
    Output: 3
    Explanation: There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.
Example 2:
    Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
    Output: 0
    Explanation: There are exactly three trios:
    1) [1,4,3] with degree 0.
    2) [2,5,6] with degree 2.
    3) [5,6,7] with degree 2.
 
Constraints:
    1. 2 <= n <= 400
    2. edges[i].length == 2
    3. 1 <= edges.length <= n * (n-1) / 2
    4. 1 <= ui, vi <= n
    5. ui != vi
    6. There are no repeated edges.
'''
# === 11492ms && 39.6MB === #
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(set)
        for u, v in edges:
            connections[u].add(v)
            connections[v].add(u)
        length = {k: len(v) for k, v in connections.items()}
        res = math.inf
        for u, v in edges:
            for w in connections[u] & connections[v]:
                d = length[u] + length[v] + length[w] - 6
                res = min(d, res)
                if res == 0:
                    break
            if res == 0:
                break
        return res if res != math.inf else -1

# === 648ms && 51MB === 算法来源于网上#
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph=collections.defaultdict(set)
        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)
        nds=sorted([[len(graph[x]),x] for x in graph])
        nnds=sorted([[len(graph[x])+len(graph[y]),x,y] for x,y in edges])
        ans=3*n*(n-1)
        for w0,x,y in nnds:
            if w0>=ans:
                break
            for w1,z in nds:
                if w0+w1>=ans:
                    break
                if z in graph[x] and z in graph[y]:
                    ans=min(ans,w0+w1)
                    break
        return ans-6 if ans<3*n*(n-1) else -1