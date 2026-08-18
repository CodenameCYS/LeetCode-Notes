'''
=== 472. Concatenated Words ===

Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
    Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
    "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:
    1. The number of elements of the given array will not exceed 10,000
    2. The length sum of elements in the given array will not exceed 600,000.
    3. All the input string will only include lower case letters.
    4. The returned elements order does not matter.
'''
class Trie:
    def __init__(self, words):
        self.trie = {}
        for word in words:
            if word == "":
                continue
            self.add(word)
            
    def add(self, word):
        trie = self.trie
        n = len(word)
        for c in word:
            trie = trie.setdefault(c, {})
        trie["eos"] = n
        
    def find(self, word, allow_full_match = False):
        candidates = []
        trie = self.trie
        for c in word:
            if "eos" in trie:
                candidates.append(word[trie["eos"]:])
            if c not in trie:
                return any(self.find(w, allow_full_match=True) for w in candidates)
            trie = trie[c]
        if allow_full_match and "eos" in trie:
            return True
        return any(self.find(w, allow_full_match=True) for w in candidates)
            
# === 808ms(45.32%) && 24.6MB(64%) === #
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie(words)
        ans = []
        for word in words:
            if trie.find(word, allow_full_match=False):
                ans.append(word)
        return ans