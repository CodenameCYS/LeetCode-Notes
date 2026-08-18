'''
=== 583. Delete Operation for Two Strings ===

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
    Input: word1 = "sea", word2 = "eat"
    Output: 2
    Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:
    Input: word1 = "leetcode", word2 = "etco"
    Output: 4
    
Constraints:
    1. 1 <= word1.length, word2.length <= 500
    2. word1 and word2 consist of only lowercase English letters.
'''
# === 268ms && 32.5MB === #
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        @lru_cache(None)
        def lcs(i, j):
            if i == n or j == m:
                return 0
            if word1[i] == word2[j]:
                return 1 + lcs(i+1, j+1)
            return max(lcs(i+1, j), lcs(i, j+1))
        
        l = lcs(0, 0)
        return m+n - 2*l
        