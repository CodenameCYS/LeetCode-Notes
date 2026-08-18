'''
=== 522. Longest Uncommon Subsequence II ===

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.
A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
    Input: "aba", "cdc", "eae"
    Output: 3

Note:
    1. All the given strings' lengths will not exceed 10.
    2. The length of the given list will be in the range of [2, 50].
'''
# === 28ms(89.34%) && 12.8MB(100%) === #
class Solution:
    def find(self, s1, s2):
        i=0; j=0; l1=len(s1); l2=len(s2)
        while i<l1 and j<l2:
            if s1[i] == s2[j]:
                j += 1
            i += 1
        return j == l2
    
    def findLUSlength(self, strs: List[str]) -> int:
        counter = {}
        for s in strs:
            counter[s] = 1 if s not in counter.keys() else counter[s] + 1
        counter = sorted(counter.items(), key = lambda x: len(x[0]), reverse=True)
        illegal = []
        for k, v in counter:
            if v >= 2:
                illegal.append(k)
            else:
                is_legal = True
                for s in illegal:
                    if self.find(s,k):
                        is_legal = False
                        break
                if is_legal:
                    return len(k)
        return -1