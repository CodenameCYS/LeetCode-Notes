'''
=== 2959. Number of Possible Sets of Closing Branches ===

There is a company with n branches across the country, some of which are connected by roads. Initially, all branches are reachable from each other by traveling some roads.
The company has realized that they are spending an excessive amount of time traveling between their branches. As a result, they have decided to close down some of these branches (possibly none). However, they want to ensure that the remaining branches have a distance of at most maxDistance from each other.
The distance between two branches is the minimum total traveled length needed to reach one branch from another.
You are given integers n, maxDistance, and a 0-indexed 2D array roads, where roads[i] = [ui, vi, wi] represents the undirected road between branches ui and vi with length wi.
Return the number of possible sets of closing branches, so that any branch has a distance of at most maxDistance from any other.
Note that, after closing a branch, the company will no longer have access to any roads connected to it.
Note that, multiple roads are allowed.

Example 1:
    Input: n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]
    Output: 5
    Explanation: The possible sets of closing branches are:
    - The set [2], after closing, active branches are [0,1] and they are reachable to each other within distance 2.
    - The set [0,1], after closing, the active branch is [2].
    - The set [1,2], after closing, the active branch is [0].
    - The set [0,2], after closing, the active branch is [1].
    - The set [0,1,2], after closing, there are no active branches.
    It can be proven, that there are only 5 possible sets of closing branches.
Example 2:
    Input: n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
    Output: 7
    Explanation: The possible sets of closing branches are:
    - The set [], after closing, active branches are [0,1,2] and they are reachable to each other within distance 4.
    - The set [0], after closing, active branches are [1,2] and they are reachable to each other within distance 2.
    - The set [1], after closing, active branches are [0,2] and they are reachable to each other within distance 2.
    - The set [0,1], after closing, the active branch is [2].
    - The set [1,2], after closing, the active branch is [0].
    - The set [0,2], after closing, the active branch is [1].
    - The set [0,1,2], after closing, there are no active branches.
    It can be proven, that there are only 7 possible sets of closing branches.
Example 3:
    Input: n = 1, maxDistance = 10, roads = []
    Output: 2
    Explanation: The possible sets of closing branches are:
    - The set [], after closing, the active branch is [0].
    - The set [0], after closing, there are no active branches.
    It can be proven, that there are only 2 possible sets of closing branches.
 
Constraints:
    1. 1 <= n <= 10
    2. 1 <= maxDistance <= 105
    3. 0 <= roads.length <= 1000
    4. roads[i].length == 3
    5. 0 <= ui, vi <= n - 1
    6. ui != vi
    7. 1 <= wi <= 1000
    8. All branches are reachable from each other by traveling some roads.
'''
# === 9116ms && 49.2MB === #
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        paths = {}
        for u, v, w in roads:
            if w > maxDistance:
                continue
            if (u, v) in paths:
                paths[(u, v)] = min(paths[(u, v)], w)
                paths[(v, u)] = min(paths[(u, v)], w)
            else:
                paths[(u, v)] = w
                paths[(v, u)] = w
                graph[u].append(v)
                graph[v].append(u)
                
        @lru_cache(None)
        def get_subgraph(status):
            nodes = set()
            for i in range(n):
                if status & 1 == 1:
                    nodes.add(i)
                status = status >> 1
            subgraph = defaultdict(list)
            for k, v in graph.items():
                if k not in nodes:
                    continue
                subgraph[k] = [o for o in v if o in nodes]
            subpaths = {(u, v): w for (u, v), w in paths.items() if u in nodes and v in nodes}
            return subgraph, subpaths, nodes
                
        @lru_cache(None)
        def get_min_distance(status):
            distances = [[0 if i == j else math.inf for i in range(n)] for j in range(n)]
            
            subgraph, subpaths, nodes = get_subgraph(status)
            if len(nodes) <= 1:
                return distances
            
            for (u, v), w in subpaths.items():
                distances[u][v] = distances[v][u] = w
            
            for o in range(n):
                for u in range(n):
                    for v in range(n):
                        distances[u][v] = min(distances[u][o] + distances[o][v], distances[u][v])
                        distances[v][u] = min(distances[u][o] + distances[o][v], distances[v][u])
            return distances

        @lru_cache(None)
        def dfs(idx, status):
            if idx == n:
                distances = get_min_distance(status)
                subgraph, subpaths, nodes = get_subgraph(status)
                nodes = list(nodes)
                m = len(nodes)
                return 1 if all(distances[nodes[i]][nodes[j]] <= maxDistance for i in range(m-1) for j in range(i+1, m)) else 0
            return dfs(idx+1, status) + dfs(idx+1, status | (1 << idx))
            
        return dfs(0, 0)
                
# === 8546ms && 53.1MB === #
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        roads = sorted(roads, key=lambda x: x[-1])
        valid_roads = []
        seen = set()
        for u, v, w in roads:
            if (u, v) in seen:
                continue
            if w > maxDistance:
                break
            valid_roads.append((u, v, w))
            seen.add((u, v))
            seen.add((v, u))
                
        @lru_cache(None)
        def get_min_distance(status):
            distances = [[0 if i == j else math.inf for i in range(n)] for j in range(n)]
            
            for u, v, w in valid_roads:
                if ((status >> u) & 1) & ((status >> v) & 1):
                    distances[u][v] = distances[v][u] = w

            for o in range(n):
                for u in range(n):
                    for v in range(n):
                        distances[u][v] = min(distances[u][o] + distances[o][v], distances[u][v])
                        distances[v][u] = min(distances[u][o] + distances[o][v], distances[v][u])
            return distances

        @lru_cache(None)
        def dfs(idx, status):
            if idx == n:
                distances = get_min_distance(status)
                return 1 if all(distances[u][v] <= maxDistance for u in range(n) for v in range(u+1, n) if ((status >> u) & 1) & ((status >> v) & 1)) else 0
            return dfs(idx+1, status) + dfs(idx+1, status | (1 << idx))
            
        return dfs(0, 0)
                
            
            
        
        
            
        