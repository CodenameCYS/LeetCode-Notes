'''
=== 3529. Count Cells in Overlapping Horizontal and Vertical Substrings ===

You are given an m x n matrix grid consisting of characters and a string pattern.
A horizontal substring is a contiguous sequence of characters read from left to right. If the end of a row is reached before the substring is complete, it wraps to the first column of the next row and continues as needed. You do not wrap from the bottom row back to the top.
A vertical substring is a contiguous sequence of characters read from top to bottom. If the bottom of a column is reached before the substring is complete, it wraps to the first row of the next column and continues as needed. You do not wrap from the last column back to the first.
Count the number of cells in the matrix that satisfy the following condition:
    - The cell must be part of at least one horizontal substring and at least one vertical substring, where both substrings are equal to the given pattern.
Return the count of these cells.

Example 1:
    Input: grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","c","c"]], pattern = "abaca"
    Output: 1
    Explanation:
    The pattern "abaca" appears once as a horizontal substring (colored blue) and once as a vertical substring (colored red), intersecting at one cell (colored purple).
Example 2:
    Input: grid = [["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]], pattern = "aba"
    Output: 4
    Explanation:
    The cells colored above are all part of at least one horizontal and one vertical substring matching the pattern "aba".
Example 3:
    Input: grid = [["a"]], pattern = "a"
    Output: 1

Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 1000
    4. 1 <= m * n <= 105
    5. 1 <= pattern.length <= m * n
    6. grid and pattern consist of only lowercase English letters.
'''
def z_algorithm(s):
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = -1, -1
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r-l] == s[r]:
                r += 1
            z[i] = r-l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r-l] == s[r]:
                    r += 1
                z[i] = r-l
                r -= 1
    z[0] = n
    return z
# === 699ms && 64.3MB === #
class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        n, m = len(grid), len(grid[0])
        l = len(pattern)
        
        s1 = set()
        horizontal = "".join([grid[i][j] for i in range(n) for j in range(m)])
        z = z_algorithm(pattern + horizontal)[l:]
        # print(horizontal, z)
        valid = 0
        for i, c in enumerate(z):
            row, col = i // m, i % m
            if c >= l:
                valid = i + l
            if i < valid:
                s1.add((row, col))
        # print(s1)
        
        vertical = "".join([grid[i][j] for j in range(m) for i in range(n)])
        z = z_algorithm(pattern + vertical)[l:]
        # print(vertical, z)
        valid = 0
        s2 = set()
        for i, c in enumerate(z):
            row, col = i % n, i // n
            if c >= l:
                valid = i + l
            if i < valid:
                s2.add((row, col))
        # print(s2)
                
        return len(s1 & s2)