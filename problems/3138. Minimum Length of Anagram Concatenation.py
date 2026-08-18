'''
=== 3138. Minimum Length of Anagram Concatenation ===

You are given a string s, which is known to be a concatenation of anagrams of some string t.
Return the minimum possible length of the string t.
An anagram is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".

Example 1:
    Input: s = "abba"
    Output: 2
    Explanation:
    One possible string t could be "ba".
Example 2:
    Input: s = "cdef"
    Output: 4
    Explanation:
    One possible string t could be "cdef", notice that t can be equal to s.

Constraints:
    1. 1 <= s.length <= 105
    2. s consist only of lowercase English letters.
'''
# === 731ms && 17.5MB === #
class Solution:
    def minAnagramLength(self, s: str) -> int:
        cnt = Counter(s)
        cnt = [cnt[ch] for ch in string.ascii_lowercase]
        
        def is_divisible(cnt, _cnt):
            if any(x != 0 and y == 0 for x, y in zip(cnt, _cnt)):
                return False
            k = -1
            for i in range(26):
                if cnt[i] == 0:
                    continue
                if cnt[i] % _cnt[i] != 0:
                    return False
                if k == -1:
                    k = cnt[i] // _cnt[i]
                else:
                    if cnt[i] // _cnt[i] != k:
                        return False
            return True
        
        stat = [0 for _ in range(26)]
        for i, ch in enumerate(s):
            stat[ord(ch) - ord('a')] += 1
            if is_divisible(cnt, stat):
                return i+1
        return len(s)
            
            
        