'''
=== 2002. Maximum Product of the Length of Two Palindromic Subsequences ===

Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.
Return the maximum possible product of the lengths of the two palindromic subsequences.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

Example 1:
    example-1
    Input: s = "leetcodecom"
    Output: 9
    Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
    The product of their lengths is: 3 * 3 = 9.
Example 2:
    Input: s = "bb"
    Output: 1
    Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
    The product of their lengths is: 1 * 1 = 1.
Example 3:
    Input: s = "accbcaxxcxx"
    Output: 25
    Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
    The product of their lengths is: 5 * 5 = 25.
 
Constraints:
    1. 2 <= s.length <= 12
    2. s consists of lowercase English letters only.
'''
# === 389ms && 17.5MB === #
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        
        def divide_string(s, val):
            s1, s2 = "", ""
            idx = n-1
            while val != 0:
                if val % 2 == 1:
                    s1 = s[idx] + s1
                else:
                    s2 = s[idx] + s2
                idx -= 1
                val = val // 2
            s2 = s[:idx+1] + s2
            return s1, s2
        
        @lru_cache(None)
        def get_longest_palindrome(s):
            if len(s) <= 1:
                return len(s)
            idx = 0
            while True:
                nxt = s.find(s[0], idx+1)
                if nxt == -1:
                    break
                idx = nxt
            res = get_longest_palindrome(s[1:])
            if idx != 0:
                res = max(res, 2 + get_longest_palindrome(s[1:idx]))
            return res
        
        res = 1
        for val in range(1, 2**(n-1)+1):
            s1, s2 = divide_string(s, val)
            x = get_longest_palindrome(s1)
            y = get_longest_palindrome(s2)
            res = max(res, x*y)
        return res