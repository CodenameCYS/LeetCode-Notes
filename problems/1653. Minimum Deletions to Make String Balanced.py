'''
=== 1653. Minimum Deletions to Make String Balanced ===

You are given a string s consisting only of characters 'a' and 'b'​​​​.
You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
Return the minimum number of deletions needed to make s balanced.

Example 1:
    Input: s = "aababbab"
    Output: 2
    Explanation: You can either:
    Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
    Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:
    Input: s = "bbaaaaabb"
    Output: 2
    Explanation: The only solution is to delete the first two characters.
 
Constraints:
    1. 1 <= s.length <= 105
    2. s[i] is 'a' or 'b'​​.
'''
# === 1296ms && 19.8MB === #
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a = [0 for _ in range(n)]
        b = [0 for _ in range(n)]
        
        for i in range(n-1):
            if s[i] == 'b':
                b[i+1] = b[i]+1
            else:
                b[i+1] = b[i]
        for i in range(n-1, 0, -1):
            if s[i] == 'a':
                a[i-1] = a[i] + 1
            else:
                a[i-1] = a[i]
        return min(a[i] + b[i] for i in range(n))