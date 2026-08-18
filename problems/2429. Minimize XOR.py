'''
=== 2429. Minimize XOR ===

Given two positive integers num1 and num2, find the integer x such that:
    - x has the same number of set bits as num2, and
    - The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.
Return the integer x. The test cases are generated such that x is uniquely determined.
The number of set bits of an integer is the number of 1's in its binary representation.

Example 1:
    Input: num1 = 3, num2 = 5
    Output: 3
    Explanation:
    The binary representations of num1 and num2 are 0011 and 0101, respectively.
    The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:
    Input: num1 = 1, num2 = 12
    Output: 3
    Explanation:
    The binary representations of num1 and num2 are 0001 and 1100, respectively.
    The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

Constraints:
    1. 1 <= num1, num2 <= 109
'''
# === 68ms && 13.8MB === #
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        s = bin(num1)[2:].rjust(32, "0")
        cnt = Counter(bin(num2))["1"]
        # print(s, cnt)
        
        digits = [0 for _ in range(32)]
        for i in range(32):
            if s[i] == "1" and cnt > 0:
                digits[i] = 1
                cnt -= 1
        for i in range(31, -1, -1):
            if cnt > 0 and s[i] == "0":
                digits[i] = 1
                cnt -= 1
        # print(digits)
        
        res = 0
        for i in range(32):
            res = res * 2 + digits[i]
        return res
            