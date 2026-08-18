'''
=== 1023. Binary String With Substrings Representing 1 To N ===

Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

Example 1:
    Input: S = "0110", N = 3
    Output: true
Example 2:
    Input: S = "0110", N = 4
    Output: false
 
Note:
    1. 1 <= S.length <= 1000
    2. 1 <= N <= 10^9
'''
# === 36ms & 13.3MB === #
class Solution:
    def haveString(self, S: str, N: int) -> bool:
        digits = bin(N)[2:]
        return S.find(digits) != -1
    
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N+1)[1:]:
            if not self.haveString(S, i):
                return False
        return True