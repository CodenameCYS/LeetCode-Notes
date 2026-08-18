'''
=== 1916. Count Ways to Build Rooms in an Ant Colony ===

You are an ant tasked with adding n new rooms numbered 0 to n-1 to your colony. You are given the expansion plan as a 0-indexed integer array of length n, prevRoom, where prevRoom[i] indicates that you must build room prevRoom[i] before building room i, and these two rooms must be connected directly. Room 0 is already built, so prevRoom[0] = -1. The expansion plan is given such that once all the rooms are built, every room will be reachable from room 0.
You can only build one room at a time, and you can travel freely between rooms you have already built only if they are connected. You can choose to build any room as long as its previous room is already built.
Return the number of different orders you can build all the rooms in. Since the answer may be large, return it modulo 109 + 7.

Example 1:
    Input: prevRoom = [-1,0,1]
    Output: 1
    Explanation: There is only one way to build the additional rooms: 0 → 1 → 2
Example 2:
    Input: prevRoom = [-1,0,0,1,2]
    Output: 6
    Explanation:
    The 6 ways are:
    0 → 1 → 3 → 2 → 4
    0 → 2 → 4 → 1 → 3
    0 → 1 → 2 → 3 → 4
    0 → 1 → 2 → 4 → 3
    0 → 2 → 1 → 3 → 4
    0 → 2 → 1 → 4 → 3
 
Constraints:
    1. n == prevRoom.length
    2. 2 <= n <= 105
    3. prevRoom[0] == -1
    4. 0 <= prevRoom[i] < n for all 1 <= i < n
    5. Every room is reachable from room 0 once all the rooms are built.
'''
# === 3928ms && 55MB === #
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9+7
        n = len(prevRoom)
        
        def get_topological_seq(prevRoom):
            deg = Counter(prevRoom)
            nodes = [u for u in range(n) if u not in deg]
            i, m = 0, len(nodes)
            while i < m:
                u = nodes[i]
                v = prevRoom[u]
                deg[v] -= 1
                if v != -1 and deg[v] == 0:
                    nodes.append(v)
                    m += 1
                i += 1
            return nodes
        
        def get_subtree_size(nodes, prevRoom):
            sizes = [1 for _ in range(n)]
            for u in nodes[:-1]:
                sizes[prevRoom[u]] += sizes[u]
            return sizes
        
        def get_graph(prevRoom):
            graph = defaultdict(list)
            for u, v in enumerate(prevRoom):
                graph[v].append(u)
            return graph
        
        def get_factorial(n):
            f = [1 for _ in range(n+1)]
            for i in range(2, n+1):
                f[i] = (f[i-1] * i) % MOD
            g = [pow(x, -1, MOD) for x in f]
            return f, g
        
        nodes = get_topological_seq(prevRoom)
        # print("nodes: ", nodes)
        sizes = get_subtree_size(nodes, prevRoom)
        # print("sizes: ", sizes)
        graph = get_graph(prevRoom)
        # print("graph: ", graph)
        f, g = get_factorial(n)
        # print("f, g: ", f, g)
        dp = [f[sizes[i]-1] for i in range(n)]
        for u in nodes:
            if graph[u] == []:
                continue
            for v in graph[u]:
                dp[u] = (dp[u] * dp[v] * g[sizes[v]]) % MOD
        # print("dp: ", dp)
        return dp[0]