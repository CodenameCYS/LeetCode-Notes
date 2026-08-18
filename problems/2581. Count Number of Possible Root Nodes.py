'''
=== 2581. Count Number of Possible Root Nodes ===

Alice has an undirected tree with n nodes labeled from 0 to n - 1. The tree is represented as a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
Alice wants Bob to find the root of the tree. She allows Bob to make several guesses about her tree. In one guess, he does the following:
    - Chooses two distinct integers u and v such that there exists an edge [u, v] in the tree.
    - He tells Alice that u is the parent of v in the tree.
Bob's guesses are represented by a 2D integer array guesses where guesses[j] = [uj, vj] indicates Bob guessed uj to be the parent of vj.
Alice being lazy, does not reply to each of Bob's guesses, but just says that at least k of his guesses are true.
Given the 2D integer arrays edges, guesses and the integer k, return the number of possible nodes that can be the root of Alice's tree. If there is no such tree, return 0.

Example 1:
    Input: edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3
    Output: 3
    Explanation: 
    Root = 0, correct guesses = [1,3], [0,1], [2,4]
    Root = 1, correct guesses = [1,3], [1,0], [2,4]
    Root = 2, correct guesses = [1,3], [1,0], [2,4]
    Root = 3, correct guesses = [1,0], [2,4]
    Root = 4, correct guesses = [1,3], [1,0]
    Considering 0, 1, or 2 as root node leads to 3 correct guesses.
Example 2:
    Input: edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1
    Output: 5
    Explanation: 
    Root = 0, correct guesses = [3,4]
    Root = 1, correct guesses = [1,0], [3,4]
    Root = 2, correct guesses = [1,0], [2,1], [3,4]
    Root = 3, correct guesses = [1,0], [2,1], [3,2], [3,4]
    Root = 4, correct guesses = [1,0], [2,1], [3,2]
    Considering any node as root will give at least 1 correct guess. 

Constraints:
    1. edges.length == n - 1
    2. 2 <= n <= 105
    3. 1 <= guesses.length <= 105
    4. 0 <= ai, bi, uj, vj <= n - 1
    5. ai != bi
    6. uj != vj
    7. edges represents a valid tree.
    8. guesses[j] is an edge of the tree.
    9. guesses is unique.
    10. 0 <= k <= guesses.length
'''
# === 2205ms && 194.1MB === #
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        guesses = {(u,v) for u, v in guesses}
        
        # get matched questions when 0 is root.
        cnt = 0
        q = [0]
        seen = set()
        while q != []:
            u = q.pop(0)
            seen.add(u)
            for v in graph[u]:
                if v in seen:
                    continue
                if (u, v) in guesses:
                    cnt += 1
                q.append(v)
        
        # traverse and count the matched question when each node become root.
        seen = set()
        res = 0
        def dfs(u, cnt):
            nonlocal seen, res
            if u in seen:
                return 
            if cnt >= k:
                res += 1
            seen.add(u)
            for v in graph[u]:
                if (u, v) in guesses:
                    if (v, u) in guesses:
                        dfs(v, cnt)
                    else:
                        dfs(v, cnt-1)
                else:
                    if (v, u) in guesses:
                        dfs(v, cnt+1)
                    else:
                        dfs(v, cnt)
            return
        
        dfs(0, cnt)
        return res
        
        