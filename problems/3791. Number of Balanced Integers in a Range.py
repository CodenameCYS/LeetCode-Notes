'''
=== 3791. Number of Balanced Integers in a Range ===

You are given two integers low and high.
An integer is called balanced if it satisfies both of the following conditions:
    - It contains at least two digits.
    - The sum of digits at even positions is equal to the sum of digits at odd positions (the leftmost digit has position 1).
Return an integer representing the number of balanced integers in the range [low, high] (both inclusive).

Example 1:
    Input: low = 1, high = 100
    Output: 9
    Explanation:
    The 9 balanced numbers between 1 and 100 are 11, 22, 33, 44, 55, 66, 77, 88, and 99.
Example 2:
    Input: low = 120, high = 129
    Output: 1
    Explanation:
    Only 121 is balanced because the sum of digits at even and odd positions are both 2.
Example 3:
    Input: low = 1234, high = 1234
    Output: 0
    Explanation:
    1234 is not balanced because the sum of digits at odd positions (1 + 3 = 4) does not equal the sum at even positions (2 + 4 = 6).

Constraints:
    1. 1 <= low <= high <= 1015
'''
# === 1129ms && 25.79MB === #
class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        
        def count_balanced(num):
            if num <= 10:
                return 0
            digits = [int(digit) for digit in str(num)]
            n = len(digits)

            @lru_cache(None)
            def dp(idx, is_zero, allow_bigger, flag, delta):
                if idx == n-1:
                    if is_zero:
                        return 0
                    need = -delta if flag == 1 else delta
                    if allow_bigger and (0 <= need <= 9):
                        return 1
                    elif not allow_bigger and (0 <= need <= digits[-1]):
                        return 1
                    else:
                        return 0
                if flag == 1 and ((n-idx+1)//2) * 9 + delta < 0:
                    return 0
                elif flag == -1 and -((n-idx+1)//2) * 9 + delta > 0:
                    return 0
                
                if is_zero:
                    ans = dp(idx+1, True, True, 1, 0)
                    if allow_bigger:
                        for i in range(1, 10):
                            ans += dp(idx+1, False, True, -1, i)
                    else:
                        for i in range(1, digits[idx]):
                            ans += dp(idx+1, False, True, -1, i)
                        ans += dp(idx+1, False, False, -1, digits[idx])
                else:
                    ans = 0
                    if allow_bigger:
                        for i in range(10):
                            ans += dp(idx+1, False, True, -flag, delta + flag*i)
                    else:
                        for i in range(digits[idx]):
                            ans += dp(idx+1, False, True, -flag, delta + flag*i)
                        ans += dp(idx+1, False, False, -flag, delta + flag*digits[idx])
                return ans

            ans = dp(0, True, False, 1, 0)
            # print(f"count_balanced({num}) = {ans}")
            return ans

        return count_balanced(high) - count_balanced(low-1)
