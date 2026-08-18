'''
=== 3456. Find Special Substring of Length K ===

You are given a string s and an integer k.
Determine if there exists a substring of length exactly k in s that satisfies the following conditions:
    - The substring consists of only one distinct character (e.g., "aaa" or "bbb").
    - If there is a character immediately before the substring, it must be different from the character in the substring.
    - If there is a character immediately after the substring, it must also be different from the character in the substring.
Return true if such a substring exists. Otherwise, return false.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:
    Input: s = "aaabaaa", k = 3
    Output: true
    Explanation:
    The substring s[4..6] == "aaa" satisfies the conditions.
    It has a length of 3.
    All characters are the same.
    The character before "aaa" is 'b', which is different from 'a'.
    There is no character after "aaa".
Example 2:
    Input: s = "abc", k = 2
    Output: false
    Explanation:
    There is no substring of length 2 that consists of one distinct character and satisfies the conditions.

Constraints:
    1. 1 <= k <= s.length <= 100
    2. s consists of lowercase English letters only.
'''
# === 7ms && 17.8MB === #
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        
        def is_special(idx):
            if idx-1 >= 0 and s[idx-1] == s[idx]:
                return False
            if idx+k < n and s[idx] == s[idx+k]:
                return False
            return all(s[i] == s[idx] for i in range(idx, idx+k))
        
        return any(is_special(i) for i in range(n-k+1))