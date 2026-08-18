'''
=== 3174. Clear Digits ===

You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
    - Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Example 1:
    Input: s = "abc"
    Output: "abc"
    Explanation:
    There is no digit in the string.
Example 2:
    Input: s = "cb34"
    Output: ""
    Explanation:
    First, we apply the operation on s[2], and s becomes "c4".
    Then we apply the operation on s[1], and s becomes "".

Constraints:
    1. 1 <= s.length <= 100
    2. s consists only of lowercase English letters and digits.
    3. The input is generated such that it is possible to delete all digits.
'''
# === 34ms && 16.5MB === #
class Solution:
    def clearDigits(self, s: str) -> str:
        q = []
        for ch in s:
            if ch in string.ascii_lowercase:
                q.append(ch)
            else:
                if q != []:
                    q.pop()
        return "".join(q)