'''
=== 3753. Total Waviness of Numbers in Range II ===

You are given two integers num1 and num2 representing an inclusive range [num1, num2].
The waviness of a number is defined as the total count of its peaks and valleys:
    - A digit is a peak if it is strictly greater than both of its immediate neighbors.
    - A digit is a valley if it is strictly less than both of its immediate neighbors.
    - The first and last digits of a number cannot be peaks or valleys.
    - Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].
 
Example 1:
    Input: num1 = 120, num2 = 130
    Output: 3
    Explanation:
    In the range [120, 130]:
    120: middle digit 2 is a peak, waviness = 1.
    121: middle digit 2 is a peak, waviness = 1.
    130: middle digit 3 is a peak, waviness = 1.
    All other numbers in the range have a waviness of 0.
    Thus, total waviness is 1 + 1 + 1 = 3.
Example 2:
    Input: num1 = 198, num2 = 202
    Output: 3
    Explanation:
    In the range [198, 202]:
    198: middle digit 9 is a peak, waviness = 1.
    201: middle digit 0 is a valley, waviness = 1.
    202: middle digit 0 is a valley, waviness = 1.
    All other numbers in the range have a waviness of 0.
    Thus, total waviness is 1 + 1 + 1 = 3.
Example 3:
    Input: num1 = 4848, num2 = 4848
    Output: 2
    Explanation:
    Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

Constraints:
    1. 1 <= num1 <= num2 <= 1015​​​​​​​
'''
# === 872ms && 30.11MB === #
def count_waviness(n):
    s = str(n)
    m = len(s)

    @lru_cache(None)
    def dp(idx, x, y, allow_larger, digit_num):
        ans = 0
        if idx >= m:
            return ans 
        if allow_larger:
            for z in range(10):
                if z == 0 and digit_num == 0:
                    ans += dp(idx+1, y, z, True, 0)
                elif digit_num >= 2 and x > y and z > y:
                    ans += 10**(m-1-idx) + dp(idx+1, y, z, True, min(digit_num+1,2))
                elif digit_num >= 2 and x < y and z < y:
                    ans += 10**(m-1-idx) + dp(idx+1, y, z, True, min(digit_num+1,2))
                else:
                    ans += dp(idx+1, y, z, True, min(digit_num+1,2))
        else:
            upper_bound = int(s[idx])
            for z in range(upper_bound+1):
                if z == 0 and digit_num == 0:
                    ans += dp(idx+1, y, z, True, 0)
                elif digit_num >= 2 and x > y and z > y:
                    if z == upper_bound:
                        remain = int(s[idx+1:])+1 if idx+1 < m else 1
                        ans += remain + dp(idx+1, y, z, False, min(digit_num+1,2))
                    else:
                        ans += 10**(m-1-idx) + dp(idx+1, y, z, True, min(digit_num+1,2))
                elif digit_num >= 2 and x < y and z < y:
                    if z == upper_bound:
                        remain = int(s[idx+1:])+1 if idx+1 < m else 1
                        ans += remain + dp(idx+1, y, z, False, min(digit_num+1,2))
                    else:
                        ans += 10**(m-1-idx) + dp(idx+1, y, z, True, min(digit_num+1,2))
                else:
                    ans += dp(idx+1, y, z, z < upper_bound, min(digit_num+1,2))
        return ans


    ans = dp(0, 0, 0, False, 0)
    # print(f"count_waviness({n}) = {ans}")
    return ans

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return count_waviness(num2) - count_waviness(num1-1)