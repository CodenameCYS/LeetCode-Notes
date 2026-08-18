'''
=== 2131. Longest Palindrome by Concatenating Two Letter Words ===

You are given an array of strings words. Each element of words consists of two lowercase English letters.
Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
A palindrome is a string that reads the same forward and backward.

Example 1:
    Input: words = ["lc","cl","gg"]
    Output: 6
    Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
    Note that "clgglc" is another longest palindrome that can be created.
Example 2:
    Input: words = ["ab","ty","yt","lc","cl","ab"]
    Output: 8
    Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
    Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:
    Input: words = ["cc","ll","xx"]
    Output: 2
    Explanation: One longest palindrome is "cc", of length 2.
    Note that "ll" is another longest palindrome that can be created, and so is "xx".
 
Constraints:
    1. 1 <= words.length <= 105
    2. words[i].length == 2
    3. words[i] consists of lowercase English letters.
'''
# === 1464ms && 38.6MB === #
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        res = 0
        mid = False
        for w in cnt.keys():
            if w == w[::-1]:
                k = cnt[w]
                res += 4*(k//2)
                if k % 2 == 1:
                    mid = True
            else:
                k = min(cnt[w], cnt[w[::-1]])
                res += 4 * k
                cnt[w] -= k
                if w[::-1] in cnt.keys():
                    cnt[w[::-1]] -= k
        return res+2 if mid else res