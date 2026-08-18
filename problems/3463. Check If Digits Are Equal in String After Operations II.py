'''
=== 3463. Check If Digits Are Equal in String After Operations II ===

You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:
    - For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
    - Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
Return true if the final two digits in s are the same; otherwise, return false.

Example 1:
    Input: s = "3902"
    Output: true
    Explanation:
    Initially, s = "3902"
    First operation:
    (s[0] + s[1]) % 10 = (3 + 9) % 10 = 2
    (s[1] + s[2]) % 10 = (9 + 0) % 10 = 9
    (s[2] + s[3]) % 10 = (0 + 2) % 10 = 2
    s becomes "292"
    Second operation:
    (s[0] + s[1]) % 10 = (2 + 9) % 10 = 1
    (s[1] + s[2]) % 10 = (9 + 2) % 10 = 1
    s becomes "11"
    Since the digits in "11" are the same, the output is true.
Example 2:
    Input: s = "34789"
    Output: false
    Explanation:
    Initially, s = "34789".
    After the first operation, s = "7157".
    After the second operation, s = "862".
    After the third operation, s = "48".
    Since '4' != '8', the output is false.

Constraints:
    1. 3 <= s.length <= 105
    2. s consists of only digits.
'''
def comb_mod2(n, k):
    """ 计算 C(n, k) mod 2 """
    if k < 0 or k > n:
        return 0
    # 检查k的二进制位是否均为n对应位的子集
    return 0 if (k & ~n) else 1

# 预计算C(ni, ki) mod5的值（ni和ki为0-4）
mod5_comb_table = [
    [1, 0, 0, 0, 0],  # n=0
    [1, 1, 0, 0, 0],  # n=1
    [1, 2, 1, 0, 0],  # n=2
    [1, 3, 3, 1, 0],  # n=3
    [1, 4, 1, 4, 1],  # n=4（C(4,2)=6 mod5=1，C(4,3)=4 mod5=4）
]

def comb_mod5(n, k):
    """ 计算 C(n, k) mod 5 """
    result = 1
    while n > 0 or k > 0:
        ni = n % 5
        ki = k % 5
        if ki > ni:
            return 0
        # 查预计算表获取C(ni, ki) mod5
        result = (result * mod5_comb_table[ni][ki]) % 5
        n = n // 5
        k = k // 5
    return result

# 中国剩余定理映射表（a mod2，b mod5）→ 结果 mod10
crt_map = {
    (0, 0): 0,
    (0, 1): 6,
    (0, 2): 2,
    (0, 3): 8,
    (0, 4): 4,
    (1, 0): 5,
    (1, 1): 1,
    (1, 2): 7,
    (1, 3): 3,
    (1, 4): 9,
}

def get_element_mod10(i, j):
    """ 计算杨辉三角第i行第j个元素的个位数（索引从0开始） """
    if j < 0 or j > i:
        return 0
    a = comb_mod2(i, j)   # 计算模2
    b = comb_mod5(i, j)   # 计算模5
    return crt_map[(a, b)]

# === 1443ms && 19.2MB === #
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        weights = [get_element_mod10(n-2, i) for i in range(n-1)]
        # print(weights)
        
        def fn(s):
            ans = 0
            n = len(s)
            for i, ch in enumerate(s):
                digit = int(ch)
                ans = (ans + weights[i] * digit) % 10
            return ans
        
        return fn(s[:-1]) == fn(s[1:])