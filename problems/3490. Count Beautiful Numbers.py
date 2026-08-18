'''
=== 3490. Count Beautiful Numbers ===

You are given two positive integers, l and r. A positive integer is called beautiful if the product of its digits is divisible by the sum of its digits.
Return the count of beautiful numbers between l and r, inclusive.

Example 1:
    Input: l = 10, r = 20
    Output: 2
    Explanation:
    The beautiful numbers in the range are 10 and 20.
Example 2:
    Input: l = 1, r = 15
    Output: 10
    Explanation:
    The beautiful numbers in the range are 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.

Constraints:
    1. 1 <= l <= r < 109
'''
# === 637ms && 64.6MB === #
class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        
        def count_beatiful_numbers(num):
            if num <= 10:
                return num
            
            num_str = str(num)
            n = len(num_str)
            
            @lru_cache(None)
            def dp(idx, _sum, _prod, allow_larger, is_all_leading_zeros):
                if idx >= n:
                    return 1 if _sum == 0 and _prod == 1 else 0
                elif _sum == 0:
                    return 1
                elif 9 * (n-idx) < _sum:
                    return 0
                
                if allow_larger:
                    ans = 0
                    if is_all_leading_zeros:
                        ans += dp(idx+1, _sum, _prod, allow_larger, True)
                        for i in range(1, min(10, _sum+1)):
                            ans += dp(idx+1, _sum-i, _prod // gcd(_prod, i), True, False)
                    else:
                        for i in range(min(10, _sum+1)):
                            ans += dp(idx+1, _sum-i, _prod // gcd(_prod, i), True, False)
                else:
                    digit = int(num_str[idx])
                    ans = 0
                    if is_all_leading_zeros:
                        if digit == 0:
                            ans += dp(idx+1, _sum, _prod, False, True)
                        else:
                            ans += dp(idx+1, _sum, _prod, True, True)
                        for i in range(1, min(digit, _sum+1)):
                            ans += dp(idx+1, _sum-i, _prod // gcd(_prod, i), True, False)
                        if digit != 0 and digit <= _sum:
                            ans += dp(idx+1, _sum-digit, _prod // gcd(_prod, digit), False, False)
                    else:
                        for i in range(min(digit, _sum+1)):
                            ans += dp(idx+1, _sum-i, _prod // gcd(_prod, i), True, False)
                        if digit <= _sum:
                            ans += dp(idx+1, _sum-digit, _prod // gcd(_prod, digit), False, False)
                return ans
            
            ans = 0
            for i in range(1, 82):
                ans += dp(0, i, i, False, True)
            return ans
        
        return count_beatiful_numbers(r) - count_beatiful_numbers(l-1)