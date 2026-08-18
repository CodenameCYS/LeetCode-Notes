'''
=== 3120. Count the Number of Special Characters I ===

You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.

Example 1:
    Input: word = "aaAbcBC"
    Output: 3
    Explanation:
    The special characters in word are 'a', 'b', and 'c'.
Example 2:
    Input: word = "abc"
    Output: 0
    Explanation:
    No character in word appears in uppercase.
Example 3:
    Input: word = "abBCab"
    Output: 1
    Explanation:
    The only special character in word is 'b'.

Constraints:
    1. 1 <= word.length <= 50
    2. word consists of only lowercase and uppercase English letters.
'''
# === 34ms && 16.6MB === #
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        ans = 0
        for ch in string.ascii_lowercase:
            if ch in chars and chr(ord(ch) - ord('a') + ord('A')) in chars:
                ans += 1
        return ans