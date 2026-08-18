'''
=== 3373. Maximize the Number of Target Nodes After Connecting Trees II ===

There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.
You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.
Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.
Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

Example 1:
    Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    Output: [8,7,7,8,8]
    Explanation:
    For i = 0, connect node 0 from the first tree to node 0 from the second tree.
    For i = 1, connect node 1 from the first tree to node 4 from the second tree.
    For i = 2, connect node 2 from the first tree to node 7 from the second tree.
    For i = 3, connect node 3 from the first tree to node 0 from the second tree.
    For i = 4, connect node 4 from the first tree to node 4 from the second tree.
Example 2:
    Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]
    Output: [3,6,6,6,6]
    Explanation:
    For every i, connect node i of the first tree with any node of the second tree.

Constraints:
    1. 2 <= n, m <= 105
    2. edges1.length == n - 1
    3. edges2.length == m - 1
    4. edges1[i].length == edges2[i].length == 2
    5. edges1[i] = [ai, bi]
    6. 0 <= ai, bi < n
    7. edges2[i] = [ui, vi]
    8. 0 <= ui, vi < m
    9. The input is generated such that edges1 and edges2 represent valid trees.
'''
# === 4387ms && 386.5MB === #
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        graph2 = defaultdict(list)
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)
            
        n, m = len(edges1) + 1, len(edges2) + 1
        
        @lru_cache(None)
        def dfs1(u, p, is_valid):
            if is_valid:
                if (p != -1 and len(graph1[u]) == 1) or (p == -1 and len(graph1[u]) == 0):
                    return 1
                else:
                    return 1 + sum(dfs1(v, u, False) for v in graph1[u] if v != p) 
            else:
                if (p != -1 and len(graph1[u]) == 1) or (p == -1 and len(graph1[u]) == 0):
                    return 0
                else:
                    return sum(dfs1(v, u, True) for v in graph1[u] if v != p) 
        
        @lru_cache(None)
        def dfs2(u, p, is_valid):
            if is_valid:
                if (p != -1 and len(graph2[u]) == 1) or (p == -1 and len(graph2[u]) == 0):
                    return 1
                else:
                    return 1 + sum(dfs2(v, u, False) for v in graph2[u] if v != p) 
            else:
                if (p != -1 and len(graph2[u]) == 1) or (p == -1 and len(graph2[u]) == 0):
                    return 0
                else:
                    return sum(dfs2(v, u, True) for v in graph2[u] if v != p) 
        
        s1 = [dfs1(u, -1, True) for u in range(n)]
        # print(s1)
        s2 = [dfs2(u, -1, False) for u in range(m)]
        # print(s2)
        s = max(s2)
        return [x+s for x in s1]
            