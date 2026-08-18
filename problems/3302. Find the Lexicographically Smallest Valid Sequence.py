'''
=== 3302. Find the Lexicographically Smallest Valid Sequence ===

You are given two strings word1 and word2.
A string x is called almost equal to y if you can change at most one character in x to make it identical to y.
A sequence of indices seq is called valid if:
    - The indices are sorted in ascending order.
    - Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.
Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.
Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

Example 1:
    Input: word1 = "vbcca", word2 = "abc"
    Output: [0,1,2]
    Explanation:
    The lexicographically smallest valid sequence of indices is [0, 1, 2]:
    Change word1[0] to 'a'.
    word1[1] is already 'b'.
    word1[2] is already 'c'.
Example 2:
    Input: word1 = "bacdc", word2 = "abc"
    Output: [1,2,4]
    Explanation:
    The lexicographically smallest valid sequence of indices is [1, 2, 4]:
    word1[1] is already 'a'.
    Change word1[2] to 'b'.
    word1[4] is already 'c'.
Example 3:
    Input: word1 = "aaaaaa", word2 = "aaabc"
    Output: []
    Explanation:
    There is no valid sequence of indices.
    Example 4:
    Input: word1 = "abc", word2 = "ab"
    Output: [0,1]

Constraints:
    1. 1 <= word2.length < word1.length <= 3 * 105
    2. word1 and word2 consist only of lowercase English letters.
'''
# === 1200ms && 55.7MB === #
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        if m == 1:
            return [0]
        
        # print(f"word1: {word1}, n = {n}")
        # print(f"word2: {word2}, m = {m}")
        prefix = [0 for _ in word1]
        i, j = 0, 0
        while j < m:
            while i < n and word1[i] != word2[j]:
                prefix[i] = j
                i += 1
            if i >= n:
                break
            j += 1
            prefix[i] = j
            i += 1
        while i < n:
            prefix[i] = j
            i += 1
        # print(f"prefix: {prefix}")

        i, j = n-1, m-1
        suffix = [0 for _ in word1]
        while j >= 0:
            while i >= 0 and word1[i] != word2[j]:
                suffix[i] = m-1-j
                i -= 1
            if i < 0:
                break
            j -= 1
            suffix[i] = m-1-j
            i -= 1
        while i >= 0:
            suffix[i] = m-1-j
            i -= 1
        # print(f"suffix: {suffix}")
        
        idx = -1
        if word1[0] != word2[0] and suffix[1] >= m-1:
            idx = 0
        else:
            for i in range(1, n-1):
                if prefix[i-1] + suffix[i+1] >= m-1 and prefix[i] != prefix[i-1]+1:
                    idx = i
                    break
        if idx == -1 and prefix[n-2] >= m-1:
            idx = n-1
        # print(f"idx = {idx}")
        
        if idx == -1:
            return []
        i, j = 0, 0
        ans = []
        while j < m:
            while i < idx and word1[i] != word2[j]:
                i += 1
            if i >= idx:
                break
            ans.append(i)
            j += 1
            i += 1
        if j < m:
            ans.append(i)
            i += 1
            j += 1
        while j < m:
            while i < n and word1[i] != word2[j]:
                i += 1
            if i >= n:
                break
            ans.append(i)
            j += 1
            i += 1
        # print("=" * 10)
        return ans
                