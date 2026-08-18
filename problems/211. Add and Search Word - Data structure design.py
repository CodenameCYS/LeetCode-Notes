'''
=== 211. Add and Search Word - Data structure design ===

Design a data structure that supports the following two operations:
    - void addWord(word)
    - bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:
    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

Note:
    - You may assume that all words are consist of lowercase letters a-z.
'''
class TrieTree:
    def __init__(self):
        self.children = {}
        self.eos = False
# === 420ms(38.97%) && 28.6MB(36.74%) === #
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieTree()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.root
        for c in word:
            root = root.children.setdefault(c, TrieTree())
        root.eos = True
        return

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)
        def dfs(root, i):
            if i == n:
                return root.eos
            if word[i] != '.':
                if word[i] not in root.children.keys():
                    return False
                else:
                    return dfs(root.children[word[i]], i+1)
            else:
                return any(dfs(root.children[c], i+1) for c in root.children.keys())
            
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)