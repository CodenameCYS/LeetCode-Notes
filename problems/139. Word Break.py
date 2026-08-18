'''
=== 139. Word Break ===

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
    - The same word in the dictionary may be reused multiple times in the segmentation.
    - You may assume the dictionary does not contain duplicate words.

Example 1:
    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.
Example 3:
    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: false
'''
# === 32ms(95.33%) && 13.8MB(92.43%) === #
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mapping = {}
        for w in wordDict:
            mapping[w[0]] = mapping.get(w[0], []) + [w]
        
        n = len(s)
        
        @lru_cache(None)
        def dp(idx):
            if idx >= n:
                return True
            for w in mapping.get(s[idx], []):
                if s[idx:].startswith(w) and dp(idx+len(w)):
                    return True
            return False
        
        return dp(0)