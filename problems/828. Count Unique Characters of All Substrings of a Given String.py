'''
=== 828. Count Unique Characters of All Substrings of a Given String ===

Let's define a function countUniqueChars(s) that returns the number of unique characters on s, for example if s = "LEETCODE" then "L", "T","C","O","D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
On this problem given a string s we need to return the sum of countUniqueChars(t) where t is a substring of s. Notice that some substrings can be repeated so on this case you have to count the repeated ones too.
Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.

Example 1:
    Input: s = "ABC"
    Output: 10
    Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
    Evey substring is composed with only unique letters.
    Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:
    Input: s = "ABA"
    Output: 8
    Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
Example 3:
    Input: s = "LEETCODE"
    Output: 92
 
Constraints:
    1. 0 <= s.length <= 10^4
    2. s contain upper-case English letters only.
'''
# === 104ms(45.45%) && 14.1MB(100%) === #
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 1000000007
        counter = {chr(ord('A') + i):[] for i in range(26)}
        l = len(s)
        for i, c in enumerate(s):
            counter[c].append(i)
        ans = 0
        for k, v in counter.items():
            # n = len(v)
            for i, loc in enumerate(v):
                last_loc = -1 if i == 0 else v[i-1]
                next_loc = l if i == len(v)-1 else v[i+1]
                ans = (ans + (loc-last_loc)*(next_loc-loc)) % MOD
        return ans