'''
=== 3303. Find the Occurrence of First Almost Equal Substring ===

You are given two strings s and pattern.
A string x is called almost equal to y if you can change at most one character in x to make it identical to y.
Return the smallest starting index of a substring in s that is almost equal to pattern. If no such index exists, return -1.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "abcdefg", pattern = "bcdffg"
    Output: 1
    Explanation:
    The substring s[1..6] == "bcdefg" can be converted to "bcdffg" by changing s[4] to "f".
Example 2:
    Input: s = "ababbababa", pattern = "bacaba"
    Output: 4
    Explanation:
    The substring s[4..9] == "bababa" can be converted to "bacaba" by changing s[6] to "c".
Example 3:
    Input: s = "abcd", pattern = "dba"
    Output: -1
Example 4:
    Input: s = "dde", pattern = "d"
    Output: 0

Constraints:
    1. 1 <= pattern.length < s.length <= 3 * 105
    2. s and pattern consist only of lowercase English letters.
 
- Follow-up: Could you solve the problem if at most k consecutive characters can be changed?
'''
def z_algorithm(s):
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = -1, -1
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r-l] == s[r]:
                r += 1
            z[i] = r-l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r-l] == s[r]:
                    r += 1
                z[i] = r-l
                r -= 1
    z[0] = n
    return z
# === 2756ms && 50.4MB === #
class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        n, m = len(s), len(pattern)
        z1 = z_algorithm(pattern + s)
        z2 = z_algorithm(pattern[::-1] + s[::-1])
        for i in range(n):
            if i+m > n:
                break
            c1 = z1[i+m]
            if c1 >= m:
                return i
            j = i+m-1
            c2 = z2[n-j-1+m]
            if c1 + c2 == m-1:
                return i
        return -1