'''
=== 3485. Longest Common Prefix of K Strings After Removal ===

You are given an array of strings words and an integer k.
For each index i in the range [0, words.length - 1], find the length of the longest common prefix among any k strings (selected at distinct indices) from the remaining array after removing the ith element.
Return an array answer, where answer[i] is the answer for ith element. If removing the ith element leaves the array with fewer than k strings, answer[i] is 0.
A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.
A substring is a contiguous sequence of characters within a string.
 
Example 1:
    Input: words = ["jump","run","run","jump","run"], k = 2
    Output: [3,4,4,3,4]
    Explanation:
    Removing index 0 ("jump"):
    words becomes: ["run", "run", "jump", "run"]. "run" occurs 3 times. Choosing any two gives the longest common prefix "run" (length 3).
    Removing index 1 ("run"):
    words becomes: ["jump", "run", "jump", "run"]. "jump" occurs twice. Choosing these two gives the longest common prefix "jump" (length 4).
    Removing index 2 ("run"):
    words becomes: ["jump", "run", "jump", "run"]. "jump" occurs twice. Choosing these two gives the longest common prefix "jump" (length 4).
    Removing index 3 ("jump"):
    words becomes: ["jump", "run", "run", "run"]. "run" occurs 3 times. Choosing any two gives the longest common prefix "run" (length 3).
    Removing index 4 ("run"):
    words becomes: ["jump", "run", "run", "jump"]. "jump" occurs twice. Choosing these two gives the longest common prefix "jump" (length 4).
Example 2:
    Input: words = ["dog","racer","car"], k = 2
    Output: [0,0,0]
    Explanation:
    Removing any index results in an answer of 0.
 
Constraints:
    1. 1 <= k <= words.length <= 105
    2. 1 <= words[i].length <= 104
    3. words[i] consists of lowercase English letters.
    4. The sum of words[i].length is smaller than or equal 105.
'''
class Trie:
    def __init__(self, k):
        self.k = k
        self.cnt = defaultdict(int)
        self.valid = []
    
    def add_word(self, word):
        prefix = ""
        for c in word:
            prefix += c
            self.cnt[prefix] += 1
            if self.cnt[prefix] >= self.k:
                bisect.insort(self.valid, len(prefix))
        return
        
    def del_word(self, word):
        prefix = ""
        for c in word:
            prefix += c
            self.cnt[prefix] -= 1
            if self.cnt[prefix] == self.k-1:
                self.valid.pop(bisect.bisect_left(self.valid, len(prefix)))
        return
# === 5962ms && 131.3MB === #
class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)
        if n <= k:
            return [0 for _ in words]
        
        trie = Trie(k)
        for word in words[1:]:
            trie.add_word(word)
        ans = [0 for _ in words]
        ans[0] = trie.valid[-1] if len(trie.valid) > 0 else 0
        for i in range(n-1):
            trie.add_word(words[i])
            trie.del_word(words[i+1])
            ans[i+1] = trie.valid[-1] if len(trie.valid) > 0 else 0
        return ans
            