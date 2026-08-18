'''
=== 1556. Thousand Separator ===

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Example 1:
    Input: n = 987
    Output: "987"
Example 2:
    Input: n = 1234
    Output: "1.234"
Example 3:
    Input: n = 123456789
    Output: "123.456.789"
Example 4:
    Input: n = 0
    Output: "0"
 
Constraints:
    1. 0 <= n < 2^31
'''
# === 28ms && 13.6MB === #
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = []
        while n != 0:
            ans.insert(0, ("000" + str(n % 1000))[-3:])
            n = n // 1000
        return ".".join(ans).lstrip("0")