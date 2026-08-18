'''
=== 2781. Length of the Longest Valid Substring ===

You are given a string word and an array of strings forbidden.
A string is called valid if none of its substrings are present in forbidden.
Return the length of the longest valid substring of the string word.
A substring is a contiguous sequence of characters in a string, possibly empty.

Example 1:
    Input: word = "cbaaaabc", forbidden = ["aaa","cb"]
    Output: 4
    Explanation: There are 9 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", and "aabc". The length of the longest valid substring is 4. 
    It can be shown that all other substrings contain either "aaa" or "cb" as a substring. 
Example 2:
    Input: word = "leetcode", forbidden = ["de","le","e"]
    Output: 4
    Explanation: There are 11 valid substrings in word: "l", "t", "c", "o", "d", "tc", "co", "od", "tco", "cod", and "tcod". The length of the longest valid substring is 4.
    It can be shown that all other substrings contain either "de", "le", or "e" as a substring. 
    
Constraints:
    1. 1 <= word.length <= 105
    2. word consists only of lowercase English letters.
    3. 1 <= forbidden.length <= 105
    4. 1 <= forbidden[i].length <= 10
    5. forbidden[i] consists only of lowercase English letters.
'''
class Trie:
    def __init__(self):
        self.trie = {}
    
    def add_word(self, word):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie["eos"] = word

    def find(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return "eos" in trie
    
    def find_any_word(self, s):
        trie = self.trie
        for ch in s:
            if ch not in trie:
                return ""
            trie = trie[ch]
            if "eos" in trie:
                return trie["eos"]
        return ""
            
# === 2358ms && 194.3MB === #
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        trie = Trie()
        for w in forbidden:
            trie.add_word(w)
            
        s = ""
        res = 0
        for ch in word[::-1]:
            s = ch + s
            w = trie.find_any_word(s)
            if w != "":
                s = w[:-1]
            res = max(res, len(s))
        return res