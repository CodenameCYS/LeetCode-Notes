'''
=== 1405. Longest Happy String ===

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
Given three integers a, b and c, return any string s, which satisfies following conditions:
    - s is happy and longest possible.
    - s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
    - s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

Example 1:
    Input: a = 1, b = 1, c = 7
    Output: "ccaccbcc"
    Explanation: "ccbccacc" would also be a correct answer.
Example 2:
    Input: a = 2, b = 2, c = 1
    Output: "aabbc"
Example 3:
    Input: a = 7, b = 1, c = 0
    Output: "aabaa"
    Explanation: It's the only correct answer in this case.
 
Constraints:
    1. 0 <= a, b, c <= 100
    2. a + b + c > 0
'''
# === 28ms(84.03%) && 13.9MB(100%) === #
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = sorted([[a, 'a'], [b, 'b'], [c, 'c']], reverse=True)
        def fill(chars, s):
            if chars[1][0] == 0:
                return s + chars[0][1] * min(2, chars[0][0])
            if chars[0][0] > chars[1][0]:
                s += 2*chars[0][1] + chars[1][1]
                chars[0][0] -= 2; chars[1][0] -= 1
            else:
                s += chars[0][1] + chars[1][1]
                chars[0][0] -= 1; chars[1][0] -= 1
            chars = sorted(chars, reverse=True)
            return fill(chars, s)
        return fill(chars, "")
        