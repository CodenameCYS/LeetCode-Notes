'''
=== 3884. First Matching Character From Both Ends ===

You are given a string s of length n consisting of lowercase English letters.
Return the smallest index i such that s[i] == s[n - i - 1].
If no such index exists, return -1.

Example 1:
    Input: s = "abcacbd"
    Output: 1
    Explanation:
    At index i = 1, s[1] and s[5] are both 'b'.
    No smaller index satisfies the condition, so the answer is 1.
Example 2:
    Input: s = "abc"
    Output: 1
    Explanation:
    ​​​​​​​At index i = 1, the two compared positions coincide, so both characters are 'b'.
    No smaller index satisfies the condition, so the answer is 1.
Example 3:
    Input: s = "abcdab"
    Output: -1
    Explanation:
    ​​​​​​​For every index i, the characters at positions i and n - i - 1 are different.
    Therefore, no valid index exists, so the answer is -1.

Constraints:
    1. 1 <= n == s.length <= 100
    2. s consists of lowercase English letters.
'''
# === 0ms && 19.18MB === #
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        for i in range((n+1)//2):
            if s[i] == s[n-1-i]:
                return i
        return -1