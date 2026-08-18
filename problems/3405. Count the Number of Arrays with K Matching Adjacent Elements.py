'''
=== 3405. Count the Number of Arrays with K Matching Adjacent Elements ===

You are given three integers n, m, k. A good array arr of size n is defined as follows:
    - Each element in arr is in the inclusive range [1, m].
    - Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
Return the number of good arrays that can be formed.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: n = 3, m = 2, k = 1
    Output: 4
    Explanation:
    There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
    Hence, the answer is 4.
Example 2:
    Input: n = 4, m = 2, k = 2
    Output: 6
    Explanation:
    The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
    Hence, the answer is 6.
Example 3:
    Input: n = 5, m = 2, k = 0
    Output: 2
    Explanation:
    The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
 
Constraints:
    1. 1 <= n <= 105
    2. 1 <= m <= 105
    3. 0 <= k <= n - 1
'''
MOD = 10**9+7

Factorials = [1 for _ in range(10**5+1)]
Revs = [1 for _ in range(10**5+1)]
for i in range(2, 10**5+1):
    Factorials[i] = (i * Factorials[i-1]) % MOD
    Revs[i] = pow(Factorials[i], -1, mod = MOD)

def C(n, m):
    return (Factorials[n] * Revs[m] * Revs[n-m]) % MOD if n >= m else 0

# === 0ms && 25.5MB === #
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return (m * pow(m-1, n-k-1, mod=MOD) * C(n-1, k)) % MOD
        