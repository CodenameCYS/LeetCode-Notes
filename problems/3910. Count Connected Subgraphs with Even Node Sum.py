'''
=== 3910. Count Connected Subgraphs with Even Node Sum ===

You are given an undirected graph with n nodes labeled from 0 to n - 1. Node i has a value of nums[i], which is either 0 or 1. The edges of the graph are given by a 2D array edges where edges[i] = [ui, vi] represents an edge between node ui and node vi.
For a non-empty subset s of nodes in the graph, we consider the induced subgraph of s generated as follows:
    - We keep only the nodes in s.
    - We keep only the edges whose two endpoints are both in s.
Return an integer representing the number of non-empty subsets s of nodes in the graph such that:
    - The induced subgraph of s is connected.
    - The sum of node values in s is even.
 
Example 1:
    Input: nums = [1,0,1], edges = [[0,1],[1,2]]
    Output: 2
    Explanation:
    s	connected?	sum of node values	counted?
    [0]	Yes	1	No
    [1]	Yes	0	Yes
    [2]	Yes	1	No
    [0,1]	Yes	1	No
    [0,2]	No, node 0 and node 2 are disconnected.	2	No
    [1,2]	Yes	1	No
    [0,1,2]	Yes	2	Yes
Example 2:
    Input: nums = [1], edges = []
    Output: 0
    Explanation:
    s	connected?	sum of node values	counted?
    [0]	Yes	1	No
 
Constraints:
    1. 1 <= n == nums.length <= 13
    2. nums[i] is 0 or 1.
    3. 0 <= edges.length <= n * (n - 1) / 2
    4. edges[i] = [ui, vi]
    5. 0 <= ui < vi < n
    6. All edges are distinct.
'''
# === 319ms && 19.42MB === #
class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def is_connected(status):
            nodes = [i for i in range(n) if status & (1 << i) != 0]
            q = [nodes[0]]
            connected, candi = {nodes[0]}, set(nodes)
            while q:
                u = q.pop(0)
                for v in graph[u]:
                    if v not in candi or v in connected:
                        continue
                    q.append(v)
                    connected.add(v)
            return len(connected) == len(nodes)

        def is_valid(status):
            tot = 0
            for i in range(n):
                if status & (1<<i) != 0:
                    tot += nums[i]
            if tot % 2 == 1:
                return False
            return is_connected(status)

        ans = 0
        for status in range(1, 2**n):
            if is_valid(status):
                ans += 1
        return ans