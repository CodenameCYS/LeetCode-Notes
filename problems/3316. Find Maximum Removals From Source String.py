'''
=== 3316. Find Maximum Removals From Source String ===

You are given a string source of size n, a string pattern that is a subsequence of source, and a sorted integer array targetIndices that contains distinct numbers in the range [0, n - 1].
We define an operation as removing a character at an index idx from source such that:
    - idx is an element of targetIndices.
    - pattern remains a subsequence of source after removing the character.
Performing an operation does not change the indices of the other characters in source. For example, if you remove 'c' from "acb", the character at index 2 would still be 'b'.
Return the maximum number of operations that can be performed.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:
    Input: source = "abbaa", pattern = "aba", targetIndices = [0,1,2]
    Output: 1
    Explanation:
    We can't remove source[0] but we can do either of these two operations:
    Remove source[1], so that source becomes "a_baa".
    Remove source[2], so that source becomes "ab_aa".
Example 2:
    Input: source = "bcda", pattern = "d", targetIndices = [0,3]
    Output: 2
    Explanation:
    We can remove source[0] and source[3] in two operations.
Example 3:
    Input: source = "dda", pattern = "dda", targetIndices = [0,1,2]
    Output: 0
    Explanation:
    We can't remove any character from source.
Example 4:
    Input: source = "yeyeykyded", pattern = "yeyyd", targetIndices = [0,2,3,4]
    Output: 2
    Explanation:
    We can remove source[2] and source[3] in two operations.

Constraints:
    1. 1 <= n == source.length <= 3 * 103
    2. 1 <= pattern.length <= n
    3. 1 <= targetIndices.length <= n
    4. targetIndices is sorted in ascending order.
    5. The input is generated such that targetIndices contains distinct elements in the range [0, n - 1].
    6. source and pattern consist only of lowercase English letters.
    7. The input is generated such that pattern appears as a subsequence in source.
'''
# === 2217ms && 725MB === #
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n, m = len(source), len(pattern)
        targets = set(targetIndices)

        @lru_cache(None)
        def dp(i, j):
            if j >= m:
                return len([idx for idx in range(i, n) if idx in targets])
            if i >= n:
                return -math.inf
            if i in targets:
                if source[i] == pattern[j]:
                    return max(dp(i+1, j+1), 1 + dp(i+1, j))
                else:
                    return 1 + dp(i+1, j)
            else:
                if source[i] == pattern[j]:
                    return dp(i+1, j+1)
                else:
                    return dp(i+1, j)
                
        remove = dp(0, 0)
        return remove if remove != -math.inf else 0
