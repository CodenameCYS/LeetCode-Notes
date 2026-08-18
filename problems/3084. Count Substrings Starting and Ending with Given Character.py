'''
=== 3084. Count Substrings Starting and Ending with Given Character ===

You are given a string s and a character c. Return the total number of substrings of s that start and end with c.

Example 1:
    Input: s = "abada", c = "a"
    Output: 6
    Explanation: Substrings starting and ending with "a" are: "abada", "abada", "abada", "abada", "abada", "abada".
Example 2:
    Input: s = "zzz", c = "z"
    Output: 6
    Explanation: There are a total of 6 substrings in s and all start and end with "z".

Constraints:
    1. 1 <= s.length <= 105
    2. s and c consist only of lowercase English letters.
'''
# === 52ms && 17.5MB === #
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = Counter(s)[c]
        return cnt * (cnt+1) // 2