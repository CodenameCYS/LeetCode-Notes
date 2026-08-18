'''
=== 677. Map Sum Pairs ===

Implement a MapSum class with insert, and sum methods.
For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
    Input: insert("apple", 3), Output: Null
    Input: sum("ap"), Output: 3
    Input: insert("app", 2), Output: Null
    Input: sum("ap"), Output: 5
'''
# === 28ms(92.32%) && 13.9MB(47.73%) === #
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, key: str, val: int) -> None:
        trie = self.trie
        for c in key:
            trie = trie.setdefault(c, {})
        trie["eos"] = val

    def sum(self, prefix: str) -> int:
        trie = self.trie
        for c in prefix:
            if c not in trie:
                return 0
            trie = trie[c]
            
        ans = 0
        def dfs(trie):
            nonlocal ans
            for k, v in trie.items():
                if k == "eos":
                    ans += v
                else:
                    dfs(v)
        dfs(trie)
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)