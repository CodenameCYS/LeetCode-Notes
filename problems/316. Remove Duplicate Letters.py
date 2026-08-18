'''
=== 316. Remove Duplicate Letters ===

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Example 1:
    Input: s = "bcabc"
    Output: "abc"
Example 2:
    Input: s = "cbacdcbc"
    Output: "acdb"
 
Constraints:
    1. 1 <= s.length <= 104
    2. s consists of lowercase English letters.
'''
# === 28ms(96.82%) && 14.1MB === #
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_loc = {c: idx for idx, c in enumerate(s)}
        stack = []
        for idx, c in enumerate(s):
            if c in stack:
                continue
            
            while stack != [] and stack[-1] > c and last_loc[stack[-1]] > idx:
                stack.pop()
            stack.append(c)
            
        return "".join(stack)
                
                