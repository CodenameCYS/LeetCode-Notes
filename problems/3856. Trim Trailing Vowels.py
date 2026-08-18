'''
=== 3856. Trim Trailing Vowels ===

You are given a string s that consists of lowercase English letters.
Return the string obtained by removing all trailing vowels from s.
The vowels consist of the characters 'a', 'e', 'i', 'o', and 'u'.

Example 1:
    Input: s = "idea"
    Output: "id"
    Explanation:
    Removing "idea", we obtain the string "id".
Example 2:
    Input: s = "day"
    Output: "day"
    Explanation:
    There are no trailing vowels in the string "day".
Example 3:
    Input: s = "aeiou"
    Output: ""
    Explanation:
    Removing "aeiou", we obtain the string "".

Constraints:
    1. 1 <= s.length <= 100
    2. s consists of only lowercase English letters.
'''
# === 0ms && 19.11MB === #
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        while s and s[-1] in "aeiou":
            s = s[:-1]
        return s