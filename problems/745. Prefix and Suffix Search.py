'''
=== 745. Prefix and Suffix Search ===

Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.
Implement the WordFilter class:
    - WordFilter(string[] words) Initializes the object with the words in the dictionary.
    - f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 
Example 1:
    Input
    ["WordFilter", "f"]
    [[["apple"]], ["a", "e"]]
    Output
    [null, 0]
    Explanation
    WordFilter wordFilter = new WordFilter(["apple"]);
    wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
 
Constraints:
    1. 1 <= words.length <= 15000
    2. 1 <= words[i].length <= 10
    3. 1 <= prefix.length, suffix.length <= 10
    4. words[i], prefix and suffix consist of lower-case English letters only.
    5. At most 15000 calls will be made to the function f.
'''
# === 2192ms(10.27%) && 25.1MB(93.51%) === #
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_trie = {}
        self.suffix_trie = {}
        
        for idx, word in enumerate(words):
            trie = self.prefix_trie
            for c in word:
                trie = trie.setdefault(c, {})
            trie["eos"] = idx
            
            trie = self.suffix_trie
            for c in word[::-1]:
                trie = trie.setdefault(c, {})
            trie["eos"] = idx

    def f(self, prefix: str, suffix: str) -> int:
        
        def find(word, trie):
            for c in word:
                if c not in trie:
                    return set()
                trie = trie[c]
            
            ans = set()
            def dfs(trie):
                nonlocal ans
                for k, v in trie.items():
                    if k == "eos":
                        ans.add(v)
                    else:
                        dfs(v)
            dfs(trie)
            return ans
        
        prefix_match = find(prefix, self.prefix_trie)
        suffix_match = find(suffix[::-1], self.suffix_trie)
        return max(prefix_match & suffix_match) if len(prefix_match & suffix_match) != 0 else -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)