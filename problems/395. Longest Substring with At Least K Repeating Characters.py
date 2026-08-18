'''
=== 395. Longest Substring with At Least K Repeating Characters ===

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is less than or equal to k.

Example 1:
    Input: s = "aaabb", k = 3
    Output: 3
    Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:
    Input: s = "ababbc", k = 2
    Output: 5
    Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 
Constraints:
    1. 1 <= s.length <= 104
    2. s consists of only lowercase English letters.
    3. 1 <= k <= 105
'''
# === 56ms(38.25%) && 14.5MB(13.35%) === #
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # print(s)
        counter = [x for x, y in Counter(s).items() if y < k]
        n = len(s)
        if counter == []:
            return n
        ans = 0
        last = -1
        for idx, c in enumerate(s):
            if c in counter:
                ans = max(self.longestSubstring(s[last+1:idx], k), ans)
                last = idx
        ans = max(self.longestSubstring(s[last+1:n], k), ans)
        return ans