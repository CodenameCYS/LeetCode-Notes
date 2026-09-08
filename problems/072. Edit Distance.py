'''
=== 072. Edit Distance ===

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
    - Insert a character
    - Delete a character
    - Replace a character
 
Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: 
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
 
Constraints:
    1. 0 <= word1.length, word2.length <= 500
    2. word1 and word2 consist of lowercase English letters.
'''
# === 33ms && 25.98MB === #
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        @cache
        def dp(i, j):
            if i >= n:
                return m-j
            if j >= m:
                return n-i
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            else:
                return 1 + min(
                    dp(i+1, j),
                    dp(i, j+1),
                    dp(i+1, j+1)
                )

        return dp(0, 0)