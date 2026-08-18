'''
=== 3260. Find the Largest Palindrome Divisible by K ===

You are given two positive integers n and k.
An integer x is called k-palindromic if:
    - x is a palindrome.
    - x is divisible by k.
Return the largest integer having n digits (as a string) that is k-palindromic.
Note that the integer must not have leading zeros.

Example 1:
    Input: n = 3, k = 5
    Output: "595"
    Explanation:
    595 is the largest k-palindromic integer with 3 digits.
Example 2:
    Input: n = 1, k = 4
    Output: "8"
    Explanation:
    4 and 8 are the only k-palindromic integers with 1 digit.
Example 3:
    Input: n = 5, k = 6
    Output: "89898"

Constraints:
    1. 1 <= n <= 105
    2. 1 <= k <= 9
'''
# === 637ms && 53.2MB === #
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        
        def dfs(n, start_with_even):
            if n == 0:
                yield ""
            elif n == 1:
                if start_with_even:
                    for i in range(8, -1, -1):
                        yield str(i)
                else:
                    for i in range(9, -1, -1):
                        yield str(i)
            else:
                m = n // 2
                for num1 in dfs(m, start_with_even):
                    for num2 in dfs(n-m, False):
                        yield num1 + num2
        
        def get_palindromic(n, start_with_even):
            r = n % 2
            m = n // 2
            num_iter = dfs(m, start_with_even)
            for num in num_iter:
                if r == 0:
                    yield (num + num[::-1]).strip("0")
                else:
                    for i in range(9, -1, -1):
                        yield (num + str(i) + num[::-1]).strip("0")
            return ""
                        
        def is_divisible(num, k):
            if k == 1:
                return True
            r = 0
            for d in num:
                r = (r*10 + int(d)) % k
            return r == 0
                        
        if k == 1:
            return "9" * n
        elif k == 2:
            if n <= 2:
                return "8" * n
            else:
                return "8" + "9" * (n-2) + "8"
        elif k == 4:
            if n <= 4:
                return "8" * n
            else:
                return "88" + "9" * (n-4) + "88"
        elif k == 8:
            if n <= 6:
                return "8" * n
            else:
                return "888" + "9" * (n-6) + "888"
        elif k == 5:
            if n <= 2:
                return "5" * n
            else:
                return "5" + "9" * (n-2) + "5"
        
        # print(list(dfs(1, False)))
        palindromic_iter = get_palindromic(n, k % 2 == 0)
        for num in palindromic_iter:
            # print(num)
            if is_divisible(num, k):
                return num
        # print("=" * 10)
        return "-1"
        
                        
            