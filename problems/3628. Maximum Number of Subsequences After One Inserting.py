'''
=== 3628. Maximum Number of Subsequences After One Inserting ===

You are given a string s consisting of uppercase English letters.
You are allowed to insert at most one uppercase English letter at any position (including the beginning or end) of the string.
Return the maximum number of "LCT" subsequences that can be formed in the resulting string after at most one insertion.
A subsequence is a non-empty string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:
    Input: s = "LMCT"
    Output: 2
    Explanation:
    We can insert a "L" at the beginning of the string s to make "LLMCT", which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].
Example 2:
    Input: s = "LCCT"
    Output: 4
    Explanation:
    We can insert a "L" at the beginning of the string s to make "LLCCT", which has 4 subsequences, at indices [0, 2, 4], [0, 3, 4], [1, 2, 4] and [1, 3, 4].
Example 3:
    Input: s = "L"
    Output: 0
    Explanation:
    Since it is not possible to obtain the subsequence "LCT" by inserting a single letter, the result is 0.

Constraints:
    1. 1 <= s.length <= 105
    2. s consists of uppercase English letters.
'''
# === 687ms && 29.62MB === #
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        cnt_T = [0 if ch != "T" else 1 for ch in s]
        cnt_CT = [0 for _ in s]
        for i in range(n-2, -1, -1):
            cnt_T[i] += cnt_T[i+1]
            if s[i] == "C":
                cnt_CT[i] = cnt_T[i+1] + cnt_CT[i+1]
            else:
                cnt_CT[i] = cnt_CT[i+1]
        cnt_L = [0 if ch != "L" else 1 for ch in s]
        cnt_LC = [0 for _ in s]
        for i in range(1, n):
            cnt_L[i] += cnt_L[i-1]
            if s[i] == "C":
                cnt_LC[i] = cnt_L[i-1] + cnt_LC[i-1]
            else:
                cnt_LC[i] = cnt_LC[i-1]
        ans, inc = 0, 0
        for i in range(n):
            if s[i] == "C":
                ans += cnt_L[i] * cnt_T[i]
            inc = max(inc, cnt_CT[i], cnt_LC[i], cnt_L[i] * cnt_T[i])
        return ans + inc

