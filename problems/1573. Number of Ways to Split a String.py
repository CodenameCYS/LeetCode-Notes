'''
=== 1573. Number of Ways to Split a String ===

Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).
Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: s = "10101"
    Output: 4
    Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
    "1|010|1"
    "1|01|01"
    "10|10|1"
    "10|1|01"
Example 2:
    Input: s = "1001"
    Output: 0
Example 3:
    Input: s = "0000"
    Output: 3
    Explanation: There are three ways to split s in 3 parts.
    "0|0|00"
    "0|00|0"
    "00|0|0"
Example 4:
    Input: s = "100100010100110"
    Output: 12
 
Constraints:
    1. s[i] == '0' or s[i] == '1'
    2. 3 <= s.length <= 10^5
'''
# === 116ms && 14.6MB === #
class Solution:
    def numWays(self, s: str) -> int:
        MOD = 1000000007
        one_count = 0
        zero_count = 0
        cache = {}
        for c in s:
            if c == '0':
                zero_count += 1
            else:
                one_count += 1
                cache[one_count] = zero_count
                zero_count = 0
        if one_count not in cache.keys():
            cache[one_count] = zero_count
        if one_count % 3 != 0:
            return 0
        elif one_count == 0:
            return (zero_count-2) * (zero_count-1) // 2 % MOD
        else:
            return (cache[one_count // 3 +1] + 1) * (cache[one_count // 3 * 2 +1] + 1) % MOD
            