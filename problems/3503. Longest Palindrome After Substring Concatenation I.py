'''
=== 3503. Longest Palindrome After Substring Concatenation I ===

You are given two strings, s and t.
You can create a new string by selecting a substring from s (possibly empty) and a substring from t (possibly empty), then concatenating them in order.
Return the length of the longest palindrome that can be formed this way.
A substring is a contiguous sequence of characters within a string.
A palindrome is a string that reads the same forward and backward.

Example 1:
    Input: s = "a", t = "a"
    Output: 2
    Explanation:
    Concatenating "a" from s and "a" from t results in "aa", which is a palindrome of length 2.
Example 2:
    Input: s = "abc", t = "def"
    Output: 1
    Explanation:
    Since all characters are different, the longest palindrome is any single character, so the answer is 1.
Example 3:
    Input: s = "b", t = "aaaa"
    Output: 4
    Explanation:
    Selecting "aaaa" from t is the longest palindrome, so the answer is 4.
Example 4:
    Input: s = "abcde", t = "ecdba"
    Output: 5
    Explanation:
    Concatenating "abc" from s and "ba" from t results in "abcba", which is a palindrome of length 5.

Constraints:
    1. 1 <= s.length, t.length <= 30
    2. s and t consist of lowercase English letters.
'''
class Trie:
    def __init__(self):
        self.trie = {}
    
    def add_word(self, word):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie["eos"] = ""

    def find(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return "eos" in trie
    
    def find_longest_prefix(self, word):
        prefix = ""
        trie = self.trie
        for c in word:
            if c not in trie:
                break
            prefix += c
            trie = trie[c]
        return prefix

def z_algorithm(s):
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = -1, -1
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r-l] == s[r]:
                r += 1
            z[i] = r-l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r-l] == s[r]:
                    r += 1
                z[i] = r-l
                r -= 1
    z[0] = n
    return z
# === 48ms && 18.5MB === #
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        ans = 0
        
        rs = s[::-1]
        trie_s = Trie()
        trie_rs = Trie()
        for i in range(n):
            trie_s.add_word(s[i:])
            trie_rs.add_word(rs[i:])
        for i in range(n):
            prefix = trie_s.find_longest_prefix(rs[i:])
            if prefix == prefix[::-1]:
                ans = max(ans, len(prefix))
        
        rt = t[::-1]
        trie_t = Trie()
        trie_rt = Trie()
        for i in range(m):
            trie_t.add_word(t[i:])
            trie_rt.add_word(rt[i:])
        for i in range(m):
            prefix = trie_t.find_longest_prefix(t[i:])
            if prefix == prefix[::-1]:
                ans = max(ans, len(prefix))
                
        for i in range(n):
            prefix = trie_rt.find_longest_prefix(s[i:])
            if i+len(prefix) == n:
                ans = max(ans, len(prefix) * 2)
            else:
                remain = s[i+len(prefix):]
                k = len(remain)
                z = z_algorithm(remain + remain[::-1])
                for j in range(k):
                    if z[k+j] == k-j:
                        ans = max(ans, len(prefix) * 2 + k-j)
                        
        for i in range(m):
            prefix = trie_s.find_longest_prefix(rt[i:])
            if i+len(prefix) == m:
                ans = max(ans, len(prefix) * 2)
            else:
                remain = rt[i+len(prefix):]
                k = len(remain)
                z = z_algorithm(remain + remain[::-1])
                for j in range(k):
                    if z[k+j] == k-j:
                        ans = max(ans, len(prefix) * 2 + k-j)

        return ans
            
                
        
        
        