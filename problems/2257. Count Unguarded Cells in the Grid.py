'''
=== 2257. Count Unguarded Cells in the Grid ===

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
Return the number of unoccupied cells that are not guarded.

Example 1:
    Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
    Output: 7
    Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
    There are a total of 7 unguarded cells, so we return 7.
Example 2:
    Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
    Output: 4
    Explanation: The unguarded cells are shown in green in the above diagram.
    There are a total of 4 unguarded cells, so we return 4.
 
Constraints:
    1. 1 <= m, n <= 105
    2. 2 <= m * n <= 105
    3. 1 <= guards.length, walls.length <= 5 * 104
    4. 2 <= guards.length + walls.length <= m * n
    5. guards[i].length == walls[j].length == 2
    6. 0 <= rowi, rowj < m
    7. 0 <= coli, colj < n
    8. All the positions in guards and walls are unique.
'''
# === 5340ms && 76.7MB === #
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        status = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in guards:
            status[i][j] = 1
        for i, j in walls:
            status[i][j] = -1
            
        l2r = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            l2r[i][0] = 0 if status[i][0] != 1 else 1
            for j in range(1, n):
                if status[i][j] == -1:
                    l2r[i][j] = 0
                else:
                    l2r[i][j] = l2r[i][j-1] + status[i][j]
                
        r2l = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            r2l[i][n-1] = 0 if status[i][n-1] != 1 else 1
            for j in range(n-2, -1, -1):
                if status[i][j] == -1:
                    r2l[i][j] = 0
                else:
                    r2l[i][j] = r2l[i][j+1] + status[i][j]
                    
        t2b = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            t2b[0][j] = 0 if status[0][j] != 1 else 1
            for i in range(1, m):
                if status[i][j] == -1:
                    t2b[i][j] = 0
                else:
                    t2b[i][j] = t2b[i-1][j] + status[i][j]
                    
        b2t = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            b2t[m-1][j] = 0 if status[m-1][j] != 1 else 1
            for i in range(m-2, -1, -1):
                if status[i][j] == -1:
                    b2t[i][j] = 0
                else:
                    b2t[i][j] = b2t[i+1][j] + status[i][j]
        
        res = [(i, j) for i in range(m) for j in range(n) if status[i][j] != -1 and l2r[i][j] + r2l[i][j] + t2b[i][j] + b2t[i][j] == 0]
        return len(res)
        