'''
=== 3213. Construct String with Minimum Cost ===

You are given a string target, an array of strings words, and an integer array costs, both arrays of the same length.
Imagine an empty string s.
You can perform the following operation any number of times (including zero):
    - Choose an index i in the range [0, words.length - 1].
    - Append words[i] to s.
    - The cost of operation is costs[i].
Return the minimum cost to make s equal to target. If it's not possible, return -1.

Example 1:
    Input: target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]
    Output: 7
    Explanation:
    The minimum cost can be achieved by performing the following operations:
    - Select index 1 and append "abc" to s at a cost of 1, resulting in s = "abc".
    - Select index 2 and append "d" to s at a cost of 1, resulting in s = "abcd".
    - Select index 4 and append "ef" to s at a cost of 5, resulting in s = "abcdef".
Example 2:
    Input: target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]
    Output: -1
    Explanation:
    It is impossible to make s equal to target, so we return -1.

Constraints:
    1. 1 <= target.length <= 5 * 104
    2. 1 <= words.length == costs.length <= 5 * 104
    3. 1 <= words[i].length <= target.length
    4. The total sum of words[i].length is less than or equal to 5 * 104.
    5. target and words[i] consist only of lowercase English letters.
    6. 1 <= costs[i] <= 104
'''
# === 10897ms && 267.2MB === #
class Trie:
    def __init__(self):
        self.trie = {}
    
    def add_word(self, word, cost):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        if "eos" not in trie:
            trie["eos"] = (word, cost)
        elif cost < trie["eos"][1]:
            trie["eos"] = (word, cost)
        return
            

    def find(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return "eos" in trie
    
    def find_all_prefix(self, word):
        prefixs = []
        trie = self.trie
        for c in word:
            if c not in trie:
                break
            trie = trie[c]
            if "eos" in trie:
                prefixs.append(trie["eos"])
        return prefixs

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        trie = Trie()
        for word, cost in zip(words, costs):
            trie.add_word(word, cost)
        n = len(target)
        ans = math.inf
        
        @lru_cache(None)
        def dp(idx):
            nonlocal ans
            if idx >= n:
                return 0
            prefixs = trie.find_all_prefix(target[idx:])
            if prefixs == []:
                return math.inf
            return min(c + dp(idx+len(w)) for w, c in prefixs)
        
        ans = dp(0)
        return ans if ans != math.inf else -1
        