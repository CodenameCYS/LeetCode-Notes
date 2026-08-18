'''
=== 2876. Count Visited Nodes in a Directed Graph ===

There is a directed graph consisting of n nodes numbered from 0 to n - 1 and n directed edges.
You are given a 0-indexed array edges where edges[i] indicates that there is an edge from node i to node edges[i].
Consider the following process on the graph:
    - You start from a node x and keep visiting other nodes through edges until you reach a node that you have already visited before on this same process.
Return an array answer where answer[i] is the number of different nodes that you will visit if you perform the process starting from node i.

Example 1:
    Input: edges = [1,2,0,0]
    Output: [3,3,3,4]
    Explanation: We perform the process starting from each node in the following way:
    - Starting from node 0, we visit the nodes 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 3.
    - Starting from node 1, we visit the nodes 1 -> 2 -> 0 -> 1. The number of different nodes we visit is 3.
    - Starting from node 2, we visit the nodes 2 -> 0 -> 1 -> 2. The number of different nodes we visit is 3.
    - Starting from node 3, we visit the nodes 3 -> 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 4.
Example 2:
    Input: edges = [1,2,3,4,0]
    Output: [5,5,5,5,5]
    Explanation: Starting from any node we can visit every node in the graph in the process.
    
Constraints:
    1. n == edges.length
    2. 2 <= n <= 105
    3. 0 <= edges[i] <= n - 1
    4. edges[i] != i
'''
# === 1542ms && 44.7MB === #
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        res = [-1 for _ in range(n)]
        
        def scan(u):
            nonlocal res
            if res[u] != -1:
                return
            visited = {}
            nodes = []
            idx = 0
            while u not in visited and res[u] == -1:
                visited[u] = idx
                nodes.append(u)
                idx += 1
                u = edges[u]
            if res[u] == -1:
                pre = visited[u]
                loop = idx - pre
                for u in nodes[pre:]:
                    res[u] = loop
                for i, u in enumerate(nodes[:pre]):
                    res[u] = loop + pre-i
            else:
                s = res[u]
                l = len(nodes)
                for i, u in enumerate(nodes):
                    res[u] = s + l-i
            return
        
        in_nodes = set(edges)
        starts = [i for i in range(n) if i not in in_nodes]
        for i, u in enumerate(starts):
            scan(u)
        for u in range(n):
            if res[u] == -1:
                scan(u)
        return res