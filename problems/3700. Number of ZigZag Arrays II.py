'''
=== 3700. Number of ZigZag Arrays II ===

You are given three integers n, l, and r.
A ZigZag array of length n is defined as follows:
    - Each element lies in the range [l, r].
    - No two adjacent elements are equal.
    - No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.
Since the answer may be large, return it modulo 109 + 7.
A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).
A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

Example 1:
    Input: n = 3, l = 4, r = 5
    Output: 2
    Explanation:
    There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:
    [4, 5, 4]
    [5, 4, 5]
Example 2:
    Input: n = 3, l = 1, r = 3
    Output: 10
    Explanation:
    ​​​​​​​There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:
    [1, 2, 1], [1, 3, 1], [1, 3, 2]
    [2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
    [3, 1, 2], [3, 1, 3], [3, 2, 3]
    All arrays meet the ZigZag conditions.

Constraints:
    1. 3 <= n <= 109
    2. 1 <= l < r <= 75​​​​​​​
'''
MOD = 10**9 + 7

def mul(A, B):
    return [[sum(x*y for x,y in zip(row, col)) % MOD for col in zip(*B)] for row in A]
    
def pow_mul(a: List[List[int]], n: int, f1: List[List[int]]) -> List[List[int]]:
    res = f1
    while n:
        if n & 1:
            res = [sum(x*y for x, y in zip(row, res)) for row in a]
        a = mul(a, a)
        n >>= 1
    return res
# === 12495ms && 19.52MB === #    
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        d = r-l+1
        vec = [1 for _ in range(d-1)] + [0] + [0] + [1 for _ in range(d-1)] 

        M = [[0 for _ in range(2*d)] for _ in range(2*d)]
        for i in range(d):
            for j in range(i+1, d):
                M[i][d+j] = 1
            for j in range(i):
                M[i+d][j] = 1

        res = pow_mul(M, n-1, vec)
        return sum(res) % MOD
    
# === 4045ms && 31.78MB === #
import numpy as np
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        d = r-l+1
        vec = [1 for _ in range(d-1)] + [0] + [0] + [1 for _ in range(d-1)] 
        vec = np.array(vec, dtype=object)

        M = [[0 for _ in range(2*d)] for _ in range(2*d)]
        for i in range(d):
            for j in range(i+1, d):
                M[i][d+j] = 1
            for j in range(i):
                M[i+d][j] = 1
        M = np.array(M, dtype=object)

        def pow_mul(M, vec, n):
            res = vec
            while n:
                if n % 2 == 1:
                    res = (M @ res) % MOD
                M = (M @ M) % MOD
                n = n // 2
            return res                

        res = pow_mul(M, vec, n-1)
        return sum(res) % MOD