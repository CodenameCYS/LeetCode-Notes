'''
=== 4073. Count Good Strings ===

You are given an integer n.
A string is considered good if it consists only of the characters 'a' and 'b', and one of the following holds:
    - It contains exactly one distinct character, and its length is odd.
    - It can be written as s = s1 + s2, where s1 and s2 are non-empty good strings, and the last character of s1 is different from the first character of s2.
Return the number of good strings of length n, modulo 109 + 7.
Here, + denotes string concatenation.

Example 1:
    Input: n = 4
    Output: 6
    Explanation:
    The good strings are "aaab", "abbb", "baaa", "bbba", "abab", and "baba".
    For example, "aaab" = "aaa" + "b". Both parts are good because each contains one distinct character and has odd length, and their characters at the boundary are different.
    Also, "ab" = "a" + "b" is good, so "abab" = "ab" + "ab" is good because the boundary characters are different.
    Thus, the answer is 6.
Example 2:
    Input: n = 3
    Output: 4
    Explanation:
    The good strings are "aaa", "bbb", "aba", and "bab". Thus, the answer is 4.
Example 3:
    Input: n = 2
    Output: 2
    Explanation:
    The good strings are "ab" and "ba". Thus, the answer is 2.

Constraints:
    1. 1 <= n <= 1015
'''
# === 63ms && 19.32MB === #
MOD = 1_000_000_007

# a @ b，其中 @ 是矩阵乘法
# 更快的写法见另一份代码【NumPy】
def mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
            for row in a]

# a^n @ f
def pow_mul(a: list[list[int]], n: int, f: list[list[int]]) -> list[list[int]]:
    res = f
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res

class Solution:
    def countGoodStrings(self, n: int) -> int:
        m = [[1, 1], [1, 0]]
        f1 = [[2], [0]]  # 这里初始化成 2，就不用把答案乘以 2 了
        fn = pow_mul(m, n - 1, f1)
        return fn[0][0]