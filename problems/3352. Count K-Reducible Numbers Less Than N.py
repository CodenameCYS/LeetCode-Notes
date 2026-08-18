'''
=== 3352. Count K-Reducible Numbers Less Than N ===

You are given a binary string s representing a number n in its binary form.
You are also given an integer k.
An integer x is called k-reducible if performing the following operation at most k times reduces it to 1:
    - Replace x with the count of set bits in its binary representation.
For example, the binary representation of 6 is "110". Applying the operation once reduces it to 2 (since "110" has two set bits). Applying the operation again to 2 (binary "10") reduces it to 1 (since "10" has one set bit).
Return an integer denoting the number of positive integers less than n that are k-reducible.
Since the answer may be too large, return it modulo 109 + 7.
A set bit refers to a bit in the binary representation of a number that has a value of 1.

Example 1:
    Input: s = "111", k = 1
    Output: 3
    Explanation:
    n = 7. The 1-reducible integers less than 7 are 1, 2, and 4.
Example 2:
    Input: s = "1000", k = 2
    Output: 6
    Explanation:
    n = 8. The 2-reducible integers less than 8 are 1, 2, 3, 4, 5, and 6.
Example 3:
    Input: s = "1", k = 3
    Output: 0
    Explanation:
    There are no positive integers less than n = 1, so the answer is 0.

Constraints:
    1. 1 <= s.length <= 800
    2. s has no leading zeros.
    3. s consists only of the characters '0' and '1'.
    4. 1 <= k <= 5
'''
MOD = 10**9+7

factorials = [1 for _ in range(801)]
for i in range(2, 801):
    factorials[i] = (i * factorials[i-1]) % MOD
revs = [pow(i, -1, mod=MOD) for i in factorials]

@lru_cache(None)
def C(n, m):
    return (factorials[n] * revs[m] * revs[n-m]) % MOD

# === 1513ms && 438.4MB === #
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        if s == "1":
            return 0
        
        def minus_one(s):
            n = len(s)
            idx = n-1
            while s[idx] == "0":
                idx -= 1
            s = s[:idx] + "0" + "1" * (n-idx-1)
            return s.lstrip("0")
        
        s = minus_one(s)
        n = len(s)
        
        digit_nums = defaultdict(set)
        digit_nums[1] = {1}
        for i in range(2, k+1):
            for j in range(2, n+1):
                if Counter(bin(j))["1"] in digit_nums[i-1]:
                    digit_nums[i].add(j)
        # print(digit_nums)
                    
        @lru_cache(None)
        def count(idx, ones, allow_large):
            if allow_large:
                return C(n-idx, ones) if n-idx >= ones else 0
            if ones == 0:
                return 1
            if idx >= n:
                return 0
            if allow_large:
                return (count(idx+1, ones-1, allow_large) + count(idx+1, ones, allow_large)) % MOD
            elif s[idx] == "1":
                return (count(idx+1, ones-1, allow_large) + count(idx+1, ones, True)) % MOD
            else:
                return count(idx+1, ones, allow_large)
            
        ans = 0
        for digit_num in digit_nums.values():
            for digit in digit_num:
                ans = (ans + count(0, digit, False)) % MOD
        return ans