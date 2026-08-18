'''
=== 1796. Second Largest Digit in a String ===

Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:
    Input: s = "dfa12321afd"
    Output: 2
    Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:
    Input: s = "abc1111"
    Output: -1
    Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 
Constraints:
    1. 1 <= s.length <= 500
    2. s consists of only lowercase English letters and/or digits.
'''
# === 28ms && 14.1MB === #
class Solution:
    def secondHighest(self, s: str) -> int:
        res = set()
        for c in s:
            if c in "0123456789":
                res.add(int(c))
        res = sorted(res, reverse=True)
        if len(res) > 1:
            return res[1]
        return -1