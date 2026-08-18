'''
=== 3966. Count Good Integers in a Range ===

You are given three integers l, r and k.
A number is considered good if the absolute difference between every pair of adjacent digits is at most k.
Return the number of good integers in the range [l, r] (inclusive).
The absolute difference between values x and y is defined as abs(x - y).

Example 1:
    Input: l = 10, r = 15, k = 1
    Output: 3
    Explanation:
    The good integers in the range are 10, 11, and 12.
    For 10, abs(1 - 0) = 1.
    For 11, abs(1 - 1) = 0.
    For 12, abs(1 - 2) = 1.
    All these differences are at most k = 1. Thus, the answer is 3.
Example 2:
    Input: l = 201, r = 204, k = 2
    Output: 2
    Explanation:
    The good integers in the range are 201 and 202.
    For 201, abs(2 - 0) = 2 and abs(0 - 1) = 1.
    For 202, abs(2 - 0) = 2 and abs(0 - 2) = 2.
    Thus, the answer is 2.
    
Constraints:
    1. 10 <= l <= r <= 1015
    2. 0 <= k <= 9
'''
# === 175ms && 31.66MB === #
class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        
        def count_good_int(n):
            if n < 10:
                return n+1
            digits = [int(ch) for ch in str(n)]
            m = len(digits)

            @lru_cache(None)
            def dp(idx, pre, allow_larger, is_zero):
                if idx >= m:
                    return 1
                ans = 0
                if idx == 0:
                    ans += dp(1, 0, True, True)
                    for d in range(1, digits[0]):
                        ans += dp(1, d, True, False)
                    ans += dp(1, digits[0], False, False)
                elif is_zero:
                    ans += dp(idx+1, 0, True, True)
                    for d in range(1, 10):
                        ans += dp(idx+1, d, True, False)
                elif allow_larger:
                    for d in range(max(0, pre-k), min(10, pre+k+1)):
                        ans += dp(idx+1, d, True, False)
                else:
                    for d in range(max(0, pre-k), min(10, pre+k+1, digits[idx])):
                        ans += dp(idx+1, d, True, False)
                    if abs(digits[idx]-pre) <= k:
                        ans += dp(idx+1, digits[idx], False, False)
                return ans

            return dp(0, 0, False, True)


        return count_good_int(r) - count_good_int(l-1)