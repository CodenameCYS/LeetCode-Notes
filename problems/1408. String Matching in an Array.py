'''
=== 1408. String Matching in an Array ===

Given an array of string words. Return all strings in words which is substring of another word in any order. 
String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:
    Input: words = ["mass","as","hero","superhero"]
    Output: ["as","hero"]
    Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
    ["hero","as"] is also a valid answer.
Example 2:
    Input: words = ["leetcode","et","code"]
    Output: ["et","code"]
    Explanation: "et", "code" are substring of "leetcode".
Example 3:
    Input: words = ["blue","green","bu"]
    Output: []
 
Constraints:
    1. 1 <= words.length <= 100
    2. 1 <= words[i].length <= 30
    3. words[i] contains only lowercase English letters.
    4. It's guaranteed that words[i] will be unique.
'''
# === 48ms && 13.9MB === #
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return []
        words = sorted(words, key=lambda x: len(x))
        ans = []
        for i, w in enumerate(words[:-1]):
            if any(it.find(w) != -1 for it in words[i+1:]):
                ans.append(w)
        return ans