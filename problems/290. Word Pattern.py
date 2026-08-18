'''
=== 290. Word Pattern ===

Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true
Example 2:
    Input:pattern = "abba", str = "dog cat cat fish"
    Output: false
Example 3:
    Input: pattern = "aaaa", str = "dog cat cat dog"
    Output: false
Example 4:
    Input: pattern = "abba", str = "dog dog dog dog"
    Output: false

Notes:
- You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''
# === 36ms(55.03%) & 13.1MB(5.47%) === #
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split()
        # print(s)
        if len(s) != len(pattern):
            return False
        record1 = {}
        record2 = {}
        for w,p in zip(s,pattern):
            if w in record1.keys() and record1[w] != p:
                return False
            else:
                record1[w] = p
            if p in record2.keys() and record2[p] != w:
                return False
            else:
                record2[p] = w
        return True
        