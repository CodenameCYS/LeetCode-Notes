'''
=== 3216. Lexicographically Smallest String After a Swap ===

Given a string s containing only digits, return the lexicographically smallest string that can be obtained after swapping adjacent digits in s with the same parity at most once.
Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

Example 1:
    Input: s = "45320"
    Output: "43520"
    Explanation:
    s[1] == '5' and s[2] == '3' both have the same parity, and swapping them results in the lexicographically smallest string.
Example 2:
    Input: s = "001"
    Output: "001"
    Explanation:
    There is no need to perform a swap because s is already the lexicographically smallest.

Constraints:
    1. 2 <= s.length <= 100
    2. s consists only of digits.
'''
# === 36ms && 16.4MB === #
class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        for i in range(n-1):
            x, y = int(s[i]), int(s[i+1])
            if x % 2 == y % 2 and x > y:
                return s[:i] + s[i+1] + s[i] + s[i+2:]
        return s
        