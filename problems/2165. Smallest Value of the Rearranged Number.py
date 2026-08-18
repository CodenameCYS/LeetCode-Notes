'''
=== 2165. Smallest Value of the Rearranged Number ===

You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.
Return the rearranged number with minimal value.
Note that the sign of the number does not change after rearranging the digits.

Example 1:
    Input: num = 310
    Output: 103
    Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
    The arrangement with the smallest value that does not contain any leading zeros is 103.
Example 2:
    Input: num = -7605
    Output: -7650
    Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
    The arrangement with the smallest value that does not contain any leading zeros is -7650.
 
Constraints:
    1. -1015 <= num <= 1015
'''
# === 61ms && 13.9MB === #
class Solution:
    def smallestNumber(self, num: int) -> int:
        is_positive = True
        if num == 0:
            return 0
        elif num < 0:
            num = -num
            is_positive = False
            
        digits = []
        while num != 0:
            digits.insert(0, num % 10)
            num = num // 10
        if is_positive:
            digits = sorted(digits)
            idx = 0
            while digits[idx] == 0:
                idx += 1
            digits[idx], digits[0] = digits[0], digits[idx]
        else:
            digits = sorted(digits, reverse=True)
        
        res = 0
        for d in digits:
            res = res*10 + d
        return res if is_positive else -res
        