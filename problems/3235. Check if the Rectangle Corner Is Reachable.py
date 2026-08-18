'''
=== 3235. Check if the Rectangle Corner Is Reachable ===

You are given two positive integers X and Y, and a 2D array circles, where circles[i] = [xi, yi, ri] denotes a circle with center at (xi, yi) and radius ri.
There is a rectangle in the coordinate plane with its bottom left corner at the origin and top right corner at the coordinate (X, Y). You need to check whether there is a path from the bottom left corner to the top right corner such that the entire path lies inside the rectangle, does not touch or lie inside any circle, and touches the rectangle only at the two corners.
Return true if such a path exists, and false otherwise.

Example 1:
    Input: X = 3, Y = 4, circles = [[2,1,1]]
    Output: true
    Explanation:
    The black curve shows a possible path between (0, 0) and (3, 4).
Example 2:
    Input: X = 3, Y = 3, circles = [[1,1,2]]
    Output: false
    Explanation:
    No path exists from (0, 0) to (3, 3).
Example 3:
    Input: X = 3, Y = 3, circles = [[2,1,1],[1,2,1]]
    Output: false
    Explanation:
    No path exists from (0, 0) to (3, 3).

Constraints:
    1. 3 <= X, Y <= 109
    2. 1 <= circles.length <= 1000
    3. circles[i].length == 3
    4. 1 <= xi, yi, ri <= 109
'''
# === 3644ms && 17.4MB === #
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
        return

class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        dsu = DSU(n)
        for i in range(n-1):
            x1, y1, r1 = circles[i]
            for j in range(i+1, n):
                x2, y2, r2 = circles[j]
                if math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r1+r2:
                    dsu.union(i, j)
        
        def is_blocked(lbound, rbound, dbound, ubound):
            if lbound <= 0 and rbound >= X:
                return True
            elif dbound <= 0 and ubound >= Y:
                return True
            elif lbound <= X <= rbound and dbound <= Y <= ubound:
                return True
            elif lbound <= 0 <= rbound and dbound <= 0 <= ubound:
                return True
            return False
        
        boundary = {}
        for i in range(n):
            x, y, r = circles[i]
            c = dsu.find(i)
            if c not in boundary:
                boundary[c] = [x-r, x+r, y-r, y+r]
            else:
                boundary[c][0] = min(boundary[c][0], x-r)
                boundary[c][1] = max(boundary[c][1], x+r)
                boundary[c][2] = min(boundary[c][2], y-r)
                boundary[c][3] = max(boundary[c][3], y+r)
            if is_blocked(*boundary[c]):
                return False
        return True