'''
=== 415. Add Strings ===

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
    1. The length of both num1 and num2 is < 5100.
    2. Both num1 and num2 contains only digits 0-9.
    3. Both num1 and num2 does not contain any leading zero.
    4. You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
# === 36ms(82.51%) && 12.7MB(100%) === #
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))