'''
=== 2801. Count Stepping Numbers in Range ===

Given two positive integers low and high represented as strings, find the count of stepping numbers in the inclusive range [low, high].
A stepping number is an integer such that all of its adjacent digits have an absolute difference of exactly 1.
Return an integer denoting the count of stepping numbers in the inclusive range [low, high].
Since the answer may be very large, return it modulo 109 + 7.
Note: A stepping number should not have a leading zero.

Example 1:
    Input: low = "1", high = "11"
    Output: 10
    Explanation: The stepping numbers in the range [1,11] are 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10. There are a total of 10 stepping numbers in the range. Hence, the output is 10.
Example 2:
    Input: low = "90", high = "101"
    Output: 2
    Explanation: The stepping numbers in the range [90,101] are 98 and 101. There are a total of 2 stepping numbers in the range. Hence, the output is 2. 
 
Constraints:
    1. 1 <= int(low) <= int(high) < 10100
    2. 1 <= low.length, high.length <= 100
    3. low and high consist of only digits.
    4. low and high don't have any leading zeros.
'''
MOD = 10**9 + 7
# === 326ms && 21.5MB === #
class Solution:
    
    @lru_cache(None)
    def count_stepping_number(self, num):
        if num == "0":
            return 1
        n = len(num)
        
        @lru_cache(None)
        def dp(k, pre, have_start, allow_bigger):
            if k == 0:
                return 1
            res = 0
            if have_start:
                if allow_bigger:
                    if pre != 9:
                        res += dp(k-1, pre+1, True, True)
                else:
                    if pre+1 < int(num[n-k]):
                        res += dp(k-1, pre+1, True, True)
                    elif pre+1 == int(num[n-k]):
                        res += dp(k-1, pre+1, True, False)
                    
                if allow_bigger:
                    if pre != 0:
                        res += dp(k-1, pre-1, True, True)
                else:
                    if 0 <= pre-1 < int(num[n-k]):
                        res += dp(k-1, pre-1, True, True)
                    elif pre-1 == int(num[n-k]):
                        res += dp(k-1, pre-1, True, False)
            else:
                res += dp(k-1, pre, False, True)
                if k == n:
                    for i in range(1, int(num[0])):
                        res += dp(k-1, i, True, True)
                    res += dp(k-1, int(num[0]), True, False)
                else:
                    for i in range(1, 10):
                        res += dp(k-1, i, True, True)
            return res % MOD
        
        res = dp(len(num), 0, False, False)
        return res
    
    def minus_one(self, num):
        num = [ch for ch in num]
        i = len(num) - 1
        while num[i] == "0":
            num[i] = "9"
            i -= 1
        num[i] = str(int(num[i]) - 1)
        res = "".join(num).lstrip("0")
        return res if res != "" else "0"
    
    def countSteppingNumbers(self, low: str, high: str) -> int:
        low = self.minus_one(low)
        res = self.count_stepping_number(high) - self.count_stepping_number(low)
        res = (res + MOD) % MOD
        return res
        