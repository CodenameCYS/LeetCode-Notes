'''
=== 1791. Find Center of Star Graph ===

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

Example 1:
    Input: edges = [[1,2],[2,3],[4,2]]
    Output: 2
    Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:
    Input: edges = [[1,2],[5,1],[1,3],[1,4]]
    Output: 1
 
Constraints:
    1. 3 <= n <= 105
    2. edges.length == n - 1
    3. edges[i].length == 2
    4. 1 <= ui, vi <= n
    5. ui != vi
    6. The given edges represent a valid star graph.
'''
# === 1520ms && 50.7MB === #
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for u, v in edges:
            cnt[u] += 1
            cnt[v] += 1
        res = [x for x in cnt if cnt[x] != 1][0]
        return res