'''
=== 140. Word Break II ===

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
    - The same word in the dictionary may be reused multiple times in the segmentation.
    - You may assume the dictionary does not contain duplicate words.

Example 1:
    Input:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    Output:
    [
        "cats and dog",
        "cat sand dog"
    ]
Example 2:
    Input:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    Output:
    [
        "pine apple pen apple",
        "pineapple pen apple",
        "pine applepen apple"
    ]
    Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:
    Input:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output:
    []
'''
# === 60ms(40.94%) && 14.1MB === #
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mapping = {}
        for w in wordDict:
            mapping[w[0]] = mapping.get(w[0], []) + [w]
        
        n = len(s)

        @lru_cache(None)
        def dp(idx):
            if idx >= n:
                return [[]]
            output = []
            for w in mapping.get(s[idx], []):
                if s[idx:].startswith(w):
                    for res in dp(idx+len(w)):
                        output.append([w] + res)
            return output
        
        ans = dp(0)
        
        return [" ".join(tokens) for tokens in ans]
            