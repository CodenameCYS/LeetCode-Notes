'''
=== 1876. Substrings of Size Three with Distinct Characters ===

A string is good if there are no repeated characters.
Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.

Example 1:
    Input: s = "xyzzaz"
    Output: 1
    Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
    The only good substring of length 3 is "xyz".
Example 2:
    Input: s = "aababcabc"
    Output: 4
    Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
    The good substrings are "abc", "bca", "cab", and "abc".
 
Constraints:
    1. 1 <= s.length <= 100
    2. s​​​​​​ consists of lowercase English letters.
'''
# === 60ms && 14.2MB === #
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return 0
        cnt = Counter(s[:3])
        res = 1 if all(x <= 1 for x in cnt.values()) else 0
        for i in range(3, n):
            cnt[s[i]] += 1
            cnt[s[i-3]] -= 1
            if all(x <= 1 for x in cnt.values()):
                res += 1
        return res
        
        
        