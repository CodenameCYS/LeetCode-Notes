'''
=== 3419. Minimize the Maximum Edge Weight of Graph ===

You are given two integers, n and threshold, as well as a directed weighted graph of n nodes numbered from 0 to n - 1. The graph is represented by a 2D integer array edges, where edges[i] = [Ai, Bi, Wi] indicates that there is an edge going from node Ai to node Bi with weight Wi.
You have to remove some edges from this graph (possibly none), so that it satisfies the following conditions:
    - Node 0 must be reachable from all other nodes.
    - The maximum edge weight in the resulting graph is minimized.
    - Each node has at most threshold outgoing edges.
Return the minimum possible value of the maximum edge weight after removing the necessary edges. If it is impossible for all conditions to be satisfied, return -1.

Example 1:
    Input: n = 5, edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]], threshold = 2
    Output: 1
    Explanation:
    Remove the edge 2 -> 0. The maximum weight among the remaining edges is 1.
Example 2:
    Input: n = 5, edges = [[0,1,1],[0,2,2],[0,3,1],[0,4,1],[1,2,1],[1,4,1]], threshold = 1
    Output: -1
    Explanation: 
    It is impossible to reach node 0 from node 2.
Example 3:
    Input: n = 5, edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[3,4,2],[4,0,1]], threshold = 1
    Output: 2
    Explanation: 
    Remove the edges 1 -> 3 and 1 -> 4. The maximum weight among the remaining edges is 2.
    Example 4:
    Input: n = 5, edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[4,0,1]], threshold = 1
    Output: -1

Constraints:
    1. 2 <= n <= 105
    2. 1 <= threshold <= n - 1
    3. 1 <= edges.length <= min(105, n * (n - 1) / 2).
    4. edges[i].length == 3
    5. 0 <= Ai, Bi < n
    6. Ai != Bi
    7. 1 <= Wi <= 106
    8. There may be multiple edges between a pair of nodes, but they must have unique weights.
'''
# === 1754ms && 74.3MB === #
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[v].append((u, w))
        for u in list(graph.keys()):
            graph[u] = sorted(graph[u], key=lambda x: x[1])
            
            
        def is_possbile(k):
            seen = {0}
            q = [0]
            while q:
                u = q.pop(0)
                for v, w in graph[u]:
                    if w > k:
                        break
                    if v in seen:
                        continue
                    q.append(v)
                    seen.add(v)
            return len(seen) == n
        
        i, j = 0, max(w for u, v, w in edges)
        if not is_possbile(j):
            return -1
        while j-i > 1:
            k = (i+j) // 2
            if is_possbile(k):
                j = k
            else:
                i = k
        return j
                
# === 548ms && 74.4MB === #         
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[v].append((u, w))
        
        reached = set()
        ans = 0
        q = [(0, 0)]
        while q:
            d, u = heapq.heappop(q)
            if u in reached:
                continue
            reached.add(u)
            ans = max(ans, d)
            for v, w in graph[u]:
                if v in reached:
                    continue
                nd = max(w, d)
                heapq.heappush(q, (nd, v))
        return ans if len(reached) == n else -1
            
               