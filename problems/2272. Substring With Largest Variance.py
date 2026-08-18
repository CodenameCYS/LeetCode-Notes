'''
=== 2272. Substring With Largest Variance ===

The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.
Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.
A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "aababbb"
    Output: 3
    Explanation:
    All possible variances along with their respective substrings are listed below:
    - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
    - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
    - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
    - Variance 3 for substring "babbb".
    Since the largest possible variance is 3, we return it.
Example 2:
    Input: s = "abcde"
    Output: 0
    Explanation:
    No letter occurs more than once in s, so the variance of every substring is 0.
 
Constraints:
    1. 1 <= s.length <= 104
    2. s consists of lowercase English letters.
'''
# === 2809ms && 13.9MB === #
class Solution:
    def largestVariance(self, s: str) -> int:
        chars = list(set(s))
        
        res = 0
        for ch1 in chars:
            for ch2 in chars:
                if ch1 == ch2:
                    continue
                
                cnt = 0
                has_another = False
                _min, last_min = 0, math.inf
                for ch in s:
                    if ch == ch1:
                        cnt += 1
                        res = max(res, cnt - _min) if has_another else max(res, cnt - last_min)
                    if ch == ch2:
                        cnt -= 1
                        if cnt >= _min:
                            has_another = True
                            last_min = _min
                        else:
                            last_min = min(last_min, _min)
                            _min = cnt
                            has_another = False
                        res = max(res, cnt - _min) if has_another else max(res, cnt - last_min)
        return res
                            
                        