'''
=== 2658. Maximum Number of Fish in a Grid ===

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
    - A land cell if grid[r][c] = 0, or
    - A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:
    - Catch all the fish at cell (r, c), or
    - Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Example 1:
    Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
    Output: 7
    Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:
    Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
    Output: 1
    Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 10
    4. 0 <= grid[i][j] <= 10
'''
# === 307ms && 16.4MB === #
class DSU:
    def __init__(self, n, m):
        self.width = m
        self.root = [i for i in range(n * m)]
        
    def _find(self, k):
        if self.root[k] == k:
            return k
        return self._find(self.root[k])
        
    def find(self, i, j):
        k = i * self.width + j
        if self.root[k] == k:
            return k
        return self._find(self.root[k])
    
    def union(self, i, j, a, b):
        x = self.find(i, j)
        y = self.find(a, b)
        if x != y:
            self.root[y] = x
        return

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        dsu = DSU(n, m)
        
        def is_water(i, j):
            return 0 <= i < n and 0 <= j < m and grid[i][j] != 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                if is_water(i+1, j):
                    dsu.union(i, j, i+1, j)
                if is_water(i, j+1):
                    dsu.union(i, j, i, j+1)
        
        cnt = defaultdict(int)
        for i in range(n):
            for j in range(m):
                cnt[dsu.find(i, j)] += grid[i][j]
        return max(cnt.values())
                
            
        