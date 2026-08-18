'''
=== 3093. Longest Common Suffix Queries ===

You are given two arrays of strings wordsContainer and wordsQuery.
For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.
Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].

Example 1:
    Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]
    Output: [1,1,1]
    Explanation:
    Let's look at each wordsQuery[i] separately:
    - For wordsQuery[0] = "cd", strings from wordsContainer that share the longest common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
    - For wordsQuery[1] = "bcd", strings from wordsContainer that share the longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
    - For wordsQuery[2] = "xyz", there is no string from wordsContainer that shares a common suffix. Hence the longest common suffix is "", that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
Example 2:
    Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]
    Output: [2,0,2]
    Explanation:
    Let's look at each wordsQuery[i] separately: 
    - For wordsQuery[0] = "gh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
    - For wordsQuery[1] = "acbfgh", only the string at index 0 shares the longest common suffix "fgh". Hence it is the answer, even though the string at index 2 is shorter.
    - For wordsQuery[2] = "acbfegh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
 
Constraints:
    1. 1 <= wordsContainer.length, wordsQuery.length <= 104
    2. 1 <= wordsContainer[i].length <= 5 * 103
    3. 1 <= wordsQuery[i].length <= 5 * 103
    4. wordsContainer[i] consists only of lowercase English letters.
    5. wordsQuery[i] consists only of lowercase English letters.
    6. Sum of wordsContainer[i].length is at most 5 * 105.
    7. Sum of wordsQuery[i].length is at most 5 * 105.
'''
class Trie:
    def __init__(self):
        self.trie = {}
        self.init = -1
    
    def add_word(self, word, idx):
        trie = self.trie
        if self.init == -1:
            self.init = idx
        for c in word:
            _, trie = trie.setdefault(c, (idx, {}))
        return

    def find(self, word):
        trie = self.trie
        ans = self.init
        for c in word:
            if c not in trie:
                break
            ans, trie = trie[c]
        return ans
# === 1197ms && 144.7MB === #
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        words = [(len(w), i, w) for i, w in enumerate(wordsContainer)]
        words = sorted(words)
        
        trie = Trie()
        for _, i, word in words:
            trie.add_word(word[::-1], i)
        # print(trie.trie)
        
        ans = [trie.find(word[::-1]) for word in wordsQuery]
        return ans