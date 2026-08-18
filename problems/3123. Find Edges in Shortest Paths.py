'''
=== 3123. Find Edges in Shortest Paths ===

You are given an undirected weighted graph of n nodes numbered from 0 to n - 1. The graph consists of m edges represented by a 2D array edges, where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.
Consider all the shortest paths from node 0 to node n - 1 in the graph. You need to find a boolean array answer where answer[i] is true if the edge edges[i] is part of at least one shortest path. Otherwise, answer[i] is false.
Return the array answer.
Note that the graph may not be connected.

Example 1:
    Input: n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
    Output: [true,true,true,false,true,true,true,false]
    Explanation:
    The following are all the shortest paths between nodes 0 and 5:
    The path 0 -> 1 -> 5: The sum of weights is 4 + 1 = 5.
    The path 0 -> 2 -> 3 -> 5: The sum of weights is 1 + 1 + 3 = 5.
    The path 0 -> 2 -> 3 -> 1 -> 5: The sum of weights is 1 + 1 + 2 + 1 = 5.
Example 2:
    Input: n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]
    Output: [true,false,false,true]
    Explanation:
    There is one shortest path between nodes 0 and 3, which is the path 0 -> 2 -> 3 with the sum of weights 1 + 2 = 3.

Constraints:
    1. 2 <= n <= 5 * 104
    2. m == edges.length
    3. 1 <= m <= min(5 * 104, n * (n - 1) / 2)
    4. 0 <= ai, bi < n
    5. ai != bi
    6. 1 <= wi <= 105
    7. There are no repeated edges.
'''
# === 1911ms && 50.8MB === #
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for i, (u, v, w) in enumerate(edges):
            graph[u].append((v, w, i))
            graph[v].append((u, w, i))
            
        ans = [False for _ in edges]
        distances = [math.inf for _ in range(n)]
        q = [(0, 0, [])]
        while q != []:
            dis, u, edges = heapq.heappop(q)
            if dis > distances[u]:
                continue
            distances[u] = dis
            for v, w, e in graph[u]:
                if dis + w <= distances[v]:
                    heapq.heappush(q, (dis+w, v, edges + [e]))
            if u == n-1:
                for e in edges:
                    ans[e] = True
        return ans