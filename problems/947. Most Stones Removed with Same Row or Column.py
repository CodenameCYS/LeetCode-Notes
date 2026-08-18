'''
=== 947. Most Stones Removed with Same Row or Column ===

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
What is the largest possible number of moves we can make?

Example 1:
    Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output: 5
Example 2:
    Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    Output: 3
Example 3:
    Input: stones = [[0,0]]
    Output: 0
 
Note:
    1. 1 <= stones.length <= 1000
    2. 0 <= stones[i][j] < 10000
'''
class DSU:
    def __init__(self):
        self.dsu = {}
        
    def add(self, x):
        if x not in self.dsu:
            self.dsu[x] = x
        return
    
    def find(self, x):
        if self.dsu[x] == x:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.dsu[yr] = xr
        return
    
    def count_groups(self):
        return len([1 for s in self.dsu if s == self.dsu[s]])
# === 148ms(97.27%) && 14.8MB(24.09%) === #    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = DSU()
        stones = [tuple(x) for x in stones]
        for s in stones:
            dsu.add(s)
        stones = sorted(stones, key=lambda x:x[0])
        for i in range(n-1):
            if stones[i][0] == stones[i+1][0]:
                dsu.union(stones[i], stones[i+1])
        stones = sorted(stones, key=lambda x:x[1])
        for i in range(n-1):
            if stones[i][1] == stones[i+1][1]:
                dsu.union(stones[i], stones[i+1])
        return n - dsu.count_groups()