'''
=== 5417. Maximum Number of Vowels in a Substring of Given Length ===

Given a string s and an integer k.
Return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are (a, e, i, o, u).

Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.
Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.
Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:
    Input: s = "rhythms", k = 4
    Output: 0
    Explanation: We can see that s doesn't have any vowel letters.
Example 5:
    Input: s = "tryhard", k = 4
    Output: 1
 
Constraints:
    1. 1 <= s.length <= 10^5
    2. s consists of lowercase English letters.
    3. 1 <= k <= s.length
'''
# === 508ms && 17.9MB === #
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        count = [0 for i in range(n+1)]
        count[0] = 0
        for i in range(n):
            if s[i] in {"a", "e", "i", "o", "u"}:
                count[i+1] = count[i] + 1
            else:
                count[i+1] = count[i]
        ans = 0
        for i in range(n-k+1):
            ans = max(ans, count[i+k] - count[i])
        return ans