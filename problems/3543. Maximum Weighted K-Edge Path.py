'''
=== 3543. Maximum Weighted K-Edge Path ===

You are given an integer n and a Directed Acyclic Graph (DAG) with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [ui, vi, wi] indicates a directed edge from node ui to vi with weight wi.
You are also given two integers, k and t.
Your task is to determine the maximum possible sum of edge weights for any path in the graph such that:
    - The path contains exactly k edges.
    - The total sum of edge weights in the path is strictly less than t.
Return the maximum possible sum of weights for such a path. If no such path exists, return -1.

Example 1:
    Input: n = 3, edges = [[0,1,1],[1,2,2]], k = 2, t = 4
    Output: 3
    Explanation:
    The only path with k = 2 edges is 0 -> 1 -> 2 with weight 1 + 2 = 3 < t.
    Thus, the maximum possible sum of weights less than t is 3.
Example 2:
    Input: n = 3, edges = [[0,1,2],[0,2,3]], k = 1, t = 3
    Output: 2
    Explanation:
    There are two paths with k = 1 edge:
    0 -> 1 with weight 2 < t.
    0 -> 2 with weight 3 = t, which is not strictly less than t.
    Thus, the maximum possible sum of weights less than t is 2.
Example 3:
    Input: n = 3, edges = [[0,1,6],[1,2,8]], k = 1, t = 6
    Output: -1
    Explanation:
    There are two paths with k = 1 edge:
    0 -> 1 with weight 6 = t, which is not strictly less than t.
    1 -> 2 with weight 8 > t, which is not strictly less than t.
    Since there is no path with sum of weights strictly less than t, the answer is -1.
 
Constraints:
    1. 1 <= n <= 300
    2. 0 <= edges.length <= 300
    3. edges[i] = [ui, vi, wi]
    4. 0 <= ui, vi < n
    5. ui != vi
    6. 1 <= wi <= 10
    7. 0 <= k <= 300
    8. 1 <= t <= 600
    9. The input graph is guaranteed to be a DAG.
    10. There are no duplicate edges.
'''
# === 216ms && 48.2MB === #
class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        @lru_cache(None)
        def dfs(u, k):
            if k == 0:
                return {0}
            if graph[u] == []:
                return set()
            ans = set()
            for v, w in graph[u]:
                nxt_set = dfs(v, k-1)
                for nxt in nxt_set:
                    if nxt + w < t:
                        ans.add(nxt+w)
            return ans
        
        return max(max(dfs(u, k)) if len(dfs(u, k)) > 0 else -1 for u in range(n))
        
        
        
        
        