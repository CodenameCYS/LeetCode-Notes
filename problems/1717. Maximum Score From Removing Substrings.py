'''
=== 1717. Maximum Score From Removing Substrings ===

You are given a string s and two integers x and y. You can perform two types of operations any number of times.
    - Remove substring "ab" and gain x points.
        - For example, when removing "ab" from "cabxbae" it becomes "cxbae".
    - Remove substring "ba" and gain y points.
        - For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example 1:
    Input: s = "cdbcbbaaabab", x = 4, y = 5
    Output: 19
    Explanation:
    - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
    - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
    - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
    - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
    Total score = 5 + 4 + 5 + 5 = 19.
Example 2:
    Input: s = "aabbaaxybbaabb", x = 5, y = 4
    Output: 20
 
Constraints:
    1. 1 <= s.length <= 105
    2. 1 <= x, y <= 104
    3. s consists of lowercase English letters.
'''
# === 332ms && 16.1MB === #
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if x <= y:
            s1 = []
            for c in s:
                if c == "a" and s1 and s1[-1] == "b":
                    s1.pop()
                else:
                    s1.append(c)
            res += y * (len(s) - len(s1)) // 2
            s2 = []
            for c in s1:
                if c == "b" and s2 and s2[-1] == "a":
                    s2.pop()
                else:
                    s2.append(c)
            res += x * (len(s1) - len(s2)) // 2
        else:
            s1 = []
            for c in s:
                if c == "b" and s1 and s1[-1] == "a":
                    s1.pop()
                else:
                    s1.append(c)
            res += x * (len(s) - len(s1)) // 2
            s2 = []
            for c in s1:
                if c == "a" and s2 and s2[-1] == "b":
                    s2.pop()
                else:
                    s2.append(c)
            res += y * (len(s1) - len(s2)) // 2
        return res