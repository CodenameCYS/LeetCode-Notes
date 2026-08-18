'''
=== 3983. Subsequence After One Replacement ===

You are given two strings s and t consisting of lowercase English letters.
You may choose at most one index in s and replace the character at that index with any lowercase English letter.
Return true if it is possible to make s a subsequence of t; otherwise, return false.

Example 1:
    Input: s = "cat", t = "chat"
    Output: true
    Explanation:
    Replace s[1] from 'a' to 'h'. The resulting string is "cht".
    "cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.
Example 2:
    Input: s = "plane", t = "apple"
    Output: false
    Explanation:
    The characters 'p', 'l', and 'e' can be matched in t, but the remaining characters cannot be matched while preserving the required order.
    Even after replacing any one character in s, it is impossible to make s a subsequence of t.
 
Constraints:
    - 1 <= s.length, t.length <= 105
    - s and t consist only of lowercase English letters.
'''
# === 11ms && 23.61MB === #
class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n > m:
            return False
        
        @lru_cache(None)
        def dp(i, j, k):
            if n-i == m-j:
                diff = 0
                for ch1, ch2 in zip(s[i:], t[j:]):
                    if ch1 != ch2:
                        diff += 1
                        if diff > k:
                            return False
                return True
            if j >= m or n-i > m-j:
                return False
            if n-i <= k:
                return True
            if s[i] == t[j]:
                return dp(i+1, j+1, k)
            elif k >= 1:
                return dp(i, j+1, k) or dp(i+1, j+1, k-1)
            else:
                return dp(i, j+1, k)

        return dp(0, 0, 1)