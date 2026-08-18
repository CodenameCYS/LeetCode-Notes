'''
=== 1782. Count Pairs Of Nodes ===

You are given an undirected graph represented by an integer n, which is the number of nodes, and edges, where edges[i] = [ui, vi] which indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.
The answer to the jth query is the number of pairs of nodes (a, b) that satisfy the following conditions:
    - a < b
    - cnt is strictly greater than queries[j], where cnt is the number of edges incident to a or b.
Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.
Note that there can be repeated edges.

Example 1:
    Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
    Output: [6,5]
    Explanation: The number of edges incident to at least one of each pair is shown above.
Example 2:
    Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
    Output: [10,10,9,8,6]
 
Constraints:
    1. 2 <= n <= 2 * 104
    2. 1 <= edges.length <= 105
    3. 1 <= ui, vi <= n
    4. ui != vi
    5. 1 <= queries.length <= 20
    6. 0 <= queries[j] < edges.length
'''
# === 3352ms && 61.5MB === #
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        pcnt = [0 for _ in range(n+1)]
        ecnt = defaultdict(int)
        for u, v in edges:
            pcnt[u] += 1
            pcnt[v] += 1
            u, v = (u, v) if u < v else (v, u)
            ecnt[(u, v)] += 1
        plist = sorted(pcnt[1:])
        
        def fn(q):
            res = 0
            for i, d in enumerate(plist):
                idx = bisect.bisect_right(plist, q-d)
                if idx <= i:
                    res += n-idx-1
                else:
                    res += n-idx
            res = res // 2
            for u, v in ecnt:
                if pcnt[u] + pcnt[v] > q and pcnt[u] + pcnt[v] - ecnt[(u, v)] <= q:
                    res -= 1
            return res
        
        return [fn(q) for q in queries]