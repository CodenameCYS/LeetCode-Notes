'''
=== 3557. Find Maximum Number of Non Intersecting Substrings ===

You are given a string word.
Return the maximum number of non-intersecting substrings of word that are at least four characters long and start and end with the same letter.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: word = "abcdeafdef"
    Output: 2
    Explanation:
    The two substrings are "abcdea" and "fdef".
Example 2:
    Input: word = "bcdaaaab"
    Output: 1
    Explanation:
    The only substring is "aaaa". Note that we cannot also choose "bcdaaaab" since it intersects with the other substring.

Constraints:
    1. 1 <= word.length <= 2 * 105
    2. word consists only of lowercase English letters.
'''
# === 1713ms && 420.2MB === #
class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        locs = defaultdict(list)
        for i, ch in enumerate(word):
            locs[ch].append(i)
        
        @lru_cache(None)
        def dp(idx):
            if idx >= n:
                return 0
            ch = word[idx]
            i = bisect.bisect_left(locs[ch], idx+3)
            if i >= len(locs[ch]):
                return dp(idx+1)
            else:
                return max(dp(idx+1), 1 + dp(locs[ch][i] + 1))
        
        return dp(0)
            