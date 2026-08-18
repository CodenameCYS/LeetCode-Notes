'''
=== 3747. Count Distinct Integers After Removing Zeros ===

You are given a positive integer n.
For every integer x from 1 to n, we write down the integer obtained by removing all zeros from the decimal representation of x.
Return an integer denoting the number of distinct integers written down.

Example 1:
    Input: n = 10
    Output: 9
    Explanation:
    The integers we wrote down are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1. There are 9 distinct integers (1, 2, 3, 4, 5, 6, 7, 8, 9).
Example 2:
    Input: n = 3
    Output: 3
    Explanation:
    The integers we wrote down are 1, 2, 3. There are 3 distinct integers (1, 2, 3).

Constraints:
    1. 1 <= n <= 1015
'''
# === 6ms && 18.12MB === #
class Solution:
    def countDistinct(self, n: int) -> int:
        
        s = str(n)
        l = len(s)

        @lru_cache(None)
        def dp(idx, allow_bigger, is_zero):
            if idx >= l:
                return 1 if not is_zero else 0
            if allow_bigger:
                if is_zero:
                    ans = 0
                    for i in range(1, l-idx+1):
                        ans += 9**i
                    return ans
                else:
                    return 9**(l-idx)
            elif s[idx] == '0':
                return 0
            elif is_zero:
                return dp(idx+1, True, True) + (int(s[idx])-1) * dp(idx+1, True, False) + dp(idx+1, False, False)
            else:
                return (int(s[idx])-1) * dp(idx+1, True, False) + dp(idx+1, False, False)

        return dp(0, False, True)

