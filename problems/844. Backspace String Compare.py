'''
=== 844. Backspace String Compare ===

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".
Example 2:
    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".
Example 3:
    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".
Example 4:
    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

Note:
    1. 1 <= S.length <= 200
    2. 1 <= T.length <= 200
    3. S and T only contain lowercase letters and '#' characters.

Follow up:
    - Can you solve it in O(N) time and O(1) space?
'''
# === 56ms(5.40%) && 13.8MB(66.84%) === #
class Solution:
    def get_string(self, s):
        cache = []
        for c in s:
            if c != '#':
                cache.append(c)
            elif cache != []:
                cache.pop()
        return "".join(cache)
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.get_string(S) == self.get_string(T)