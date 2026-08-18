'''
=== 861. Score After Flipping Matrix ===

We have a two dimensional matrix A where each value is 0 or 1.
A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score.

Example 1:
    Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    Output: 39
    Explanation:
    Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
    0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 
Note:
    1. 1 <= A.length <= 20
    2. 1 <= A[0].length <= 20
    3. A[i][j] is 0 or 1.
'''
# === 36ms(80.95%) && 14.2MB(20.41%) === #
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        for i in range(n):
            if A[i][0] != 1:
                A[i] = [1-x for x in A[i]]
        flag = 1
        ans = 0
        for j in range(m-1, -1, -1):
            s = sum([A[i][j] for i in range(n)])
            ans += flag * max(s, n-s)
            flag *= 2
        return ans