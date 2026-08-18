'''
=== 3563. Lexicographically Smallest String After Adjacent Removals ===

You are given a string s consisting of lowercase English letters.
You can perform the following operation any number of times (including zero):
    - Remove any pair of adjacent characters in the string that are consecutive in the alphabet, in either order (e.g., 'a' and 'b', or 'b' and 'a').
    - Shift the remaining characters to the left to fill the gap.
Return the lexicographically smallest string that can be obtained after performing the operations optimally.
A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
If the first min(a.length, b.length) characters do not differ, then the shorter string is the lexicographically smaller one.
Note: Consider the alphabet as circular, thus 'a' and 'z' are consecutive.

Example 1:
    Input: s = "abc"
    Output: "a"
    Explanation:
    Remove "bc" from the string, leaving "a" as the remaining string.
    No further operations are possible. Thus, the lexicographically smallest string after all possible removals is "a".
Example 2:
    Input: s = "bcda"
    Output: ""
    Explanation:
    Remove "cd" from the string, leaving "ba" as the remaining string.
    Remove "ba" from the string, leaving "" as the remaining string.
    No further operations are possible. Thus, the lexicographically smallest string after all possible removals is "".
Example 3:
    Input: s = "zdce"
    Output: "zdce"
    Explanation:
    Remove "dc" from the string, leaving "ze" as the remaining string.
    No further operations are possible on "ze".
    However, since "zdce" is lexicographically smaller than "ze", the smallest string after all possible removals is "zdce".
 
Constraints:
    1. 1 <= s.length <= 250
    2. s consists only of lowercase English letters.
'''
# === 6771ms && 18.5MB === #
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        remEmpty = [[False] * n for _ in range(n)]
        
        def is_consecutive(a, b):
            d = abs(ord(a) - ord(b))
            return d == 1 or d == 25
        
        for i in range(n - 1):
            if is_consecutive(s[i], s[i + 1]):
                remEmpty[i][i + 1] = True
        for L in range(4, n + 1, 2):
            for i in range(n - L + 1):
                j = i + L - 1
                for k in range(i + 1, j + 1, 2):
                    if is_consecutive(s[i], s[k]) and (k == i + 1 or remEmpty[i + 1][k - 1]) and (k == j or remEmpty[k + 1][j]):
                        remEmpty[i][j] = True
                        break
        f = [""] * (n + 1)
        for i in range(n - 1, -1, -1):
            best = s[i] + f[i + 1]
            for j in range(i + 1, n, 2):
                if remEmpty[i][j] and f[j + 1] < best:
                    best = f[j + 1]
            f[i] = best
        return f[0]