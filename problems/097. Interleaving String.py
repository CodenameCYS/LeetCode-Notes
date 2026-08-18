'''
=== 97. Interleaving String ===

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
    - s = s1 + s2 + ... + sn
    - t = t1 + t2 + ... + tm
    - |n - m| <= 1
    - The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
Example 2:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false
Example 3:
    Input: s1 = "", s2 = "", s3 = ""
    Output: true
 
Constraints:
    1. 0 <= s1.length, s2.length <= 100
    2. 0 <= s3.length <= 200
    3. s1, s2, and s3 consist of lowercase English letters.
 
Follow up: Could you solve it using only O(s2.length) additional memory space?
'''
# === 36ms(60.72%) && 14.4MB(51.66%) === #
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)
        if n + m != l:
            return False
        
        @lru_cache(None)
        def dp(i, j, k):
            if i >= n and j >= m and k >= l:
                return True
            elif i >= n:
                return s2[j:] == s3[k:]
            elif j >= m:
                return s1[i:] == s3[k:]
            
            if s1[i] != s3[k] and s2[j] != s3[k]:
                return False
            elif s1[i] == s3[k] and s2[j] != s3[k]:
                return dp(i+1, j, k+1)
            elif s1[i] != s3[k] and s2[j] == s3[k]:
                return dp(i, j+1, k+1)
            else:
                return dp(i+1, j, k+1) or dp(i, j+1, k+1)
            
        return dp(0, 0, 0)
        