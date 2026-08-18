'''
=== 902. Numbers At Most N Given Digit Set ===

Given an array of digits, you can write numbers using each digits[i] as many times as we want.  For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.
Return the number of positive integers that can be generated that are less than or equal to a given integer n.

Example 1:
    Input: digits = ["1","3","5","7"], n = 100
    Output: 20
    Explanation: 
    The 20 numbers that can be written are:
    1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:
    Input: digits = ["1","4","9"], n = 1000000000
    Output: 29523
    Explanation: 
    We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
    81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
    2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
    In total, this is 29523 integers that can be written using the digits array.
Example 3:
    Input: digits = ["7"], n = 8
    Output: 1

Constraints:
    1. 1 <= digits.length <= 9
    2. digits[i].length == 1
    3. digits[i] is a digit from '1' to '9'.
    4. All the values in digits are unique.
    5. 1 <= n <= 109
'''
# === 32ms(55.10%) && 14.4MB === #
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def num2digits(n):
            digits = []
            while n != 0:
                digits.insert(0, n % 10)
                n = n // 10
            return digits
        
        n = num2digits(n)
        l = len(n)
        digits = [int(x) for x in digits]
        k = len(digits)
        
        if k == 1:
            ans = (l-1)
        else:
            ans = k * (k**(l-1) - 1) // (k-1)
        
        def dp(idx):
            nonlocal ans
            if idx >= l:
                ans += 1
                return
            ans += len([x for x in digits if x < n[idx]]) * k**(l-idx-1)
            if any(x == n[idx] for x in digits):
                dp(idx+1)
            return
        
        dp(0)
        return ans
        