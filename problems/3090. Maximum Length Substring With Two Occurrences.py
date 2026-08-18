'''
=== 3090. Maximum Length Substring With Two Occurrences ===

Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 
Example 1:
    Input: s = "bcbbbcba"
    Output: 4
    Explanation:
    The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:
    Input: s = "aaaa"
    Output: 2
    Explanation:
    The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 
Constraints:
    1. 2 <= s.length <= 100
    2. s consists only of lowercase English letters.
'''
# === 39ms && 16.6MB === #
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        i, j = 0, 0
        cnt = defaultdict(int)
        ans = 0
        while j < n:
            cnt[s[j]] += 1
            while i < j and cnt[s[j]] > 2:
                cnt[s[i]] -= 1
                i += 1
            j += 1
            ans = max(ans, j-i)
        return ans