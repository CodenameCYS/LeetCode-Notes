'''
=== 516. Longest Palindromic Subsequence ===

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
    Input:
    "bbbab"
    Output:
    4
    One possible longest palindromic subsequence is "bbbb".
Example 2:
    Input:
    "cbbd"
    Output:
    2
    One possible longest palindromic subsequence is "bb".
'''
# === 8212ms(5.01%) && 82.6MB(15.38%) === #
class Solution:
    def my_longest_subseq(self, s, st, ed):
        if ed - st < 1:
            return 0
        if ed - st == 1:
            return 1
        if (st, ed) in self.cache.keys():
            return self.cache[(st,ed)]
        s1 = self.my_longest_subseq(s, st+1, ed)
        j = ed
        while st < j and s[j-1] != s[st]:
            j -= 1
        if j == st+1:
            s2 = 1
        else:
            s2 = self.my_longest_subseq(s, st+1, j-1) + 2
        length = s1 if s1 > s2 else s2
        self.cache[(st, ed)] = length
        # print(s[st:ed], " == ", length)
        return length
    
    def longestPalindromeSubseq(self, s: str) -> int:
        self.cache = {}
        return self.my_longest_subseq(s, 0, len(s))