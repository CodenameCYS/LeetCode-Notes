'''
=== 2825. Make String a Subsequence Using Cyclic Increments ===

You are given two 0-indexed strings str1 and str2.
In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.
Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.
Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

Example 1:
    Input: str1 = "abc", str2 = "ad"
    Output: true
    Explanation: Select index 2 in str1.
    Increment str1[2] to become 'd'. 
    Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.
Example 2:
    Input: str1 = "zc", str2 = "ad"
    Output: true
    Explanation: Select indices 0 and 1 in str1. 
    Increment str1[0] to become 'a'. 
    Increment str1[1] to become 'd'. 
    Hence, str1 becomes "ad" and str2 is now a subsequence. Therefore, true is returned.
Example 3:
    Input: str1 = "ab", str2 = "d"
    Output: false
    Explanation: In this example, it can be shown that it is impossible to make str2 a subsequence of str1 using the operation at most once. 
    Therefore, false is returned.
 
Constraints:
    1. 1 <= str1.length <= 105
    2. 1 <= str2.length <= 105
    3. str1 and str2 consist of only lowercase English letters.
'''
# === 120ms && 17.2MB === #
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        def move_cyclic(ch):
            return "a" if ch == "z" else chr(ord(ch)+1)
        
        idx, n = 0, len(str2)
        for ch in str1:
            if idx >= n:
                break
            if ch == str2[idx]:
                idx += 1
            elif move_cyclic(ch) == str2[idx]:
                idx += 1
        return idx == n