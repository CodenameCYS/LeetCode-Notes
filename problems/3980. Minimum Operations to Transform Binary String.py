'''
=== 3980. Minimum Operations to Transform Binary String ===

You are given two binary strings s1 and s2 of the same length n.
You can perform the following operations on s1 any number of times, in any order:
    - Choose an index i such that s1[i] == '0', and change it to '1'.
    - Choose an index i such that 0 <= i < n - 1, and both s1[i] and s1[i + 1] are '1'. Change both characters to '0'.
Return the minimum number of operations required to make s1 equal to s2. If it is impossible, return -1.

Example 1:
    Input: s1 = "11", s2 = "00"
    Output: 1
    Explanation:
    Change indices 0 and 1 from '1' to '0' in one operation, so "11" becomes "00". Thus, the answer is 1.
Example 2:
    Input: s1 = "01", s2 = "10"
    Output: 3
    Explanation:
    Change index 0 from '0' to '1', so "01" becomes "11".
    Change indices 0 and 1 from '1' to '0', so "11" becomes "00".
    Change index 0 from '0' to '1', so "00" becomes "10".
    Thus, the answer is 3.
Example 3:
    Input: s1 = "1", s2 = "0"
    Output: -1
    Explanation:
    The first operation cannot change '1' to '0', and the second operation requires two adjacent characters. Therefore, it is impossible.

Constraints:
    - 1 <= n == s1.length == s2.length <= 105
    - s1 and s2 consist only of '0' and '1'.
'''
# === 123ms && 20.28MB === #
class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        n = len(s1)
        if s1 == "1" and s2 == "0":
            return -1
        one2zero, zero2one = 0, 0
        idx, prev = 0, 0
        ans = 0
        while idx < n:
            if s1[idx] == s2[idx]:
                prev = 0
            elif s1[idx] == "0":
                zero2one += 1
                prev = 0
            elif prev == 1:
                one2zero -= 1
                ans += 1
                prev = 0
            else:
                one2zero += 1
                prev = 1
            idx += 1
        return ans + 2*one2zero + zero2one
