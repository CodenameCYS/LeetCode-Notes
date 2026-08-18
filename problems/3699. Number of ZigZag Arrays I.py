'''
=== 3699. Number of ZigZag Arrays I ===

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
    [5, 4, 5]​​​​​​​
Example 2:
    Input: n = 3, l = 1, r = 3
    Output: 10
    Explanation:
    There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:
    [1, 2, 1], [1, 3, 1], [1, 3, 2]
    [2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
    [3, 1, 2], [3, 1, 3], [3, 2, 3]
    All arrays meet the ZigZag conditions.

Constraints:
    1. 3 <= n <= 2000
    2. 1 <= l < r <= 2000
'''
MOD = 10**9 + 7
# === 10691ms && 18.52MB === #
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        d = r-l
        up, down = [1 for _ in range(d)] + [0], [0] + [1 for _ in range(d)] 

        for i in range(n-2, -1, -1):
            prev_up = [0 for _ in range(d+1)]
            valid = 0
            for j in range(d-1, -1, -1):
                valid = (valid + down[j+1]) % MOD
                prev_up[j] = valid
            
            prev_down = [0 for _ in range(d+1)]
            valid = 0
            for j in range(1, d+1):
                valid = (valid + up[j-1]) % MOD
                prev_down[j] = valid

            up, down = prev_up, prev_down
        return (sum(up) + sum(down)) % MOD
        