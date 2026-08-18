'''
=== 3121. Count the Number of Special Characters II ===

You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
Return the number of special letters in word.

Example 1:
    Input: word = "aaAbcBC"
    Output: 3
    Explanation:
    The special characters are 'a', 'b', and 'c'.
Example 2:
    Input: word = "abc"
    Output: 0
    Explanation:
    There are no special characters in word.
Example 3:
    Input: word = "AbBCab"
    Output: 0
    Explanation:
    There are no special characters in word.

Constraints:
    1. 1 <= word.length <= 2 * 105
    2. word consists of only lowercase and uppercase English letters.
'''
# === 322ms && 18.5MB === #
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        status = [0 for _ in range(26)]
        seen = set()
        for ch in word:
            if ch in string.ascii_lowercase:
                idx = ord(ch) - ord('a')
                if string.ascii_uppercase[idx] in seen:
                    status[idx] = -1
            else:
                idx = ord(ch) - ord('A')
                if string.ascii_lowercase[idx] in seen and status[idx] == 0:
                    status[idx] = 1
            seen.add(ch)
        return Counter(status)[1]