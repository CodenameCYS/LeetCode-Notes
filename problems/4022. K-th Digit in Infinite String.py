'''
=== 4022. K-th Digit in Infinite String ===

You are given an integer k.
An infinite string is formed by concatenating the decimal representations of the positive integers, without separators.
For every nonnegative integer b, block b contains the positive integers from 10 * b through 10 * b + 9. The integers in each block are appended as follows:
    - If b is even, append the integers in increasing order.
    - If b is odd, append the integers in decreasing order.
Therefore, the string starts with the integers 1 through 9, followed by 19 through 10, then 20 through 29, then 39 through 30, and so on.
Return the kth digit (1-indexed) of this string.

Example 1:
    Input: k = 4
    Output: 4
    Explanation:
    The string begins as "123456789..". The 4th digit is '4'.
Example 2:
    Input: k = 15
    Output: 7
    Explanation:
    The string begins as "123456789191817..". The 15th digit is '7'.
Example 3:
    Input: k = 11
    Output: 9
    Explanation:
    The string begins as "12345678919..". The 11th digit is '9'.

Constraints:
    1. 1 <= k <= 1015
'''
# === 0ms && 19.46MB === #
class Solution:
    def kthDigit(self, k: int) -> int:
        base, bn, bl, l = 0, 9, 1, 0
        while l + bn*bl < k:
            l += bn*bl
            bn *= 10
            bl += 1
            base = 10 * base + 9
        n, r = (k-l) // bl, (k-l) % bl
        m = base + n if r == 0 else base + n+1
        # print(n, r, m)
        if (m // 10) % 2 == 0:
            return int(str(m)[r-1]) if r > 0 else int(str(m)[-1])
        else:
            m = 2*(m//10)*10+10-m-1
            return int(str(m)[r-1]) if r > 0 else int(str(m)[-1])