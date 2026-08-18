'''
=== 1914. Cyclically Rotating a Grid ===

You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.
The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:
A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:
Return the matrix after applying k cyclic rotations to it.

Example 1:
    Input: grid = [[40,10],[30,20]], k = 1
    Output: [[10,20],[40,30]]
    Explanation: The figures above represent the grid at every state.
Example 2:
    Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
    Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
    Explanation: The figures above represent the grid at every state.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 2 <= m, n <= 50
    4. Both m and n are even integers.
    5. 1 <= grid[i][j] <= 5000
    6. 1 <= k <= 109
'''
# === 140ms && 14.7MB === #
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        l = min(n, m) // 2
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(l):
            s = [grid[j][i] for j in range(i, n-i)] + [grid[n-1-i][j] for j in range(i+1, m-i)] + [grid[j][m-1-i] for j in range(n-i-2,i,-1)] + [grid[i][j] for j in range(m-i-1,i,-1)]
            # print(s)
            delta = k % len(s)
            s = s[-delta:] + s[:-delta]
            idx = 0
            for j in range(i, n-i):
                res[j][i] = s[idx]
                idx += 1
            for j in range(i+1, m-i):
                res[n-1-i][j] = s[idx]
                idx += 1
            for j in range(n-i-2,i,-1):
                res[j][m-1-i] = s[idx]
                idx += 1
            for j in range(m-i-1,i,-1):
                res[i][j] = s[idx]
                idx += 1
        return res
        