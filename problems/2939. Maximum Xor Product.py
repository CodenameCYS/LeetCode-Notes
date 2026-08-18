'''
=== 2939. Maximum Xor Product ===

Given three integers a, b, and n, return the maximum value of (a XOR x) * (b XOR x) where 0 <= x < 2n.
Since the answer may be too large, return it modulo 109 + 7.
Note that XOR is the bitwise XOR operation.

Example 1:
    Input: a = 12, b = 5, n = 4
    Output: 98
    Explanation: For x = 2, (a XOR x) = 14 and (b XOR x) = 7. Hence, (a XOR x) * (b XOR x) = 98. 
    It can be shown that 98 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2n.
Example 2:
    Input: a = 6, b = 7 , n = 5
    Output: 930
    Explanation: For x = 25, (a XOR x) = 31 and (b XOR x) = 30. Hence, (a XOR x) * (b XOR x) = 930.
    It can be shown that 930 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2n.
Example 3:
    Input: a = 1, b = 6, n = 3
    Output: 12
    Explanation: For x = 5, (a XOR x) = 4 and (b XOR x) = 3. Hence, (a XOR x) * (b XOR x) = 12.
    It can be shown that 12 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2n.
 
Constraints:
    1. 0 <= a, b < 250
    2. 0 <= n <= 50
'''
# === 69ms && 16.3MB === #
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        
        def num2digits(num):
            digits = [0 for i in range(50)]
            idx = 0
            while num != 0:
                digits[idx] = num % 2
                num = num // 2
                idx += 1
            return digits
        
        def digits2num(digits):
            flag = 1
            ans = 0
            for d in digits:
                ans += flag * d
                flag = flag * 2 % MOD
            return ans % MOD
        
        def convert(digits_a, digits_b):
            status = 0
            for idx in range(49, -1, -1):
                if idx >= n:
                    if digits_a[idx] > digits_b[idx]:
                        if status == 0:
                            status = 1
                    elif digits_a[idx] < digits_b[idx]:
                        if status == 0:
                            status = 2
                    continue
                if digits_a[idx] == 0 and digits_b[idx] == 0:
                    digits_a[idx] = 1
                    digits_b[idx] = 1
                elif digits_a[idx] == 1 and digits_b[idx] == 1:
                    digits_a[idx] = 1
                    digits_b[idx] = 1
                elif digits_a[idx] == 0 and digits_b[idx] == 1:
                    if status == 0:
                        status = 2
                    elif status == 2:
                        digits_a[idx] = 1
                        digits_b[idx] = 0
                else:
                    if status == 0:
                        status = 1
                    elif status == 1:
                        digits_a[idx] = 0
                        digits_b[idx] = 1
            return
        
        digits_a = num2digits(a)
        digits_b = num2digits(b)
        # int(digits_a, digits_b)
        convert(digits_a, digits_b)
        # int(digits_a, digits_b)
        na = digits2num(digits_a)
        nb = digits2num(digits_b)
        # print(na, nb)
        # print("=" * 10)
        return na * nb % MOD
                        