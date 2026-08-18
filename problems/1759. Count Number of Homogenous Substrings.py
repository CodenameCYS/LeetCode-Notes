'''
=== 1759. Count Number of Homogenous Substrings ===

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
A string is homogenous if all the characters of the string are the same.
A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "abbcccaa"
    Output: 13
    Explanation: The homogenous substrings are listed as below:
    "a"   appears 3 times.
    "aa"  appears 1 time.
    "b"   appears 2 times.
    "bb"  appears 1 time.
    "c"   appears 3 times.
    "cc"  appears 2 times.
    "ccc" appears 1 time.
    3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:
    Input: s = "xy"
    Output: 2
    Explanation: The homogenous substrings are "x" and "y".
Example 3:
    Input: s = "zzzzz"
    Output: 15
 
Constraints:
    1. 1 <= s.length <= 105
    2. s consists of lowercase letters.
'''
# === 212ms && 15.1MB === #
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9+7
        cache = {}
        cnt = 0
        for idx, c in enumerate(s):
            if idx == 0:
                cnt += 1
            else:
                last = s[idx-1]
                if c == last:
                    cnt += 1
                else:
                    if last not in cache:
                        cache[last] = {}
                    if cnt not in cache[last]:
                        cache[last][cnt] = 0
                    cache[last][cnt] += 1
                    cnt = 1
        last = s[-1]
        if last not in cache:
            cache[last] = {}
        if cnt not in cache[last]:
            cache[last][cnt] = 0
        cache[last][cnt] += 1
        # print(cache)
        res = 0
        for item in cache.values():
            for cnt, repeat in item.items():
                res = (res + repeat * cnt * (cnt+1) // 2) % MOD
        return res
