'''
=== 1684. Count the Number of Consistent Strings ===

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.

Example 1:
    Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    Output: 2
    Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:
    Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
    Output: 7
    Explanation: All strings are consistent.
Example 3:
    Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
    Output: 4
    Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 
Constraints:
    1. 1 <= words.length <= 104
    2. 1 <= allowed.length <= 26
    3. 1 <= words[i].length <= 10
    4. The characters in allowed are distinct.
    5. words[i] and allowed contain only lowercase English letters.
'''
# === 284ms && 16.1MB === #
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        allowed = set(allowed)
        # print(allowed)
        for w in words:
            w = set(w)
            # print(w)
            if w.issubset(allowed):
                cnt += 1
        return cnt