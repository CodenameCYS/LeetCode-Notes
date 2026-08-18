'''
=== 676. Implement Magic Dictionary ===

Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.
Implement the MagicDictionary class:
    - MagicDictionary() Initializes the object.
    - void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
    - bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.
 
Example 1:
    Input
    ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
    [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
    Output
    [null, null, false, true, false, false]
    Explanation
    MagicDictionary magicDictionary = new MagicDictionary();
    magicDictionary.buildDict(["hello", "leetcode"]);
    magicDictionary.search("hello"); // return False
    magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
    magicDictionary.search("hell"); // return False
    magicDictionary.search("leetcoded"); // return False
 
Constraints:
    1. 1 <= dictionary.length <= 100
    2. 1 <= dictionary[i].length <= 100
    3. dictionary[i] consists of only lower-case English letters.
    4. All the strings in dictionary are distinct.
    5. 1 <= searchWord.length <= 100
    6. searchWord consists of only lower-case English letters.
    7. buildDict will be called only once before search.
    8. At most 100 calls will be made to search.
'''
# === 164ms(34.51%) && 16.3MB(16.79%) === #
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            trie = self.trie
            for c in word:
                trie = trie.setdefault(c, {})
            trie["eos"] = ''


    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        
        def dfs(idx, trie, counter):
            if idx == n:
                return "eos" in trie and counter == 1
            if counter == 0:
                for k, v in trie.items():
                    if k == searchWord[idx]:
                        match = dfs(idx+1, v, 0)
                        if match:
                            return True
                    else:
                        match = dfs(idx+1, v, 1)
                        if match:
                            return True
                return False
            else:
                if searchWord[idx] not in trie:
                    return False
                return dfs(idx+1, trie[searchWord[idx]], 1)
        
        return dfs(0, self.trie, 0)
            


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)