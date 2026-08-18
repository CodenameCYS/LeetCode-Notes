'''
=== 2185. Counting Words With a Given Prefix ===

You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.

Example 1:
    Input: words = ["pay","attention","practice","attend"], pref = "at"
    Output: 2
    Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:
    Input: words = ["leetcode","win","loops","success"], pref = "code"
    Output: 0
    Explanation: There are no strings that contain "code" as a prefix.
    
Constraints:
    1. 1 <= words.length <= 100
    2. 1 <= words[i].length, pref.length <= 100
    3. words[i] and pref consist of lowercase English letters.
'''
# === 57ms && 14.1MB === #
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = [w for w in words if w.startswith(pref)]
        return len(res)
        