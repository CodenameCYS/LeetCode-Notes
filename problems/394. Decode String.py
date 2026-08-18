'''
=== 394. Decode String ===

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"
Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
Example 4:
    Input: s = "abc3[cd]xyz"
    Output: "abccdcdcdxyz"
 
Constraints:
    1. 1 <= s.length <= 30
    2. s consists of lowercase English letters, digits, and square brackets '[]'.
    3. s is guaranteed to be a valid input.
    4. All the integers in s are in the range [1, 300].
'''
import string
# === 20ms(97.92%) && 14.1MB(30.27%) === #
class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        res = ""
        
        i = 0
        while i<n:
            if s[i] in string.ascii_lowercase:
                res += s[i]
                i += 1
            else:
                repeat = 0
                while i<n and s[i] in string.digits:
                    repeat = repeat * 10 + int(s[i])
                    i += 1
                depth = 1
                j = i+1
                while j<n and depth > 0:
                    if s[j] == '[':
                        depth += 1
                    elif s[j] == ']':
                        depth -= 1
                    j += 1
                res += repeat * self.decodeString(s[i+1:j])
                i = j
        return res
                
        