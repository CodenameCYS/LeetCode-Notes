'''
=== 1745. Palindrome Partitioning IV ===

Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​
A string is said to be palindrome if it the same string when reversed.

Example 1:
    Input: s = "abcbdd"
    Output: true
    Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
Example 2:
    Input: s = "bcbddxy"
    Output: false
    Explanation: s cannot be split into 3 palindromes.
 
Constraints:
    1. 3 <= s.length <= 2000
    2. s​​​​​​ consists only of lowercase English letters.
'''
# === 2240ms && 15.1MB === #
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        
        @lru_cache(None)
        def dp(idx, k):
            if k == 1:
                sub = s[idx:]
                return sub == sub[::-1]
            elif idx >= n:
                return False
            for j in range(idx+1, n):
                sub = s[idx: j]
                if sub == sub[::-1] and dp(j, k-1):
                    return True
            return False
        
        return dp(0, 3)
                    