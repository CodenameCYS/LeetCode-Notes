'''
=== 3203. Find Minimum Diameter After Merging Two Trees ===

There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
You must connect one node from the first tree with another node from the second tree with an edge.
Return the minimum possible diameter of the resulting tree.
The diameter of a tree is the length of the longest path between any two nodes in the tree.

Example 1:
    Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
    Output: 3
    Explanation:
    We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.
Example 2:
    Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
    Output: 5
    Explanation:
    We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

Constraints:
    1. 1 <= n, m <= 105
    2. edges1.length == n - 1
    3. edges2.length == m - 1
    4. edges1[i].length == edges2[i].length == 2
    5. edges1[i] = [ai, bi]
    6. 0 <= ai, bi < n
    7. edges2[i] = [ui, vi]
    8. 0 <= ui, vi < m
    9. The input is generated such that edges1 and edges2 represent valid trees.
'''
# === 3216ms && 93.4MB === #
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def dfs(edges):
            if edges == []:
                return 0, 0
            diameter = 0
            graph = defaultdict(list)
            deg = defaultdict(int)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
                deg[u] += 1
                deg[v] += 1
            seen = set()
            leafs = [u for u in deg if deg[u] == 1]
            depth = defaultdict(int)
            while leafs != []:
                u = leafs.pop(0)
                if u in seen:
                    continue
                seen.add(u)
                for v in graph[u]:
                    if v in seen:
                        continue
                    diameter = max(diameter, depth[v] + depth[u] + 1)
                    depth[v] = max(depth[v], depth[u]+1)
                    deg[v] -= 1
                    if deg[v] == 1:
                        leafs.append(v)
            # print(edges, depth)
            return max(depth.values()), diameter
        
        depth1, diameter1 = dfs(edges1)
        depth2, diameter2 = dfs(edges2)
        return max(depth1 + depth2 + 1, diameter1, diameter2)