'''
=== 2846. Minimum Edge Weight Equilibrium Queries in a Tree ===

There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates that there is an edge between nodes ui and vi with weight wi in the tree.
You are also given a 2D integer array queries of length m, where queries[i] = [ai, bi]. For each query, find the minimum number of operations required to make the weight of every edge on the path from ai to bi equal. In one operation, you can choose any edge of the tree and change its weight to any value.
Note that:
    - Queries are independent of each other, meaning that the tree returns to its initial state on each new query.
    - The path from ai to bi is a sequence of distinct nodes starting with node ai and ending with node bi such that every two adjacent nodes in the sequence share an edge in the tree.
Return an array answer of length m where answer[i] is the answer to the ith query.

Example 1:
    Input: n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]
    Output: [0,0,1,3]
    Explanation: In the first query, all the edges in the path from 0 to 3 have a weight of 1. Hence, the answer is 0.
    In the second query, all the edges in the path from 3 to 6 have a weight of 2. Hence, the answer is 0.
    In the third query, we change the weight of edge [2,3] to 2. After this operation, all the edges in the path from 2 to 6 have a weight of 2. Hence, the answer is 1.
    In the fourth query, we change the weights of edges [0,1], [1,2] and [2,3] to 2. After these operations, all the edges in the path from 0 to 6 have a weight of 2. Hence, the answer is 3.
    For each queries[i], it can be shown that answer[i] is the minimum number of operations needed to equalize all the edge weights in the path from ai to bi.
Example 2:
    Input: n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]
    Output: [1,2,2,3]
    Explanation: In the first query, we change the weight of edge [1,3] to 6. After this operation, all the edges in the path from 4 to 6 have a weight of 6. Hence, the answer is 1.
    In the second query, we change the weight of edges [0,3] and [3,1] to 6. After these operations, all the edges in the path from 0 to 4 have a weight of 6. Hence, the answer is 2.
    In the third query, we change the weight of edges [1,3] and [5,2] to 6. After these operations, all the edges in the path from 6 to 5 have a weight of 6. Hence, the answer is 2.
    In the fourth query, we change the weights of edges [0,7], [0,3] and [1,3] to 6. After these operations, all the edges in the path from 7 to 4 have a weight of 6. Hence, the answer is 3.
    For each queries[i], it can be shown that answer[i] is the minimum number of operations needed to equalize all the edge weights in the path from ai to bi.
 
Constraints:
    1. 1 <= n <= 104
    2. edges.length == n - 1
    3. edges[i].length == 3
    4. 0 <= ui, vi < n
    5. 1 <= wi <= 26
    6. The input is generated such that edges represents a valid tree.
    7. 1 <= queries.length == m <= 2 * 104
    8. queries[i].length == 2
    9. 0 <= ai, bi < n
'''
# === 5775ms && 434.5MB === #
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        if n == 1:
            return [0 for _ in queries]
        
        graph = defaultdict(list)
        weights = defaultdict(int)
        for u, v, w in edges:
            graph[u].append(v)
            graph[v].append(u)
            weights[(u, v)] = w
            weights[(v, u)] = w
            
        for i in range(n):
            if len(graph[i]) == 1:
                u0 = i
                break
                
        parent = {u0: -1}
        nodes = {u0: tuple([0 for _ in range(26)])}
        paths = {u0: [u0]}
        
        def dfs(u):
            nonlocal parent, nodes, paths
            val = list(nodes[u])
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                w = weights[(u, v)]
                val[w-1] += 1
                nodes[v] = tuple(val)
                val[w-1] -= 1
                paths[v] = paths[u] + [v]
                dfs(v)
            return
        
        dfs(u0)

        def get_latest_ancestor(u, v):
            n = min(len(paths[u]), len(paths[v]))
            if paths[u][n-1] == paths[v][n-1]:
                return paths[u][n-1]
            i, j = 0, n-1
            while j-i > 1:
                m = (i+j) // 2
                if paths[u][m] == paths[v][m]:
                    i = m
                else:
                    j = m
            return paths[u][i]

        def query(u, v):
            p = get_latest_ancestor(u, v)
            path = [x+y-2*z for x,y,z in zip(nodes[u], nodes[v], nodes[p])]
            return sum(path) - max(path)
        
        return [query(u, v) for u, v in queries]
            
# === 5087ms && 432.4MB === #              
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        if n == 1:
            return [0 for _ in queries]
        
        graph = defaultdict(list)
        weights = defaultdict(int)
        for u, v, w in edges:
            graph[u].append(v)
            graph[v].append(u)
            weights[(u, v)] = w
            weights[(v, u)] = w
            
        _max = 0
        for i in range(n):
            if len(graph[i]) > _max:
                u0 = i
                
        parent = {u0: -1}
        nodes = {u0: tuple([0 for _ in range(26)])}
        paths = {u0: [u0]}
        
        def dfs(u):
            nonlocal parent, nodes, paths
            val = list(nodes[u])
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                w = weights[(u, v)]
                val[w-1] += 1
                nodes[v] = tuple(val)
                val[w-1] -= 1
                paths[v] = paths[u] + [v]
                dfs(v)
            return
        
        dfs(u0)

        def get_latest_ancestor(u, v):
            n = min(len(paths[u]), len(paths[v]))
            if paths[u][n-1] == paths[v][n-1]:
                return paths[u][n-1]
            i, j = 0, n-1
            while j-i > 1:
                m = (i+j) // 2
                if paths[u][m] == paths[v][m]:
                    i = m
                else:
                    j = m
            return paths[u][i]

        def query(u, v):
            p = get_latest_ancestor(u, v)
            path = [x+y-2*z for x,y,z in zip(nodes[u], nodes[v], nodes[p])]
            return sum(path) - max(path)
        
        return [query(u, v) for u, v in queries]
            
                
            
        
        
            
                
            
        