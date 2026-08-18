'''
=== 3530. Maximum Profit from Valid Topological Order in DAG ===

You are given a Directed Acyclic Graph (DAG) with n nodes labeled from 0 to n - 1, represented by a 2D array edges, where edges[i] = [ui, vi] indicates a directed edge from node ui to vi. Each node has an associated score given in an array score, where score[i] represents the score of node i.
You must process the nodes in a valid topological order. Each node is assigned a 1-based position in the processing order.
The profit is calculated by summing up the product of each node's score and its position in the ordering.
Return the maximum possible profit achievable with an optimal topological order.
A topological order of a DAG is a linear ordering of its nodes such that for every directed edge u → v, node u comes before v in the ordering.

Example 1:
    Input: n = 2, edges = [[0,1]], score = [2,3]
    Output: 8
    Explanation:
    Node 1 depends on node 0, so a valid order is [0, 1].
    Node	Processing Order	Score	Multiplier	Profit Calculation
    0	1st	2	1	2 × 1 = 2
    1	2nd	3	2	3 × 2 = 6
    The maximum total profit achievable over all valid topological orders is 2 + 6 = 8.
Example 2:
    Input: n = 3, edges = [[0,1],[0,2]], score = [1,6,3]
    Output: 25
    Explanation:
    Nodes 1 and 2 depend on node 0, so the most optimal valid order is [0, 2, 1].
    Node	Processing Order	Score	Multiplier	Profit Calculation
    0	1st	1	1	1 × 1 = 1
    2	2nd	3	2	3 × 2 = 6
    1	3rd	6	3	6 × 3 = 18
    The maximum total profit achievable over all valid topological orders is 1 + 6 + 18 = 25.

Constraints:
    1. 1 <= n == score.length <= 22
    2. 1 <= score[i] <= 105
    3. 0 <= edges.length <= n * (n - 1) / 2
    4. edges[i] == [ui, vi] denotes a directed edge from ui to vi.
    5. 0 <= ui, vi < n
    6. ui != vi
    7. The input graph is guaranteed to be a DAG.
    8. There are no duplicate edges.
'''
# === 214ms && 24.3MB === #
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        if len(edges) == 0:
            return sum((i+1) * x for i, x in enumerate(sorted(score)))
        
        need = defaultdict(int)
        for u, v in edges:
            need[v]  = need[v] | (1 << u)
                 
        @lru_cache(None)
        def dp(idx, visited):
            if idx > n:
                return 0
            ans = 0
            state = 1
            for i in range(n):
                if (visited & state == 0) and (need[i] & visited == need[i]):
                    ans = max(ans, idx * score[i] + dp(idx+1, visited | state))     
                state = state << 1
            return ans
        
        return dp(1, 0)