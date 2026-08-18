'''
=== 336. Palindrome Pairs ===

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:
    Input: words = ["abcd","dcba","lls","s","sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]]
    Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:
    Input: words = ["bat","tab","cat"]
    Output: [[0,1],[1,0]]
    Explanation: The palindromes are ["battab","tabbat"]
Example 3:
    Input: words = ["a",""]
    Output: [[0,1],[1,0]]
 
Constraints:
    1. 1 <= words.length <= 5000
    2. 0 <= words[i] <= 300
    3. words[i] consists of lower-case English letters.
'''
class Trie:
    def __init__(self, words=[]):
        self.trie = {}
        for i, word in enumerate(words):
            self.add(word, i)
    
    def add(self, word, idx):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie["eos"] = idx
        
    def find(self, word):
        trie = self.trie
        candidates = []
        for c in word:
            if "eos" in trie:
                candidates.append(trie["eos"])
            if c not in trie:
                return candidates
            trie = trie[c]
        
        def dp(trie):
            nonlocal candidates
            for k, v in trie.items():
                if k == "eos":
                    candidates.append(v)
                else:
                    dp(v)
        dp(trie)
        return candidates
# === 600ms(66.87%) && 17.8MB(29.99%) === #
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            i = 0
            j = len(s)-1
            while i<j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        trie = Trie(words)
        # print(trie.trie)
        ans = []
        for i, word in enumerate(words):
            candidates = trie.find(word[::-1])
            # print(i, word, candidates)
            for j in candidates:
                if i != j and is_palindrome(words[j] + words[i]):
                    ans.append([j, i])
        return ans
            