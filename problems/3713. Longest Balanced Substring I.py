'''
=== 3713. Longest Balanced Substring I ===

You are given a string s consisting of lowercase English letters.
A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
Return the length of the longest balanced substring of s.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "abbac"
    Output: 4
    Explanation:
    The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.
Example 2:
    Input: s = "zzabccy"
    Output: 4
    Explanation:
    The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​
Example 3:
    Input: s = "aba"
    Output: 2
    Explanation:
    ​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

Constraints:
    1. 1 <= s.length <= 1000
    2. s consists of lowercase English letters.
'''
# ===  === #
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        tot = Counter(s)
        
        def is_balanced(cnt):
            freq = max(cnt.values())
            return all(x == 0 or x == freq for x in cnt.values())

        ans = 1
        for i in range(n-1):
            if n-i <= ans:
                break
            cnt = deepcopy(tot)
            for j in range(n-1, i, -1):
                if j-i+1 <= ans:
                    break
                if is_balanced(cnt):
                    ans = j-i+1
                    break
                cnt[s[j]] -= 1
            tot[s[i]] -= 1
        return ans