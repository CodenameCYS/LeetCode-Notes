'''
=== 424. Longest Repeating Character Replacement ===

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
In one operation, you can choose any character of the string and change it to any other uppercase English character.
Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
- Both the string's length and k will not exceed 104.

Example 1:
    Input:
    s = "ABAB", k = 2
    Output:
    4
    Explanation:
    Replace the two 'A's with two 'B's or vice versa.
Example 2:
    Input:
    s = "AABABBA", k = 1
    Output:
    4
    Explanation:
    Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
'''
# === 124ms(60.12%) && 14.7MB(27.96%) === #
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        cache = defaultdict(list)
        for idx, c in enumerate(s):
            cache[c].append(idx)

        def get_length(st, ed, i, j, k):
            l = ed - st + 1
            s = j - i + 1
            diff = l - s
            return min(n, l + (k - diff))

        res = min(n, k+1)
        for c in cache:
            m = len(cache[c])
            i, j = 0, 0
            while True:
                while j < m and cache[c][j] - cache[c][i] <= j-i+k:
                    j += 1
                res = max(res, get_length(cache[c][i], cache[c][j-1], i, j-1, k))
                if j == m:
                    break
                while i < j and cache[c][j] - cache[c][i] > j-i+k:
                    i += 1
        return res