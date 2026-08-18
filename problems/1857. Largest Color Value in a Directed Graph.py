'''
=== 1857. Largest Color Value in a Directed Graph ===

There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

Example 1:
    Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
    Output: 3
    Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:
    Input: colors = "a", edges = [[0,0]]
    Output: -1
    Explanation: There is a cycle from 0 to 0.
 
Constraints:
    1. n == colors.length
    2. m == edges.length
    3. 1 <= n <= 105
    4. 0 <= m <= 105
    5. colors consists of lowercase English letters.
    6. 0 <= aj, bj < n
'''
# === 3092ms && 88.1MB === #
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        
        deg = [0 for _ in range(n)]
        graph = defaultdict(list)
        for u, v in edges:
            deg[u] += 1
            graph[v].append(u)
        
        endpoints = [u for u in range(n) if deg[u] == 0]
        cnt = [[0 for _ in range(26)] for _ in range(n)]
        while endpoints:
            v = endpoints.pop(0)
            color = ord(colors[v]) - ord('a')
            cnt[v][color] += 1
            for u in graph[v]:
                deg[u] -= 1
                for i in range(26):
                    cnt[u][i] = max(cnt[u][i], cnt[v][i])
                if deg[u] == 0:
                    endpoints.append(u)
                    
        if any(v != 0 for v in deg):
            return -1
        return max(max(c) for c in cnt)
            
        