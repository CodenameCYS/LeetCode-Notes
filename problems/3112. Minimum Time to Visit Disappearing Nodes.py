'''
=== 3112. Minimum Time to Visit Disappearing Nodes ===

There is an undirected graph of n nodes. You are given a 2D array edges, where edges[i] = [ui, vi, lengthi] describes an edge between node ui and node vi with a traversal time of lengthi units.
Additionally, you are given an array disappear, where disappear[i] denotes the time when the node i disappears from the graph and you won't be able to visit it.
Notice that the graph might be disconnected and might contain multiple edges.
Return the array answer, with answer[i] denoting the minimum units of time required to reach node i from node 0. If node i is unreachable from node 0 then answer[i] is -1.

Example 1:
    Input:  n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]
    Output:  [0,-1,4]
    Explanation:
    We are starting our journey from node 0, and our goal is to find the minimum time required to reach each node before it disappears.
    - For node 0, we don't need any time as it is our starting point.
    - For node 1, we need at least 2 units of time to traverse edges[0]. Unfortunately, it disappears at that moment, so we won't be able to visit it.
    - For node 2, we need at least 4 units of time to traverse edges[2].
Example 2:
    Input:  n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]
    Output:  [0,2,3]
    Explanation:
    We are starting our journey from node 0, and our goal is to find the minimum time required to reach each node before it disappears.
    - For node 0, we don't need any time as it is the starting point.
    - For node 1, we need at least 2 units of time to traverse edges[0].
    - For node 2, we need at least 3 units of time to traverse edges[0] and edges[1].
Example 3:
    Input: n = 2, edges = [[0,1,1]], disappear = [1,1]
    Output: [0,-1]
    Explanation:
    Exactly when we reach node 1, it disappears.

Constraints:
    1. 1 <= n <= 5 * 104
    2. 0 <= edges.length <= 105
    3. edges[i] == [ui, vi, lengthi]
    4. 0 <= ui, vi <= n - 1
    5. 1 <= lengthi <= 105
    6. disappear.length == n
    7. 1 <= disappear[i] <= 105
'''
# === 1389ms && 65.3MB === #
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v, l in edges:
            graph[u].append((v, l))
            graph[v].append((u, l))
            
        ans = [-1 for _ in range(n)]
        q = [(0, 0)]
        seen = set()
        
        while q:
            t, u = heapq.heappop(q)
            if u in seen:
                continue
            seen.add(u)
            if t >= disappear[u]:
                continue
            if ans[u] != -1 and ans[u] <= t:
                continue
            ans[u] = t
            for v, l in graph[u]:
                if v in seen:
                    continue
                if t+l >= disappear[v]:
                    continue
                heapq.heappush(q, (t+l, v))
        return ans
                