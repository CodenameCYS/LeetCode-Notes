'''
=== 2384. Largest Palindromic Number ===

You are given a string num consisting of digits only.
Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:
    - You do not need to use all the digits of num, but you must use at least one digit.
    - The digits can be reordered.
 
Example 1:
    Input: num = "444947137"
    Output: "7449447"
    Explanation: 
    Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
    It can be shown that "7449447" is the largest palindromic integer that can be formed.
Example 2:
    Input: num = "00009"
    Output: "9"
    Explanation: 
    It can be shown that "9" is the largest palindromic integer that can be formed.
    Note that the integer returned should not contain leading zeroes.
 
Constraints:
    1. 1 <= num.length <= 105
    2. num consists of digits.
'''
# === 109ms && 15.3MB === #
class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = Counter(num)
        s = [0 for _ in range(10)]
        unique = ""
        for i in range(10):
            s[i] = cnt[str(i)] // 2
            if cnt[str(i)] % 2 == 1:
                unique = str(i)
        res = ""
        for i in range(10):
            if s[i] != 0:
                res += str(i) * s[i]
        if res.strip("0") != "":
            res = res[::-1] + unique + res
        elif unique != "":
            res = unique
        else:
            res = "0"
        return res
        