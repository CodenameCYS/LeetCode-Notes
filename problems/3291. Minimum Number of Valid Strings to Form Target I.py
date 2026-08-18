'''
=== 3291. Minimum Number of Valid Strings to Form Target I ===

You are given an array of strings words and a string target.
A string x is called valid if x is a prefix of any string in words.
Return the minimum number of valid strings that can be concatenated to form target. If it is not possible to form target, return -1.
A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.

Example 1:
    Input: words = ["abc","aaaaa","bcdef"], target = "aabcdabc"
    Output: 3
    Explanation:
    The target string can be formed by concatenating:
    Prefix of length 2 of words[1], i.e. "aa".
    Prefix of length 3 of words[2], i.e. "bcd".
    Prefix of length 3 of words[0], i.e. "abc".
Example 2:
    Input: words = ["abababab","ab"], target = "ababaababa"
    Output: 2
    Explanation:
    The target string can be formed by concatenating:
    Prefix of length 5 of words[0], i.e. "ababa".
    Prefix of length 5 of words[0], i.e. "ababa".
Example 3:
    Input: words = ["abcdef"], target = "xyz"
    Output: -1

Constraints:
    1. 1 <= words.length <= 100
    2. 1 <= words[i].length <= 5 * 103
    3. The input is generated such that sum(words[i].length) <= 105.
    4. words[i] consists only of lowercase English letters.
    5. 1 <= target.length <= 5 * 103
    6. target consists only of lowercase English letters.
'''
# === 12771ms && 41.8MB === #
class Trie:
    def __init__(self):
        self.trie = {}
    
    def add_word(self, word):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie["eos"] = ""

    def find(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return "eos" in trie

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for w in words:
            trie.add_word(w)
            
        n = len(target)
        
        @lru_cache(None)
        def dp(idx):
            if idx >= n:
                return 0
            _trie = trie.trie
            ans = math.inf
            while idx < n and target[idx] in _trie:
                _trie = _trie[target[idx]]
                idx += 1
                ans = min(ans, 1+dp(idx))
            return ans
        
        ans = dp(0)
        return ans if ans != math.inf else -1
            
            