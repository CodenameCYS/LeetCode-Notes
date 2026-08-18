'''
=== 1032. Stream of Characters ===

Implement the StreamChecker class as follows:
    - StreamChecker(words): Constructor, init the data structure with the given words.
    - query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 
Example:
    StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
    streamChecker.query('a');          // return false
    streamChecker.query('b');          // return false
    streamChecker.query('c');          // return false
    streamChecker.query('d');          // return true, because 'cd' is in the wordlist
    streamChecker.query('e');          // return false
    streamChecker.query('f');          // return true, because 'f' is in the wordlist
    streamChecker.query('g');          // return false
    streamChecker.query('h');          // return false
    streamChecker.query('i');          // return false
    streamChecker.query('j');          // return false
    streamChecker.query('k');          // return false
    streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 
Note:
    1. 1 <= words.length <= 2000
    2. 1 <= words[i].length <= 2000
    3. Words will only consist of lowercase English letters.
    4. Queries will only consist of lowercase English letters.
    5. The number of queries is at most 40000.
'''
class Trie:
    def __init__(self):
        self.trie = {}
    
    def add(self, word):
        trie = self.trie
        for c in word[::-1]:
            trie = trie.setdefault(c, {})
        trie["eos"] = {}
        
    def find(self, char_list):
        trie = self.trie
        for c in char_list:
            if c not in trie.keys():
                return False
            trie = trie[c]
            if "eos" in trie.keys():
                return True
        return False

# === 2356ms(22.51%) && 37.5MB === #
class StreamChecker:
    def __init__(self, words: List[str]):
        self.query_list = []
        self.trie = Trie()
        for word in words:
            self.trie.add(word)
        return

    def query(self, letter: str):
        self.query_list.insert(0, letter)
        return self.trie.find(self.query_list)

# === 740ms(74.60%) && 37.3MB === #
class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.querys = ""
        self.trie = {}
        for word in words:
            trie = self.trie
            for c in word[::-1]:
                trie = trie.setdefault(c, {})
            trie["eos"] = ""

    def query(self, letter: str):
        self.querys = letter + self.querys
        trie = self.trie
        for c in self.querys:
            if c not in trie:
                return False
            trie = trie[c]
            if "eos" in trie:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)