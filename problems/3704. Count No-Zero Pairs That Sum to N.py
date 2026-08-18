'''
=== 3704. Count No-Zero Pairs That Sum to N ===

A no-zero integer is a positive integer that does not contain the digit 0 in its decimal representation.
Given an integer n, count the number of pairs (a, b) where:
    - a and b are no-zero integers.
    - a + b = n
Return an integer denoting the number of such pairs.

Example 1:
    Input: n = 2
    Output: 1
    Explanation:
    The only pair is (1, 1).
Example 2:
    Input: n = 3
    Output: 2
    Explanation:
    The pairs are (1, 2) and (2, 1).
Example 3:
    Input: n = 11
    Output: 8
    Explanation:
    The pairs are (2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3), and (9, 2). Note that (1, 10) and (10, 1) do not satisfy the conditions because 10 contains 0 in its decimal representation.

Constraints:
    1. 2 <= n <= 1015
'''
# === 73ms && 18.45MB === #
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = str(n)
        l = len(s)

        @lru_cache(None)
        def dp(idx, r, is_num1_empty, is_num2_empty):
            if idx >= l:
                return 0 if (r != 0 or is_num1_empty or is_num2_empty) else 1
            tgt = int(s[idx]) + 10 * r
            if tgt <= 1 and (not is_num1_empty) and (not is_num2_empty):
                return 0
            ans = 0
            for i in range(min(tgt+1, 10)):
                j = tgt-i
                if 0 < i < 10 and 0 < j < 10:
                    ans += dp(idx+1, 0, False, False)
                elif is_num1_empty and i == 0 and 0 < j < 10:
                    ans += dp(idx+1, 0, True, False)
                elif is_num2_empty and j == 0 and 0 < i < 10:
                    ans += dp(idx+1, 0, False, True)

                j = tgt-1-i
                if 0 < i < 10 and 0 < j < 10:
                    ans += dp(idx+1, 1, False, False)
                elif is_num1_empty and i == 0 and 0 < j < 10:
                    ans += dp(idx+1, 1, True, False)
                elif is_num2_empty and j == 0 and 0 < i < 10:
                    ans += dp(idx+1, 1, False, True)
                elif is_num1_empty and is_num2_empty and i == 0 and j == 0:
                    ans += dp(idx+1, 1, True, True)
            return ans
        
        return dp(0, 0, True, True)

