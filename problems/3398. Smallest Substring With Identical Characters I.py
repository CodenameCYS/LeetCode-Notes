'''
=== 3398. Smallest Substring With Identical Characters I ===

You are given a binary string s of length n and an integer numOps.
You are allowed to perform the following operation on s at most numOps times:
    - Select any index i (where 0 <= i < n) and flip s[i], i.e., if s[i] == '1', change s[i] to '0' and vice versa.
You need to minimize the length of the longest substring of s such that all the characters in the substring are identical.
Return the minimum length after the operations.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "000001", numOps = 1
    Output: 2
    Explanation: 
    By changing s[2] to '1', s becomes "001001". The longest substrings with identical characters are s[0..1] and s[3..4].
Example 2:
    Input: s = "0000", numOps = 2
    Output: 1
    Explanation: 
    By changing s[0] and s[2] to '1', s becomes "1010".
Example 3:
    Input: s = "0101", numOps = 0
    Output: 1

Constraints:
    1. 1 <= n == s.length <= 1000
    2. s consists only of '0' and '1'.
    3. 0 <= numOps <= n
'''
# === 63ms && 30.8MB === #
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        
        def flip(ch):
            return "1" if ch == "0" else "0"
        
        @lru_cache(None)
        def is_possible(idx, tgt, pre, cnt, ops):
            if idx == n:
                return True
            if ops == 0:
                for j in range(idx, n):
                    if s[j] == pre:
                        cnt += 1
                    else:
                        cnt = 1
                    if cnt > tgt:
                        return False
                    pre = s[j]
                return True
            else:
                if pre == s[idx]:
                    if cnt >= tgt:
                        return is_possible(idx+1, tgt, flip(s[idx]), 1, ops-1)
                    elif cnt == tgt-1:
                        return is_possible(idx+1, tgt, s[idx], cnt+1, ops) or is_possible(idx+1, tgt, flip(s[idx]), 1, ops-1)
                    else:
                        return is_possible(idx+1, tgt, s[idx], cnt+1, ops)
                else:
                    return is_possible(idx+1, tgt, s[idx], 1, ops)
        
        l, r = 0, n
        while r-l > 1:
            m = (l+r) // 2
            if is_possible(0, m, s[0], 0, numOps):
                r = m
            else:
                l = m
        return r
        