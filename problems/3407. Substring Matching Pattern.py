'''
=== 3407. Substring Matching Pattern ===

You are given a string s and a pattern string p, where p contains exactly one '*' character.
The '*' in p can be replaced with any sequence of zero or more characters.
Return true if p can be made a substring of s, and false otherwise.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "leetcode", p = "ee*e"
    Output: true
    Explanation:
    By replacing the '*' with "tcod", the substring "eetcode" matches the pattern.
Example 2:
    Input: s = "car", p = "c*v"
    Output: false
    Explanation:
    There is no substring matching the pattern.
Example 3:
    Input: s = "luck", p = "u*"
    Output: true
    Explanation:
    The substrings "u", "uc", and "uck" match the pattern.

Constraints:
    1. 1 <= s.length <= 50
    2. 1 <= p.length <= 50
    3. s contains only lowercase English letters.
    4. p contains only lowercase English letters and exactly one '*'
'''
# === 0ms && 17.7MB === #
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p = p.strip("*").split("*")
        i, n = 0, len(s)
        for sub in p:
            if sub == "":
                continue
            while i < n and not s[i:].startswith(sub):
                i += 1
            if i >= n:
                return False
            i += len(sub)
        return True