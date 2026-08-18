'''
=== 2311. Longest Binary Subsequence Less Than or Equal to K ===

You are given a binary string s and a positive integer k.
Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:
    - The subsequence can contain leading zeroes.
    - The empty string is considered to be equal to 0.
    - A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 
Example 1:
    Input: s = "1001010", k = 5
    Output: 5
    Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
    Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
    The length of this subsequence is 5, so 5 is returned.
Example 2:
    Input: s = "00101001", k = 1
    Output: 6
    Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
    The length of this subsequence is 6, so 6 is returned.
 
Constraints:
    1. 1 <= s.length <= 1000
    2. s[i] is either '0' or '1'.
    3. 1 <= k <= 109
'''
# === 429ms && 14MB === #
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        kd = []
        while k != 0:
            kd.insert(0, k % 2)
            k = k // 2
        m = len(kd)
        
        def get_max(idx):
            if n - idx < m:
                return n-idx
            sub = s[idx:]
            less, j = False, 0
            for i, ch in enumerate(sub):
                if j >= m:
                    break
                if not less:
                    if int(sub[i]) > kd[j]:
                        continue
                    elif int(sub[i]) < kd[j]:
                        less = True
                j += 1
            return m if j >= m else m-1
        
        res, cnt = 0, 0
        for i, ch in enumerate(s):
            if ch == "0":
                cnt += 1
                res = max(res, cnt)
            else:
                res = max(res, cnt + get_max(i))
        return res
                
            