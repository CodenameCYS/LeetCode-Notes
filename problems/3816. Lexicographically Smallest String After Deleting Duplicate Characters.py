'''
=== 3816. Lexicographically Smallest String After Deleting Duplicate Characters ===

You are given a string s that consists of lowercase English letters.
You can perform the following operation any number of times (possibly zero times):
    - Choose any letter that appears at least twice in the current string s and delete any one occurrence.
Return the lexicographically smallest resulting string that can be formed this way.

Example 1:
    Input: s = "aaccb"
    Output: "aacb"
    Explanation:
    We can form the strings "acb", "aacb", "accb", and "aaccb". "aacb" is the lexicographically smallest one.
    For example, we can obtain "aacb" by choosing 'c' and deleting its first occurrence.
Example 2:
    Input: s = "z"
    Output: "z"
    Explanation:
    We cannot perform any operations. The only string we can form is "z".

Constraints:
    1. 1 <= s.length <= 105
    2. s contains lowercase English letters only.
'''
# === 627ms && 21.28MB === #
class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        cnt = Counter(s)

        stack = []
        for ch in s:
            while stack and stack[-1] > ch and cnt[stack[-1]] > 1:
                cnt[stack.pop()] -= 1
            stack.append(ch)

        while cnt[stack[-1]] > 1:
            cnt[stack.pop()] -= 1
        return "".join(stack)