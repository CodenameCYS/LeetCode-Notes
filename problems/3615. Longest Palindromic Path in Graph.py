'''
=== 3615. Longest Palindromic Path in Graph ===

You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1 and a 2D array edges, where edges[i] = [ui, vi] indicates an edge between nodes ui and vi.
You are also given a string label of length n, where label[i] is the character associated with node i.
You may start at any node and move to any adjacent node, visiting each node at most once.
Return the maximum possible length of a palindrome that can be formed by visiting a set of unique nodes along a valid path.
A palindrome is a string that reads the same forward and backward.

Example 1:
    Input: n = 3, edges = [[0,1],[1,2]], label = "aba"
    Output: 3
    Explanation:
    The longest palindromic path is from node 0 to node 2 via node 1, following the path 0 → 1 → 2 forming string "aba".
    This is a valid palindrome of length 3.
Example 2:
    Input: n = 3, edges = [[0,1],[0,2]], label = "abc"
    Output: 1
    Explanation:
    No path with more than one node forms a palindrome.
    The best option is any single node, giving a palindrome of length 1.
Example 3:
    Input: n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac"
    Output: 3
    Explanation:
    The longest palindromic path is from node 0 to node 1, following the path 0 → 3 → 1, forming string "bcb".
    This is a valid palindrome of length 3.
 
Constraints:
    1. 1 <= n <= 14
    2. n - 1 <= edges.length <= n * (n - 1) / 2
    3. edges[i] == [ui, vi]
    4. 0 <= ui, vi <= n - 1
    5. ui != vi
    6. label.length == n
    7. label consists of lowercase English letters.
    8. There are no duplicate edges.
'''
# === 8934ms && 207.40MB === #
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        @lru_cache(None)
        def dfs(u1, u2, status):
            if u1 > u2:
                return dfs(u2, u1, status)
            ans = 2
            status = status | (1<<u1) | (1<<u2)
            for v1 in graph[u1]:
                if status & (1<<v1) != 0:
                    continue
                for v2 in graph[u2]:
                    if status & (1<<v2) != 0:
                        continue
                    if v1 != v2 and label[v1] == label[v2]:
                        ans = max(ans, 2 + dfs(v1, v2, status))
            return ans

        ans = 1
        for u in graph.keys():
            for v in graph[u]:
                if label[u] == label[v]:
                    ans = max(ans, dfs(u, v, 0))
            m = len(graph[u])
            for i in range(m-1):
                for j in range(i+1, m):
                    v, w = graph[u][i], graph[u][j]
                    if label[v] == label[w]:
                        ans = max(ans, 1+dfs(v, w, 1<<u))
        return ans

        