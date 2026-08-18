'''
=== 959. Regions Cut By Slashes ===

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.
(Note that backslash characters are escaped, so a \ is represented as "\\".)
Return the number of regions.

Example 1:
    Input:
    [
        " /",
        "/ "
    ]
    Output: 2
    Explanation: The 2x2 grid is as follows:
Example 2:
    Input:
    [
        " /",
        "  "
    ]
    Output: 1
    Explanation: The 2x2 grid is as follows:
Example 3:
    Input:
    [
        "\\/",
        "/\\"
    ]
    Output: 4
    Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
    The 2x2 grid is as follows:
Example 4:
    Input:
    [
        "/\\",
        "\\/"
    ]
    Output: 5
    Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
    The 2x2 grid is as follows:
Example 5:
    Input:
    [
        "//",
        "/ "
    ]
    Output: 3
    Explanation: The 2x2 grid is as follows:

Note:
    1. 1 <= grid.length == grid[0].length <= 30
    2. grid[i][j] is either '/', '\', or ' '.
'''
class DSU:
    def __init__(self, n):
        self.dsu = [i for i in range(n)]
        
    def find(self, x):
        if x == self.dsu[x]:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.dsu[yr] = xr
        return
    
    def count_groups(self):
        return len([1 for i, x in enumerate(self.dsu) if x == i])

# === 148ms(89.25%) && 14.3MB(60.98%) === #
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])
        dsu = DSU(4*n*m)
        for i in range(n):
            for j in range(m):
                flag = 4*(i*m + j)
                if grid[i][j] == '/':
                    dsu.union(flag, flag+3)
                    dsu.union(flag+1, flag+2)
                elif grid[i][j] == '\\':
                    dsu.union(flag, flag+1)
                    dsu.union(flag+2, flag+3)
                else:
                    dsu.union(flag, flag+1)
                    dsu.union(flag, flag+2)
                    dsu.union(flag, flag+3)
                if j != m-1:
                    dsu.union(flag+2, flag+4)
                if i != n-1:
                    dsu.union(flag+1, flag+3+4*m)
        return dsu.count_groups()
                    