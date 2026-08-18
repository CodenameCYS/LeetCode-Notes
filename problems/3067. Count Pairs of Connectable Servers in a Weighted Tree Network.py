'''
=== 3067. Count Pairs of Connectable Servers in a Weighted Tree Network ===

You are given an unrooted weighted tree with n vertices representing servers numbered from 0 to n - 1, an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional edge between vertices ai and bi of weight weighti. You are also given an integer signalSpeed.
Two servers a and b are connectable through a server c if:
    - a < b, a != c and b != c.
    - The distance from c to a is divisible by signalSpeed.
    - The distance from c to b is divisible by signalSpeed.
    - The path from c to b and the path from c to a do not share any edges.
Return an integer array count of length n where count[i] is the number of server pairs that are connectable through the server i.

Example 1:
    Input: edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1
    Output: [0,4,6,6,4,0]
    Explanation: Since signalSpeed is 1, count[c] is equal to the number of pairs of paths that start at c and do not share any edges.
    In the case of the given path graph, count[c] is equal to the number of servers to the left of c multiplied by the servers to the right of c.
Example 2:
    Input: edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3
    Output: [2,0,0,0,0,0,2]
    Explanation: Through server 0, there are 2 pairs of connectable servers: (4, 5) and (4, 6).
    Through server 6, there are 2 pairs of connectable servers: (4, 5) and (0, 5).
    It can be shown that no two servers are connectable through servers other than 0 and 6.
 
Constraints:
    1. 2 <= n <= 1000
    2. edges.length == n - 1
    3. edges[i].length == 3
    4. 0 <= ai, bi < n
    5. edges[i] = [ai, bi, weighti]
    6. 1 <= weighti <= 106
    7. 1 <= signalSpeed <= 106
    8. The input is generated such that edges represents a valid tree.
'''
# === 292ms && 38.7MB === #
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges)+1
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        # print(graph)
            
        @lru_cache(None)
        def dfs(u, pre, distance):
            ans =  1 if distance == 0 else 0
            for v, w in graph[u]:
                if v == pre:
                    continue
                ans += dfs(v, u, (distance + w) % signalSpeed)
            return ans
        
        def count_connectable(u):
            cnt = [dfs(v, u, w % signalSpeed) for v, w in graph[u]]
            # print(u, cnt)
            s = sum(cnt)
            ans = sum([x * (s-x) for x in cnt]) // 2
            return ans
        
        return [count_connectable(u) for u in range(n)]
                