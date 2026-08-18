'''
=== 1579. Remove Max Number of Edges to Keep Graph Fully Traversable ===

Alice and Bob have an undirected graph of n nodes and 3 types of edges:
    - Type 1: Can be traversed by Alice only.
    - Type 2: Can be traversed by Bob only.
    - Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.
Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.

Example 1:
    Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    Output: 2
    Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:
    Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
    Output: 0
    Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:
    Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
    Output: -1
    Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 
Constraints:
    1. 1 <= n <= 10^5
    2. 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
    3. edges[i].length == 3
    4. 1 <= edges[i][0] <= 3
    5. 1 <= edges[i][1] < edges[i][2] <= n
    6. All tuples (typei, ui, vi) are distinct.
'''
from copy import deepcopy
class DSU:
    def __init__(self, n):
        self.dsu = [i for i in range(n+1)]
        
    def find(self, x):
        if x == self.dsu[x]:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.dsu[yr] = xr
        return
# === 2372ms(78.6MB) && 72MB(20.80%) === #
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = []
        bob = []
        both = []
        for t, x, y in edges:
            if t == 1:
                alice.append((x, y))
            elif t == 2:
                bob.append((x, y))
            else:
                both.append((x, y))
        dsu = DSU(n)
        counter3 = 0
        for x, y in both:
            if dsu.find(x) == dsu.find(y):
                continue
            dsu.union(x, y)
            counter3 += 1
        dsu1 = deepcopy(dsu)
        counter1 = 0
        for x, y in alice:
            if dsu1.find(x) == dsu1.find(y):
                continue
            dsu1.union(x, y)
            counter1 += 1
        # print(dsu1.dsu)
        dsu2 = deepcopy(dsu)
        counter2 = 0
        for x, y in bob:
            if dsu2.find(x) == dsu2.find(y):
                continue
            dsu2.union(x, y)
            counter2 += 1
        # print(dsu2.dsu)
        if counter1 + counter3 != n-1 or counter2 + counter3 != n-1:
            return -1
        else:
            return len(edges) + counter3 - 2*n +2
        