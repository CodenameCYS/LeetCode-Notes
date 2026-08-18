'''
=== 3821. Find Nth Smallest Integer With K One Bits ===

You are given two positive integers n and k.
Return an integer denoting the nth smallest positive integer that has exactly k ones in its binary representation. It is guaranteed that the answer is strictly less than 250.

Example 1:
    Input: n = 4, k = 2
    Output: 9
    Explanation:
    The 4 smallest positive integers that have exactly k = 2 ones in their binary representations are:
    3 = 112
    5 = 1012
    6 = 1102
    9 = 10012
Example 2:
    Input: n = 3, k = 1
    Output: 4
    Explanation:
    The 3 smallest positive integers that have exactly k = 1 one in their binary representations are:
    1 = 12
    2 = 102
    4 = 1002
 
Constraints:
    1. 1 <= n <= 250
    2. 1 <= k <= 50
    3. The answer is strictly less than 250.
'''
# === 3ms && 19.52MB === #
class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        ans = 0
        for i in range(49, -1, -1):
            c = comb(i, k)  # 第 i 位填 0 的方案数
            if n > c:  # n 比较大，第 i 位必须填 1
                n -= c
                ans |= 1 << i
                k -= 1  # 维护剩余的 1 的个数
                if k == 0:  # 填完了 1，ans 剩余低位都是 0
                    return ans