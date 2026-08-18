'''
=== 3472. Longest Palindromic Subsequence After at Most K Operations ===

You are given a string s and an integer k.
In one operation, you can replace the character at any position with the next or previous letter in the alphabet (wrapping around so that 'a' is after 'z'). For example, replacing 'a' with the next letter results in 'b', and replacing 'a' with the previous letter results in 'z'. Similarly, replacing 'z' with the next letter results in 'a', and replacing 'z' with the previous letter results in 'y'.
Return the length of the longest palindromic subsequence of s that can be obtained after performing at most k operations.
A subsequence is a non-empty string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
A palindrome is a string that reads the same forward and backward.

Example 1:
    Input: s = "abced", k = 2
    Output: 3
    Explanation:
    Replace s[1] with the next letter, and s becomes "acced".
    Replace s[4] with the previous letter, and s becomes "accec".
    The subsequence "ccc" forms a palindrome of length 3, which is the maximum.
Example 2:
    Input: s = "aaazzz", k = 4
    Output: 6
    Explanation:
    Replace s[0] with the previous letter, and s becomes "zaazzz".
    Replace s[4] with the next letter, and s becomes "zaazaz".
    Replace s[3] with the next letter, and s becomes "zaaaaz".
    The entire string forms a palindrome of length 6.

Constraints:
    1. 1 <= s.length <= 200
    2. 1 <= k <= 200
    3. s consists of only lowercase English letters.
'''
# === 5881ms && 409.7MB === #
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        
        @lru_cache(None)
        def dp(l, r, k):
            if l == r:
                return 1
            elif l > r:
                return 0
            elif s[l] == s[r]:
                return 2 + dp(l+1, r-1, k)
            src, tgt = sorted([ord(s[l]), ord(s[r])])
            change = min(tgt-src, src+26-tgt)
            if k < change:
                return max(dp(l+1, r, k), dp(l, r-1, k))
            else:
                return max(dp(l+1, r, k), dp(l, r-1, k), 2 + dp(l+1, r-1, k-change))
            
        return dp(0, n-1, k)