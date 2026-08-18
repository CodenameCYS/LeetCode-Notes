'''
=== 2516. Take K of Each Character From Left and Right ===

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

Example 1:
    Input: s = "aabaaaacaabc", k = 2
    Output: 8
    Explanation: 
    Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
    Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
    A total of 3 + 5 = 8 minutes is needed.
    It can be proven that 8 is the minimum number of minutes needed.
Example 2:
    Input: s = "a", k = 1
    Output: -1
    Explanation: It is not possible to take one 'b' or 'c' so return -1.
 
Constraints:
    1. 1 <= s.length <= 105
    2. s consists of only the letters 'a', 'b', and 'c'.
    3. 0 <= k <= s.length
'''
# === 939ms && 14.9MB === #
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        n = len(s)
        i, j = 0, n-1
        while i < n:
            cnt[s[i]] += 1
            i += 1
            if all(cnt[ch] >= k for ch in "abc"):
                break
        if any(cnt[ch] < k for ch in "abc"):
            return -1
        res = i
        while i > 0:
            i -= 1
            cnt[s[i]] -= 1
            while any(cnt[ch] < k for ch in "abc"):
                cnt[s[j]] += 1
                j -= 1
            res = min(res, i + n-1 - j)
        return res