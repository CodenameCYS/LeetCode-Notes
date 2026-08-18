'''
=== 417. Pacific Atlantic Water Flow ===

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
- The order of returned grid coordinates does not matter.
- Both m and n are less than 150.
 
Example:
Given the following 5x5 matrix:
  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''
# === 288ms(90.37%) && 13.8MB(100%) === #
class Solution:
    def find_shore(self, matrix, stack):
        shore = set()
        n = len(matrix)
        m = len(matrix[0])
        while stack != []:
            x,y = stack.pop()
            shore.add((x,y))
            if x-1 >= 0 and matrix[x-1][y] >= matrix[x][y] and (x-1, y) not in shore:
                stack.append((x-1, y))
            if x+1 < n and matrix[x+1][y] >= matrix[x][y] and (x+1, y) not in shore:
                stack.append((x+1, y))
            if y-1 >= 0 and matrix[x][y-1] >= matrix[x][y] and (x, y-1) not in shore:
                stack.append((x, y-1))
            if y+1 < m and matrix[x][y+1] >= matrix[x][y] and (x, y+1) not in shore:
                stack.append((x, y+1))
        return shore
    
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if matrix == []:
            return []
        n = len(matrix)
        m = len(matrix[0])
        stack = [(0, j) for j in range(m)] + [(i, 0) for i in range(1,n)]
        # print(stack, end = "  -->  ")
        s1 = self.find_shore(matrix, stack)
        # print(s1)
        stack = [(n-1, j) for j in range(m)] + [(i, m-1) for i in range(n-1)]
        # print(stack, end = "  -->  ")
        s2 = self.find_shore(matrix, stack)
        # print(s2)
        ans = s1 & s2
        # print(ans)
        return [list(it) for it in ans]