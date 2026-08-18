'''
=== 3170. Lexicographically Minimum String After Removing Stars ===

You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.
While there is a '*', do the following operation:
    - Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

Example 1:
    Input: s = "aaba*"
    Output: "aab"
    Explanation:
    We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.
Example 2:
    Input: s = "abc"
    Output: "abc"
    Explanation:
    There is no '*' in the string.

Constraints:
    1. 1 <= s.length <= 105
    2. s consists only of lowercase English letters and '*'.
    3. The input is generated such that it is possible to delete all '*' characters.
'''
# === 669ms && 26.4MB === #
class Solution:
    def clearStars(self, s: str) -> str:
        q = []
        deleted = set()
        for i, ch in enumerate(s):
            if ch == "*":
                out = heapq.heappop(q)
                idx = -out[1]
                deleted.add(idx)
            else:
                heapq.heappush(q, (ch, -i))
        ans = ""
        for i, ch in enumerate(s):
            if ch != "*" and i not in deleted:
                ans += ch
        return ans