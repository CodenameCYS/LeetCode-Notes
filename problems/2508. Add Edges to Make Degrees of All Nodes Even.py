'''
=== 2508. Add Edges to Make Degrees of All Nodes Even ===

There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.
You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.
Return true if it is possible to make the degree of each node in the graph even, otherwise return false.
The degree of a node is the number of edges connected to it.

Example 1:
    Input: n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
    Output: true
    Explanation: The above diagram shows a valid way of adding an edge.
    Every node in the resulting graph is connected to an even number of edges.
Example 2:
    Input: n = 4, edges = [[1,2],[3,4]]
    Output: true
    Explanation: The above diagram shows a valid way of adding two edges.
Example 3:
    Input: n = 4, edges = [[1,2],[1,3],[1,4]]
    Output: false
    Explanation: It is not possible to obtain a valid graph with adding at most 2 edges.
 
Constraints:
    1. 3 <= n <= 105
    2. 2 <= edges.length <= 105
    3. edges[i].length == 2
    4. 1 <= ai, bi <= n
    5. ai != bi
    6. There are no repeated edges.
'''
# === 2708ms && 70MB === #
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        deg = defaultdict(set)
        for u, v in edges:
            deg[u].add(v)
            deg[v].add(u)

        odd = set()
        for u in range(1, n+1):
            if len(deg[u]) % 2 == 1:
                odd.add(u)
        if len(odd) == 0:
            return True
        elif len(odd) == 2:
            u, v = list(odd)
            return v not in deg[u] or len(deg[u] | deg[v]) < n
        elif len(odd) == 4:
            return any((b not in deg[a] and c not in deg[d]) for a, b, c, d in permutations(odd))
        else:
            return False
                
            
            
            
        