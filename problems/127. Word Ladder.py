'''
=== 127. Word Ladder ===

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
    1. Only one letter can be changed at a time.
    2. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
    1. Return 0 if there is no such transformation sequence.
    2. All words have the same length.
    3. All words contain only lowercase alphabetic characters.
    4. You may assume no duplicates in the word list.
    5. You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
    Input:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    - Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.
Example 2:
    Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
    Output: 0
    - Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''
# === Time Limit Exceeded === #
class Solution:
    def diff(self, s1, s2):
        ans = len([w1 for w1,w2 in zip(s1, s2) if w1 != w2])
        return ans
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str], stopList=set(), distance=1) -> int:
        if endWord not in wordList or len(beginWord) != len(endWord):
            return 0
        queue = [endWord]
        record = {endWord:1}
        while queue:
            tmp = queue[0]
            if self.diff(tmp, beginWord) == 1:
                return record[tmp] + 1
            i = 0
            while wordList:
                w = wordList[i]
                if self.diff(w, tmp) == 1:
                    record[w] = record[tmp] + 1
                    queue.append(w)
                    wordList.remove(w)
                else:
                    i += 1
                if i >= len(wordList):
                    break
            queue = queue[1:]
        return 0
    
# === 480ms(31.80%) && 15MB(7.76%) === #
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList[0])
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        have_seen = set([beginWord])
        queue = [(beginWord, 1)]
        while queue:
            w, t = queue.pop(0)
            for i in range(n):
                for c in string.ascii_lowercase:
                    w2 = w[:i] + c + w[i+1:]
                    if w2 == endWord:
                        return t+1
                    if w2 not in have_seen and w2 in wordList:
                        queue.append((w2, t+1))
                        have_seen.add(w2)
        return 0