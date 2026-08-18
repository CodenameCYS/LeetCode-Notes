''' 
=== 2246. Longest Path With Different Adjacent Characters ===

You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.
You are also given a string s of length n, where s[i] is the character assigned to node i.
Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

Example 1:
    Input: parent = [-1,0,0,1,1,2], s = "abacbe"
    Output: 3
    Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
    It can be proven that there is no longer path that satisfies the conditions. 
Example 2:
    Input: parent = [-1,0,0,0], s = "aabc"
    Output: 3
    Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
 
Constraints:
    1. n == parent.length == s.length
    2. 1 <= n <= 105
    3. 0 <= parent[i] <= n - 1 for all i >= 1
    4. parent[0] == -1
    5. parent represents a valid tree.
    6. s consists of only lowercase English letters.
'''
# === 1987ms && 156.5MB === #
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        childrens = defaultdict(list)
        for i in range(1, n):
            childrens[parent[i]].append(i)
        # print(childrens)
        
        res = 1
        def dfs(u):
            nonlocal res
            paths = []
            for v in childrens[u]:
                l = dfs(v)
                if s[u] != s[v]:
                    paths.append(l)
            paths = sorted(paths, reverse=True)
            if len(paths) == 0:
                return 1
            elif len(paths) == 1:
                res = max(res, paths[0]+1)
            else:
                res = max(res, paths[0]+1+paths[1])
            return 1 + paths[0] if paths != [] else 1
        
        dfs(0)
        return res
        