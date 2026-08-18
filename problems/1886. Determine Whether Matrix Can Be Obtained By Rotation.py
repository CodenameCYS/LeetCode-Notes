'''
=== 1886. Determine Whether Matrix Can Be Obtained By Rotation ===

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:
    Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
    Output: true
    Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:
    Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
    Output: false
    Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
    Output: true
    Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 
Constraints:
    1. n == mat.length == target.length
    2. n == mat[i].length == target[i].length
    3. 1 <= n <= 10
    4. mat[i][j] and target[i][j] are either 0 or 1.
'''
# === 40ms && 14.3MB === #
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        def rotate(mat):
            res = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    res[j][n-1-i] = mat[i][j]
            return res
        
        if all(mat[i][j] == target[i][j] for i in range(n) for j in range(n)):
            return True
        for _ in range(3):
            mat = rotate(mat)
            if all(mat[i][j] == target[i][j] for i in range(n) for j in range(n)):
                return True
        return False
        