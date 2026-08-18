'''
=== 3992. Rearrange String to Avoid Character Pair ===

You are given a string s and two distinct lowercase English letters x and y.
Rearrange the characters of s to construct a new string t such that:
    - t is a permutation of s.
    - Every occurrence of y appears before every occurrence of x in t.
Return any valid string t.

Example 1:
    Input: s = "aabc", x = "a", y = "c"
    Output: "cbaa"
    Explanation:
    The string "cbaa" is a permutation of "aabc", and every occurrence of 'c' appears before every occurrence of 'a'.
Example 2:
    Input: s = "dcab", x = "d", y = "b"
    Output: "cabd"
    Explanation:
    The string "cabd" is a permutation of "dcab", and every occurrence of 'b' appears before every occurrence of 'd'.
Example 3:
    Input: s = "axe", x = "o", y = "x"
    Output: "axe"
    Explanation:
    The string "axe" is already valid. Since 'o' does not occur in the string, the required condition is automatically satisfied.

Constraints:
    1. 1 <= s.length <= 100
    2. s consists of lowercase English letters.
    3. x and y are lowercase English letters.
    4. x != y
'''
# === 3ms && 19.54MB === #
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        cnt = Counter(s)
        remain = "".join([ch for ch in s if ch not in {x, y}])
        return y*cnt[y] + remain + x*cnt[x]