'''
=== 2457. Minimum Addition to Make Integer Beautiful ===

You are given two positive integers n and target.
An integer is considered beautiful if the sum of its digits is less than or equal to target.
Return the minimum non-negative integer x such that n + x is beautiful. The input will be generated such that it is always possible to make n beautiful.

Example 1:
    Input: n = 16, target = 6
    Output: 4
    Explanation: Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and digit sum becomes 2 + 0 = 2. It can be shown that we can not make n beautiful with adding non-negative integer less than 4.
Example 2:
    Input: n = 467, target = 6
    Output: 33
    Explanation: Initially n is 467 and its digit sum is 4 + 6 + 7 = 17. After adding 33, n becomes 500 and digit sum becomes 5 + 0 + 0 = 5. It can be shown that we can not make n beautiful with adding non-negative integer less than 33.
Example 3:
    Input: n = 1, target = 1
    Output: 0
    Explanation: Initially n is 1 and its digit sum is 1, which is already smaller than or equal to target.
 
Constraints:
    1. 1 <= n <= 1012
    2. 1 <= target <= 150
    3. The input will be generated such that it is always possible to make n beautiful.
'''
# === 45ms && 13.9MB === #
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        digits = []
        while n != 0:
            digits.insert(0, n % 10)
            n = n // 10
        res = 0
        flag = 1
        while sum(digits) > target:
            d = digits.pop()
            if d != 0:
                res += (10 - d) * flag
                r, i = 1, len(digits)-1
                while r != 0 and i >= 0:
                    nr = (digits[i] + r) // 10
                    digits[i] = (digits[i] + r) % 10
                    r = nr
                    i -= 1
                if r != 0:
                    digits.insert(0, r)
            flag *= 10
        return res
        