'''
=== 3310. Remove Methods From Project ===

You are maintaining a project that has n methods numbered from 0 to n - 1.
You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that method ai invokes method bi.
There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.
A group of methods can only be removed if no method outside the group invokes any methods within it.
Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.

Example 1:
    Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]
    Output: [0,1,2,3]
    Explanation:
    Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.
Example 2:
    Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]
    Output: [3,4]
    Explanation:
    Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.
Example 3:
    Input: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]
    Output: []
    Explanation:
    All methods are suspicious. We can remove them.

Constraints:
    1. 1 <= n <= 105
    2. 0 <= k <= n - 1
    3. 0 <= invocations.length <= 2 * 105
    4. invocations[i] == [ai, bi]
    5. 0 <= ai, bi <= n - 1
    6. ai != bi
    7. invocations[i] != invocations[j]
'''
class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x != y:
            self.root[y] = x
        return
# === 3352ms && 124.7MB === #
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        for u, v in invocations:
            dsu.union(u, v)
        u = dsu.find(k)
        remain = [i for i in range(n) if dsu.find(i) != u]
        remove = [i for i in range(n) if dsu.find(i) == u]
        # print(remain, remove)
        
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
        seen = {k}
        q = [k]
        while q != []:
            u = q.pop(0)
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        # print(seen)
        # print("=" * 10)
        return remain if len(remove) == len(seen) else [i for i in range(n)]
        