'''
=== 3593. Minimum Increments to Equalize Leaf Paths ===

You are given an integer n and an undirected tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an edge from node ui to vi .
Each node i has an associated cost given by cost[i], representing the cost to traverse that node.
The score of a path is defined as the sum of the costs of all nodes along the path.
Your goal is to make the scores of all root-to-leaf paths equal by increasing the cost of any number of nodes by any non-negative amount.
Return the minimum number of nodes whose cost must be increased to make all root-to-leaf path scores equal.

Example 1:
    Input: n = 3, edges = [[0,1],[0,2]], cost = [2,1,3]
    Output: 1
    Explanation:
    There are two root-to-leaf paths:
    Path 0 → 1 has a score of 2 + 1 = 3.
    Path 0 → 2 has a score of 2 + 3 = 5.
    To make all root-to-leaf path scores equal to 5, increase the cost of node 1 by 2.
    Only one node is increased, so the output is 1.
Example 2:
    Input: n = 3, edges = [[0,1],[1,2]], cost = [5,1,4]
    Output: 0
    Explanation:
    There is only one root-to-leaf path:
    Path 0 → 1 → 2 has a score of 5 + 1 + 4 = 10.
    Since only one root-to-leaf path exists, all path costs are trivially equal, and the output is 0.
Example 3:
    Input: n = 5, edges = [[0,4],[0,1],[1,2],[1,3]], cost = [3,4,1,1,7]
    Output: 1
    Explanation:
    There are three root-to-leaf paths:
    Path 0 → 4 has a score of 3 + 7 = 10.
    Path 0 → 1 → 2 has a score of 3 + 4 + 1 = 8.
    Path 0 → 1 → 3 has a score of 3 + 4 + 1 = 8.
    To make all root-to-leaf path scores equal to 10, increase the cost of node 1 by 2. Thus, the output is 1.

Constraints:
    1. 2 <= n <= 105
    2. edges.length == n - 1
    3. edges[i] == [ui, vi]
    4. 0 <= ui, vi < n
    5. cost.length == n
    6. 1 <= cost[i] <= 109
    7. The input is generated such that edges represents a valid tree.
'''
# === 791ms && 88.46MB === #
class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        tree = defaultdict(list)
        def dfs1(u, p):
            nonlocal tree
            for v in graph[u]:
                if v == p:
                    continue
                tree[u].append(v)
                dfs1(v, u)
            return
        dfs1(0, -1)

        weights = deepcopy(cost)
        def dfs2(u):
            nonlocal weights
            w = 0
            for v in tree[u]:
                w = max(w, dfs2(v))
            weights[u] += w
            return weights[u]
        dfs2(0)

        def dfs3(u):
            if len(tree[u]) == 0:
                return 0
            w = max(weights[v] for v in tree[u])
            ans = 0
            for v in tree[u]:
                ans += dfs3(v) if weights[v] == w else 1 + dfs3(v)
            return ans

        return dfs3(0)

