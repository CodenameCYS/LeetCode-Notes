'''
=== 227. Basic Calculator II ===

Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:
    Input: "3+2*2"
    Output: 7
Example 2:
    Input: " 3/2 "
    Output: 1
Example 3:
    Input: " 3+5 / 2 "
    Output: 5

Note:
    1. You may assume that the given expression is always valid.
    2. Do not use the eval built-in library function.
'''
# === 152ms(57.46%) === #
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return int(eval(s))