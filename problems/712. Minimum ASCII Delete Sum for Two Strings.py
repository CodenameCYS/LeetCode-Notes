'''
=== 712. Minimum ASCII Delete Sum for Two Strings ===

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
    Input: s1 = "sea", s2 = "eat"
    Output: 231
    Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
    Deleting "t" from "eat" adds 116 to the sum.
    At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
    Input: s1 = "delete", s2 = "leet"
    Output: 403
    Explanation: Deleting "dee" from "delete" to turn the string into "let",
    adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
    At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
    If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Note:
    1. 0 < s1.length, s2.length <= 1000.
    2. All elements of each string will have an ASCII value in [97, 122].
'''
# === 4348ms(5.06%) && 61.4MB(50%) === #
class Solution:
    def dp(self, s1: str, s2: str):
        if (s1, s2) in self.cache.keys():
            return self.cache[(s1, s2)]
        if s1 == "" or s2 == "":
            ans = sum([ord(c) for c in s1+s2])
            self.cache[(s1, s2)] = ans
            return ans
        c = s2[0]
        loc = s1.find(c)
        if loc == -1:
            ans = ord(c) + self.dp(s1, s2[1:])
        else:
            ans1 = sum([ord(it) for it in s1[:loc]]) + self.dp(s1[loc+1:], s2[1:])
            ans2 = ord(c) + self.dp(s1, s2[1:])
            ans = min(ans1, ans2)
        self.cache[(s1, s2)] = ans
        return ans
        
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.cache = {}
        ans = self.dp(s1, s2)
        return ans
            