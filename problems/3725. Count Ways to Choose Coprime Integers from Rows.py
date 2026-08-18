'''
=== 3725. Count Ways to Choose Coprime Integers from Rows ===

You are given a m x n matrix mat of positive integers.
Return an integer denoting the number of ways to choose exactly one integer from each row of mat such that the greatest common divisor of all chosen integers is 1.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: mat = [[1,2],[3,4]]
    Output: 3
    Explanation:
    Chosen integer in the first row	Chosen integer in the second row	Greatest common divisor of chosen integers
    1	3	1
    1	4	1
    2	3	1
    2	4	2
    3 of these combinations have a greatest common divisor of 1. Therefore, the answer is 3.
Example 2:
    Input: mat = [[2,2],[2,2]]
    Output: 0
    Explanation:
    Every combination has a greatest common divisor of 2. Therefore, the answer is 0.

Constraints:
    1. 1 <= m == mat.length <= 150
    2. 1 <= n == mat[i].length <= 150
    3. 1 <= mat[i][j] <= 150
'''
MOD = 10**9+7
# === 1770ms && 25.96MB === #
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        @lru_cache(None)
        def dp(idx, _gcd):
            if _gcd == 1:
                return pow(m, n-idx, mod=MOD)
            elif idx == n:
                return 0
            ans = 0
            for i in range(m):
                ans = (ans + dp(idx+1, gcd(_gcd, mat[idx][i]))) % MOD
            return ans

        ans = 0
        for i in range(m):
            ans = (ans + dp(1, mat[0][i])) % MOD
        return ans