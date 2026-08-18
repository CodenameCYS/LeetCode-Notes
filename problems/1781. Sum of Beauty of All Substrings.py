'''
=== 1781. Sum of Beauty of All Substrings ===

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
    - For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

Example 1:
    Input: s = "aabcb"
    Output: 5
    Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:
    Input: s = "aabcbaa"
    Output: 17
 
Constraints:
    1. 1 <= s.length <= 500
    2. s consists of only lowercase English letters.
'''
# === 7260ms && 14.6MB === #
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        cnt = [[0 for _ in range(26)] for _ in range(n+1)]
        for i in range(n):
            for j in range(26):
                cnt[i+1][j] = cnt[i][j]
            cnt[i+1][ord(s[i])-ord('a')] += 1
        
        res = 0
        for i in range(n-1):
            for j in range(i+2, n+1):
                c = [x-y for x, y in zip(cnt[j], cnt[i]) if x - y != 0]
                _max = max(c)
                _min = min(c)
                if _max != _min:
                    res += _max - _min
        return res