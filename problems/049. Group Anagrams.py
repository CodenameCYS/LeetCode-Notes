'''
=== 49. Group Anagrams ===

Given an array of strings, group anagrams together.

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]

Note:
    1. All inputs will be in lowercase.
    2. The order of your output does not matter.
'''
# === 104ms(55.43%) && 18MB(22.64%) === #
class Solution:
    def word2alphabet(self, s):
        alphabet = [0]*26
        for c in s:
            alphabet[ord(c)-ord('a')] += 1
        return tuple(alphabet)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            a = self.word2alphabet(s)
            if a in ans.keys():
                ans[a].append(s)
            else:
                ans[a] = [s]
        return ans.values()