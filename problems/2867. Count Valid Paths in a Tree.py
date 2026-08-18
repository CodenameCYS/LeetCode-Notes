'''
=== 2867. Count Valid Paths in a Tree ===

There is an undirected tree with n nodes labeled from 1 to n. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree.
Return the number of valid paths in the tree.
A path (a, b) is valid if there exists exactly one prime number among the node labels in the path from a to b.

Note that:
    - The path (a, b) is a sequence of distinct nodes starting with node a and ending with node b such that every two adjacent nodes in the sequence share an edge in the tree.
    - Path (a, b) and path (b, a) are considered the same and counted only once.
 
Example 1:
    Input: n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
    Output: 4
    Explanation: The pairs with exactly one prime number on the path between them are: 
    - (1, 2) since the path from 1 to 2 contains prime number 2. 
    - (1, 3) since the path from 1 to 3 contains prime number 3.
    - (1, 4) since the path from 1 to 4 contains prime number 2.
    - (2, 4) since the path from 2 to 4 contains prime number 2.
    It can be shown that there are only 4 valid paths.
Example 2:
    Input: n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
    Output: 6
    Explanation: The pairs with exactly one prime number on the path between them are: 
    - (1, 2) since the path from 1 to 2 contains prime number 2.
    - (1, 3) since the path from 1 to 3 contains prime number 3.
    - (1, 4) since the path from 1 to 4 contains prime number 2.
    - (1, 6) since the path from 1 to 6 contains prime number 3.
    - (2, 4) since the path from 2 to 4 contains prime number 2.
    - (3, 6) since the path from 3 to 6 contains prime number 3.
    It can be shown that there are only 6 valid paths.
 
Constraints:
    1. 1 <= n <= 105
    2. edges.length == n - 1
    3. edges[i].length == 2
    4. 1 <= ui, vi <= n
    5. The input is generated such that edges represent a valid tree.
'''
# === 1683ms && 71.2MB === #
@lru_cache(None)
def get_primes():
    n = 10**5
    status = [0 for _ in range(n)]
    primes = []
    for i in range(2, n):
        if status[i] == 1:
            continue
        primes.append(i)
        for j in range(i, n, i):
            status[j] = 1
    return primes

PRIMES = get_primes()

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        
        primes = PRIMES[:bisect.bisect_right(PRIMES, n)]
        prime_set = set(primes)

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        @lru_cache(None)
        def dfs(u, pre):
            res = 1
            for v in graph[u]:
                if v != pre and v not in prime_set:
                    res += dfs(v, u)
            return res
        
        def query(u):
            nodes = [dfs(v, -1) for v in graph[u] if v not in prime_set]
            res = 0
            s = sum(nodes)
            for k in nodes:
                res += k * (s-k)
            return res // 2 + s
            

        return sum(query(u) for u in primes)