'''
=== 2316. Count Unreachable Pairs of Nodes in an Undirected Graph ===

You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
Return the number of pairs of different nodes that are unreachable from each other.

Example 1:
    Input: n = 3, edges = [[0,1],[0,2],[1,2]]
    Output: 0
    Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:
    Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    Output: 14
    Explanation: There are 14 pairs of nodes that are unreachable from each other:
    [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
    Therefore, we return 14.
 
Constraints:
    1. 1 <= n <= 105
    2. 0 <= edges.length <= 2 * 105
    3. edges[i].length == 2
    4. 0 <= ai, bi < n
    5. ai != bi
    6. There are no repeated edges.
'''
class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        
    def find(self, k):
        if self.root[k] == k:
            return k
        self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
        return
# === 4812ms && 43.9MB === #
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        
        cnt = defaultdict(int)
        for i in range(n):
            cnt[dsu.find(i)] += 1
        # print(cnt)    
        
        res = 0
        for u in cnt:
            res += cnt[u] * (n - cnt[u])
        return res // 2