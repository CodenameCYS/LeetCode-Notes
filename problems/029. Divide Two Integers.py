'''
=== 29. Divide Two Integers ===

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = truncate(-2.33333..) = -2.

Note:
    1. Both dividend and divisor will be 32-bit signed integers.
    2. The divisor will never be 0.
    3. Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''
# === 32ms(69.44%) && 14.1MB(5.36%) === #
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            ans = dividend // divisor
        else:
            ans = - ((-dividend) // divisor)
        return ans if ans < 2**31-1 else 2**31-1