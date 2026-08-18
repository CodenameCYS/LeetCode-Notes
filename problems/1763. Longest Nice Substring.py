'''
=== 1763. Longest Nice Substring ===

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

Example 1:
    Input: s = "YazaAay"
    Output: "aAa"
    Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
    "aAa" is the longest nice substring.
Example 2:
    Input: s = "Bb"
    Output: "Bb"
    Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:
    Input: s = "c"
    Output: ""
    Explanation: There are no nice substrings.
Example 4:
    Input: s = "dDzeE"
    Output: "dD"
    Explanation: Both "dD" and "eE" are the longest nice substrings.
    As there are multiple longest nice substrings, return "dD" since it occurs earlier.
 
Constraints:
    1. 1 <= s.length <= 100
    2. s consists of uppercase and lowercase English letters.
'''
# === 88ms && 14.5MB === #
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            for c in sub:
                if not c.lower() in sub or not c.upper() in sub:
                    return False
            return True
        
        n = len(s)
        res = []
        for i in range(n):
            for j in range(n, i, -1):
                if is_nice(s[i:j]):
                    res.append((s[i:j], i))
        res = sorted(res, key=lambda x: (-len(x[0]), x[1]))
        return "" if res == [] else res[0][0]