'''
=== 3298. Count Substrings That Can Be Rearranged to Contain a String II ===

You are given two strings word1 and word2.
A string x is called valid if x can be rearranged to have word2 as a prefix.
Return the total number of valid substrings of word1.
Note that the memory limits in this problem are smaller than usual, so you must implement a solution with a linear runtime complexity.

Example 1:
    Input: word1 = "bcca", word2 = "abc"
    Output: 1
    Explanation:
    The only valid substring is "bcca" which can be rearranged to "abcc" having "abc" as a prefix.
Example 2:
    Input: word1 = "abcabc", word2 = "abc"
    Output: 10
    Explanation:
    All the substrings except substrings of size 1 and size 2 are valid.
Example 3:
    Input: word1 = "abcabc", word2 = "aaabc"
    Output: 0

Constraints:
    1. 1 <= word1.length <= 106
    2. 1 <= word2.length <= 104
    3. word1 and word2 consist only of lowercase English letters.
'''
# === 11046ms && 26.3MB === #
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        a = ord('a')
        i, j, n = 0, 0, len(word1)
        cnt2 = [0 for _  in range(26)]
        for ch in word2:
            cnt2[ord(ch) - a] += 1
        valids = [i for i in range(26) if cnt2[i] > 0]
        cnt = [0 for _ in range(26)]
        ans = 0
        while i < n:
            while j < n and any(cnt[i] < cnt2[i] for i in valids):
                cnt[ord(word1[j]) - a] += 1
                j += 1
            if j < n:
                ans += n-j+1
                cnt[ord(word1[i]) - a] -= 1
                i += 1
            else:
                break
        if all(cnt[i] >= cnt2[i] for i in valids):
            while i < n and cnt[ord(word1[i]) - a] >= cnt2[ord(word1[i]) - a]:
                ans += n-j+1
                cnt[ord(word1[i]) - a] -= 1
                if cnt[ord(word1[i]) - a] < cnt2[ord(word1[i]) - a]:
                    break
                i += 1
        return ans
            
        