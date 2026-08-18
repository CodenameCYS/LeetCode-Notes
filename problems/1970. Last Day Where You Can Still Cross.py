'''
=== 1970. Last Day Where You Can Still Cross ===

There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.
Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).
You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).
Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

Example 1:
    Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
    Output: 2
    Explanation: The above image depicts how the matrix changes each day starting from day 0.
    The last day where it is possible to cross from top to bottom is on day 2.
Example 2:
    Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
    Output: 1
    Explanation: The above image depicts how the matrix changes each day starting from day 0.
    The last day where it is possible to cross from top to bottom is on day 1.
Example 3:
    Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
    Output: 3
    Explanation: The above image depicts how the matrix changes each day starting from day 0.
    The last day where it is possible to cross from top to bottom is on day 3.
 
Constraints:
    1. 2 <= row, col <= 2 * 104
    2. 4 <= row * col <= 2 * 104
    3. cells.length == row * col
    4. 1 <= ri <= row
    5. 1 <= ci <= col
    6. All the values of cells are unique.
'''
class DSU:
    def __init__(self, row, col):
        self.dsu = {(i, j): (i, j) for i in range(row) for j in range(col)}
        self.dsu["bg"] = "bg"
        self.dsu["ed"] = "ed"
        for j in range(col):
            self.union("bg", (0, j))
            self.union("ed", (row-1, j))
    
    def find(self, p):
        if self.dsu[p] == p:
            return p
        self.dsu[p] = self.find(self.dsu[p])
        return self.dsu[p]
    
    def union(self, p1, p2):
        p1 = self.find(p1)
        p2 = self.find(p2)
        self.dsu[p1] = p2
        return
    
    def can_cross(self):
        return self.find("bg") == self.find("ed")
# === 2164ms && 26.3MB === #
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = len(cells)
        dsu = DSU(row, col)
        seen = set()
        for idx, (r, c) in enumerate(cells[::-1]):
            r, c = r-1, c-1
            seen.add((r, c))
            if (r-1, c) in seen:
                dsu.union((r, c), (r-1, c))
            if (r+1, c) in seen:
                dsu.union((r, c), (r+1, c))
            if (r, c-1) in seen:
                dsu.union((r, c), (r, c-1))
            if (r, c+1) in seen:
                dsu.union((r, c), (r, c+1))
            if dsu.can_cross():
                return n-1-idx