'''
=== 2267. Check if There Is a Valid Parentheses String Path ===

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
    - It is ().
    - It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    - It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:
    - The path starts from the upper left cell (0, 0).
    - The path ends at the bottom-right cell (m - 1, n - 1).
    - The path only ever moves down or right.
    - The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

Example 1:
    Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
    Output: true
    Explanation: The above diagram shows two possible paths that form valid parentheses strings.
    The first path shown results in the valid parentheses string "()(())".
    The second path shown results in the valid parentheses string "((()))".
    Note that there may be other valid parentheses string paths.
Example 2:
    Input: grid = [[")",")"],["(","("]]
    Output: false
    Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 100
    4. grid[i][j] is either '(' or ')'.
'''
# === 815ms && 15.8MB === #
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        if grid[0][0] == ")" or grid[-1][-1] == "(":
            return False
        
        seen = {(1, 0, 0)}
        q = [(1, 0, 0)]
        while q:
            cnt, i, j = heapq.heappop(q)
            if i == n-1 and j == m-1:
                return cnt == 0
            if i+1 < n:
                if grid[i+1][j] == "(":
                    if (cnt+1, i+1, j) in seen:
                        continue
                    heapq.heappush(q, (cnt+1, i+1, j))
                    seen.add((cnt+1, i+1, j))
                else:
                    if cnt > 0:
                        if (cnt+1, i+1, j) in seen:
                            continue
                        heapq.heappush(q, (cnt-1, i+1, j))
                        seen.add((cnt-1, i+1, j))
            if j+1 < m:
                if grid[i][j+1] == "(":
                    if (cnt+1, i, j+1) in seen:
                        continue
                    heapq.heappush(q, (cnt+1, i, j+1))
                    seen.add((cnt+1, i, j+1))
                else:
                    if cnt > 0:
                        if (cnt-1, i, j+1) in seen:
                            continue
                        heapq.heappush(q, (cnt-1, i, j+1))
                        seen.add((cnt-1, i, j+1))
        return False