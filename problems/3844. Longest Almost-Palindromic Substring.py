'''
=== 3844. Longest Almost-Palindromic Substring ===

You are given a string s consisting of lowercase English letters.
A substring is almost-palindromic if it becomes a palindrome after removing exactly one character from it.
Return an integer denoting the length of the longest almost-palindromic substring in s.

Example 1:
    Input: s = "abca"
    Output: 4
    Explanation:
    Choose the substring "abca".
    Remove "abca".
    The string becomes "aba", which is a palindrome.
    Therefore, "abca" is almost-palindromic.
Example 2:
    Input: s = "abba"
    Output: 4
    Explanation:
    Choose the substring "abba".
    Remove "abba".
    The string becomes "aba", which is a palindrome.
    Therefore, "abba" is almost-palindromic.
Example 3:
    Input: s = "zzabba"
    Output: 5
    Explanation:
    Choose the substring "zzabba".
    Remove "zabba".
    The string becomes "abba", which is a palindrome.
    Therefore, "zabba" is almost-palindromic.

Constraints:
    1. 2 <= s.length <= 2500
    2. s consists of only lowercase English letters.
'''
# === 1434ms && 20.09MB === #
class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)

        def gn(i, j, k):
            if i < 0 or j >= n:
                return 0 if (i < 0 and j >= n) or (k == 0) else 1
            if s[i] != s[j]:
                if k == 0:
                    return 0
                return 1 + max(gn(i-1, j, k-1), gn(i, j+1, k-1))
            else:
                return 2 + gn(i-1, j+1, k)

        def fn(idx):
            return max(1 + gn(idx-1, idx+1, 1), gn(idx, idx+1, 1))

        return max(fn(i) for i in range(n))
            