'''
=== 2318. Number of Distinct Roll Sequences ===

You are given an integer n. You roll a fair 6-sided dice n times. Determine the total number of distinct sequences of rolls possible such that the following conditions are satisfied:
    - The greatest common divisor of any adjacent values in the sequence is equal to 1.
    - There is at least a gap of 2 rolls between equal valued rolls. More formally, if the value of the ith roll is equal to the value of the jth roll, then abs(i - j) > 2.
Return the total number of distinct sequences possible. Since the answer may be very large, return it modulo 109 + 7.
Two sequences are considered distinct if at least one element is different.

Example 1:
    Input: n = 4
    Output: 184
    Explanation: Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc.
    Some invalid sequences are (1, 2, 1, 3), (1, 2, 3, 6).
    (1, 2, 1, 3) is invalid since the first and third roll have an equal value and abs(1 - 3) = 2 (i and j are 1-indexed).
    (1, 2, 3, 6) is invalid since the greatest common divisor of 3 and 6 = 3.
    There are a total of 184 distinct sequences possible, so we return 184.
Example 2:
    Input: n = 2
    Output: 22
    Explanation: Some of the possible sequences are (1, 2), (2, 1), (3, 2).
    Some invalid sequences are (3, 6), (2, 4) since the greatest common divisor is not equal to 1.
    There are a total of 22 distinct sequences possible, so we return 22.
 
Constraints:
    1. 1 <= n <= 104
'''
# === 5259ms && 528.3MB === #
class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            elif b == 0:
                return a
            a, b = b, a%b
            return gcd(a, b)
        
        @lru_cache(None)
        def dp(idx, pre1, pre2):
            if idx >= n:
                return 1
            elif idx == 0:
                return sum(dp(1, i, 0) for i in range(1, 7)) % MOD
            elif idx == 1:
                res = 0
                for i in range(1, 7):
                    if i != pre1 and gcd(i, pre1) == 1:
                        res = (res + dp(idx+1, i, pre1)) % MOD
                return res % MOD
            res = 0
            for i in range(1, 7):
                if i != pre1 and gcd(i, pre1) == 1 and i != pre2:
                    res = (res + dp(idx+1, i, pre1)) % MOD
            return res % MOD
        
        return dp(0, -1, -1)