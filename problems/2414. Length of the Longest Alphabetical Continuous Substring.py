'''
=== 6181. Length of the Longest Alphabetical Continuous Substring ===

An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".
    - For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

Example 1:
    Input: s = "abacaba"
    Output: 2
    Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
    "ab" is the longest continuous substring.
Example 2:
    Input: s = "abcde"
    Output: 5
    Explanation: "abcde" is the longest continuous substring.
 
Constraints:
    1. 1 <= s.length <= 105
    2. s consists of only English lowercase letters.
'''
# === 1303ms && 15MB === #
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        pre = 0
        res, cnt = 0, 0
        for ch in s:
            ch = ord(ch) - ord('a')
            if ch - pre == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
            pre = ch
        res = max(res, cnt)
        return res
        