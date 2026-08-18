'''
=== 2812. Find the Safest Path in a Grid ===

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
    - A cell containing a thief if grid[r][c] = 1
    - An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.
The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.
Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).
An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.
The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

Example 1:
    Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
    Output: 0
    Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
Example 2:
    Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
    Output: 2
    Explanation: The path depicted in the picture above has a safeness factor of 2 since:
    - The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
    It can be shown that there are no other paths with a higher safeness factor.
Example 3:
    Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
    Output: 2
    Explanation: The path depicted in the picture above has a safeness factor of 2 since:
    - The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
    - The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
    It can be shown that there are no other paths with a higher safeness factor.
 
Constraints:
    1. 1 <= grid.length == n <= 400
    2. grid[i].length == n
    3. grid[i][j] is either 0 or 1.
    4. There is at least one thief in the grid.
'''
class DSU:
    def __init__(self, n):
        self.root = {(i,j): (i,j) for i in range(n) for j in range(n)}
        
    def find(self, p):
        if self.root[p] != p:
            self.root[p] = self.find(self.root[p])
        return self.root[p]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.root[y] = x
        return
# === 5276ms && 90.3MB === #
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        factors = [[0 for _ in range(n)] for _ in range(n)]
        q = [[i, j, 0] for i in range(n) for j in range(n) if grid[i][j] == 1]
        seen = {(i, j) for i, j, _ in q}
        while q:
            i, j, d = q.pop(0)
            # print(i, j, d, seen)
            if i-1 >= 0 and (i-1, j) not in seen:
                factors[i-1][j] = d+1
                q.append((i-1, j, d+1))
                seen.add((i-1, j))
            if i+1 < n and (i+1, j) not in seen:
                factors[i+1][j] = d+1
                q.append((i+1, j, d+1))
                seen.add((i+1, j))
            if j-1 >= 0 and (i, j-1) not in seen:
                factors[i][j-1] = d+1
                q.append((i, j-1, d+1))
                seen.add((i, j-1))
            if j+1 < n and (i, j+1) not in seen:
                factors[i][j+1] = d+1
                q.append((i, j+1, d+1))
                seen.add((i, j+1))
        # print(factors)
        
        dsu = DSU(n)
        s = sorted([(i, j) for i in range(n) for j in range(n)], key=lambda x: factors[x[0]][x[1]], reverse=True)
        for i, j in s:
            if i-1 >= 0 and factors[i-1][j] >= factors[i][j]:
                dsu.union((i-1, j), (i, j))
            if i+1 < n and factors[i+1][j] >= factors[i][j]:
                dsu.union((i+1, j), (i, j))
            if j-1 >= 0 and factors[i][j-1] >= factors[i][j]:
                dsu.union((i, j-1), (i, j))
            if j+1 < n and factors[i][j+1] >= factors[i][j]:
                dsu.union((i, j+1), (i, j))
            if dsu.find((0, 0)) == dsu.find((n-1, n-1)):
                return factors[i][j]
        return 0
        
        