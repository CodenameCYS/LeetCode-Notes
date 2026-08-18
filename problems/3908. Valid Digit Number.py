'''
=== 3908. Valid Digit Number ===

You are given an integer n and a digit x.
A number is considered valid if:
    - It contains at least one occurrence of digit x, and
    - It does not start with digit x.
Return true if n is valid, otherwise return false.

Example 1:
    Input: n = 101, x = 0
    Output: true
    Explanation:
    The number contains digit 0 at index 1. It does not start with 0, so it satisfies both conditions. Thus, the answer is true​​​​​​​.
Example 2:
    Input: n = 232, x = 2
    Output: false
    Explanation:
    The number starts with 2, which violates the condition. Thus, the answer is false.
Example 3:
    Input: n = 5, x = 1
    Output: false
    Explanation:
    The number does not contain digit 1. Thus, the answer is false.

Constraints:
    1. 0 <= n <= 105​​​​​​​
    2. 0 <= x <= 9
'''
# === 3ms && 19.32MB === #
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        if n < 10:
            return False
        n, x = str(n), str(x)
        return x in n[1:] and x != n[0]