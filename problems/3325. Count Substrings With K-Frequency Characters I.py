'''
=== 3325. Count Substrings With K-Frequency Characters I ===

Given a string s and an integer k, return the total number of substrings of s where at least one character appears at least k times.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "abacb", k = 2
    Output: 4
    Explanation:
    The valid substrings are:
    "aba" (character 'a' appears 2 times).
    "abac" (character 'a' appears 2 times).
    "abacb" (character 'a' appears 2 times).
    "bacb" (character 'b' appears 2 times).
Example 2:
    Input: s = "abcde", k = 1
    Output: 15
    Explanation:
    All substrings are valid because every character appears at least once.

Constraints:
    1. 1 <= s.length <= 3000
    2. 1 <= k <= s.length
    3. s consists only of lowercase English letters.
'''
# === 29ms && 16.8MB === #
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        cnt = [0 for _ in range(26)]
        i, j = 0, 0
        ans = 0
        while i < n:
            while j < n and max(cnt) < k:
                cnt[ord(s[j]) - ord('a')] += 1
                j += 1
            if max(cnt) >= k:
                ans += n-j+1
            else:
                break
            cnt[ord(s[i]) - ord('a')] -= 1
            i += 1
        return ans
                