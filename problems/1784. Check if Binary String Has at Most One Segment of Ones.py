'''
=== 1784. Check if Binary String Has at Most One Segment of Ones ===

Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

Example 1:
    Input: s = "1001"
    Output: false
    Explanation: The ones do not form a contiguous segment.
Example 2:
    Input: s = "110"
    Output: true
 
Constraints:
    1. 1 <= s.length <= 100
    2. s[i]​​​​ is either '0' or '1'.
    3. s[0] is '1'.
'''
# === 28ms && 14.3MB === #
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        res = 0
        n = len(s)
        cnt = 0
        for c in s:
            if c == '0':
                if cnt > 0:
                    res += 1
                cnt = 0
            else:
                cnt += 1
        if cnt > 0:
            res += 1
        return res <= 1