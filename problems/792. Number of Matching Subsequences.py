'''
=== 792. Number of Matching Subsequences ===

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
    Input: 
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    Output: 3
    Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

Note:
    1. All words in words and S will only consists of lowercase letters.
    2. The length of S will be in the range of [1, 50000].
    3. The length of words will be in the range of [1, 5000].
    4. The length of words[i] will be in the range of [1, 50].
'''
# === 2064ms(16.07%) && 15.1MB(25%) === #
class Solution:
    def match(self, S, w):
        if (S, w) in self.cache.keys():
            return self.cache[(S, w)]
        lw = len(w)
        ls = len(S)
        j = 0
        for i in range(ls):
            if S[i] == w[j]:
                j += 1
            if j >= lw:
                break
        ans = j >= lw
        self.cache[(S,w)] = ans
        return ans
    
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        self.cache = {}
        ans = 0
        for w in words:
            if self.match(S, w):
                ans += 1
        return ans