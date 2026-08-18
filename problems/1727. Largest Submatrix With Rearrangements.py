'''
=== 1727. Largest Submatrix With Rearrangements ===

You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

Example 1:
    Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
    Output: 4
    Explanation: You can rearrange the columns as shown above.
    The largest submatrix of 1s, in bold, has an area of 4.
Example 2:
    Input: matrix = [[1,0,1,0,1]]
    Output: 3
    Explanation: You can rearrange the columns as shown above.
    The largest submatrix of 1s, in bold, has an area of 3.
Example 3:
    Input: matrix = [[1,1,0],[1,0,1]]
    Output: 2
    Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
Example 4:
    Input: matrix = [[0,0],[0,0]]
    Output: 0
    Explanation: As there are no 1s, no submatrix of 1s can be formed and the area is 0.
 
Constraints:
    1. m == matrix.length
    2. n == matrix[i].length
    3. 1 <= m * n <= 105
    4. matrix[i][j] is 0 or 1.
'''
# === 1216ms(77.36%) && 38.2MB(63.64%) === #
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        up = [0 for _ in range(m)]
        res = 0
        for i in range(n):
            up = [0 if y == 0 else x+1 for x, y in zip(up, matrix[i])]
            tmp = sorted(up, reverse=True)
            for j in range(m):
                res = max(res, (j+1)*tmp[j])
                if tmp[j]== 0:
                    break
        return res
            