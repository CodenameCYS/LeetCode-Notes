'''
=== 728. Self Dividing Numbers ===

A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
    Input: 
    left = 1, right = 22
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
    1. The boundaries of each input argument are 1 <= left <= right <= 10000.
'''
# === 44ms(76.72%) && 13MB(96%) === #
class Solution:
    def is_self_dividing(self, num):
        n = num
        while n != 0:
            r = n % 10
            n = n // 10
            if r == 0 or num % r != 0:
                return False
        return True
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right+1) if self.is_self_dividing(i)]