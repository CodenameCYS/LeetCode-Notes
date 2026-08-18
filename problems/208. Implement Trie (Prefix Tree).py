'''
=== 208. Implement Trie (Prefix Tree) ===

Implement a trie with insert, search, and startsWith methods.

Example:
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // returns true
    trie.search("app");     // returns false
    trie.startsWith("app"); // returns true
    trie.insert("app");   
    trie.search("app");     // returns true

Note:
    1. You may assume that all inputs are consist of lowercase letters a-z.
    2. All inputs are guaranteed to be non-empty strings.
'''
# === 172ms(82.83%) && 27.5MB(69.77%) === #
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cache = self.cache
        for c in word:
            cache = cache.setdefault(c, {})
        cache["eos"] = {}
        return

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cache = self.cache
        for c in word:
            if c not in cache.keys():
                return False
            cache = cache[c]
        return "eos" in cache.keys()
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cache = self.cache
        for c in prefix:
            if c not in cache.keys():
                return False
            cache = cache[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)