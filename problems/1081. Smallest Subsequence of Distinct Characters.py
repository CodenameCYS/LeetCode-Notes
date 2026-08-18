'''
=== 1081. Smallest Subsequence of Distinct Characters ===

Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

Example 1:
    Input: s = "bcabc"
    Output: "abc"
Example 2:
    Input: s = "cbacdcbc"
    Output: "acdb"
 
Constraints:
    1. 1 <= s.length <= 1000
    2. s consists of lowercase English letters.
'''
# === 24ms(96.61%) && 14MB(100%) === #
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_loc = {c: idx for idx, c in enumerate(s)}
        stack = []
        for idx, c in enumerate(s):
            if c in stack:
                continue
            
            while stack != [] and stack[-1] > c and last_loc[stack[-1]] > idx:
                stack.pop()
            stack.append(c)
            
        return "".join(stack)