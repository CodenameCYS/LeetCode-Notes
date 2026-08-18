'''
=== 3519. Count Numbers with Non-Decreasing Digits ===

You are given two integers, l and r, represented as strings, and an integer b. Return the count of integers in the inclusive range [l, r] whose digits are in non-decreasing order when represented in base b.
An integer is considered to have non-decreasing digits if, when read from left to right (from the most significant digit to the least significant digit), each digit is greater than or equal to the previous one.
Since the answer may be too large, return it modulo 109 + 7.

Example 1:
    Input: l = "23", r = "28", b = 8
    Output: 3
    Explanation:
    The numbers from 23 to 28 in base 8 are: 27, 30, 31, 32, 33, and 34.
    Out of these, 27, 33, and 34 have non-decreasing digits. Hence, the output is 3.
Example 2:
    Input: l = "2", r = "7", b = 2
    Output: 2
    Explanation:
    The numbers from 2 to 7 in base 2 are: 10, 11, 100, 101, 110, and 111.
    Out of these, 11 and 111 have non-decreasing digits. Hence, the output is 2.

Constraints:
    1. 1 <= l.length <= r.length <= 100
    2. 2 <= b <= 10
    3. l and r consist only of digits.
    4. The value represented by l is less than or equal to the value represented by r.
    5. l and r do not contain leading zeros.
'''
MOD = 10**9+7
# === 312ms && 19.3MB === #
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        
        def minus_one(num):
            n = len(num)
            idx = len(num) - 1
            while num[idx] == "0":
                idx -= 1
            return num[:idx] + str(int(num[idx]) - 1) + "9" * (n-1-idx)
        
        def convert_to_rank_b(num, b):
            def div(num, b):
                ans, r = "", 0
                for d in num:
                    r = r * 10 + int(d)
                    ans += str(r // b)
                    r = r % b
                return ans.lstrip("0"), str(r)
            
            original = num
            ans = ""
            while num != "":
                num, r = div(num, b)
                ans = r + ans
            # print(f"convert_to_rank_b({original}, {b}) = {ans.lstrip('0')}")
            return ans.lstrip("0")
        
        def count_number(num, b):
            bnum = convert_to_rank_b(num, b)
            n = len(bnum)
            
            @lru_cache(None)
            def dp(idx, pre, allow_larger):
                if idx >= n:
                    return 1
                elif not allow_larger and int(bnum[idx]) < pre:
                    return 0
                if allow_larger:
                    ans = 0
                    for i in range(pre, b):
                        ans = (ans + dp(idx+1, i, allow_larger)) % MOD
                    return ans
                else:
                    ans = 0
                    for i in range(pre, int(bnum[idx])):
                        ans = (ans + dp(idx+1, i, True)) % MOD
                    if pre <= int(bnum[idx]):
                        ans = (ans + dp(idx+1, int(bnum[idx]), False)) % MOD
                    return ans
                
            return dp(0, 0, False)
        
        return (count_number(r, b) - count_number(minus_one(l), b)) % MOD