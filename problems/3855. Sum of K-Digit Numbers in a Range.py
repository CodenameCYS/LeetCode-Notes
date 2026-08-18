'''
=== 3855. Sum of K-Digit Numbers in a Range ===

You are given three integers l, r, and k.
Consider all possible integers consisting of exactly k digits, where each digit is chosen independently from the integer range [l, r] (inclusive). If 0 is included in the range, leading zeros are allowed.
Return an integer representing the sum of all such numbers.​​​​​​​ Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: l = 1, r = 2, k = 2
    Output: 66
    Explanation:
    All numbers formed using k = 2 digits in the range [1, 2] are 11, 12, 21, 22.
    The total sum is 11 + 12 + 21 + 22 = 66.
Example 2:
    Input: l = 0, r = 1, k = 3
    Output: 444
    Explanation:
    All numbers formed using k = 3 digits in the range [0, 1] are 000, 001, 010, 011, 100, 101, 110, 111​​​​​​​.
    These numbers without leading zeros are 0, 1, 10, 11, 100, 101, 110, 111.
    The total sum is 444.
Example 3:
    Input: l = 5, r = 5, k = 10
    Output: 555555520
    Explanation:​​​​​​​
    5555555555 is the only valid number consisting of k = 10 digits in the range [5, 5].
    The total sum is 5555555555 % (109 + 7) = 555555520.
 
Constraints:
    1. 0 <= l <= r <= 9
    2. 1 <= k <= 109
'''
MOD = 10**9+7
# === 59ms && 22.98MB === #
class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        m = pow(r-l+1, k-1, mod=MOD)

        @lru_cache(None)
        def dp(n):
            if n == 1:
                return 1
            n1, n2 = n // 2, n-(n//2)
            return (dp(n1) * pow(10, n2, mod=MOD) + dp(n2)) % MOD
        t = dp(k)
        # t = 1
        # for _ in range(k-1):
        #     t = t * 10 + 1
        
        return ((l+r) * (r-l+1) // 2 * m * t) % MOD