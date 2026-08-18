'''
=== 1363. Largest Multiple of Three ===

Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.
Since the answer may not fit in an integer data type, return the answer as a string.
If there is no answer return an empty string.

Example 1:
    Input: digits = [8,1,9]
    Output: "981"
Example 2:
    Input: digits = [8,6,7,1,0]
    Output: "8760"
Example 3:
    Input: digits = [1]
    Output: ""
Example 4:
    Input: digits = [0,0,0,0,0,0]
    Output: "0"
 
Constraints:
    1. 1 <= digits.length <= 10^4
    2. 0 <= digits[i] <= 9
    3. The returning answer must not contain unnecessary leading zeros.
'''
# === 112ms && 13.6MB === #
class Solution:
    def select_digits(self, d0, d1, d2):
        n1 = len(d1); n2 = len(d2)
        if n1 % 3 - n2 % 3 == 1:
            d1.pop()
        elif n2 % 3 - n1 % 3 == 1:
            d2.pop()
        elif n1 % 3 == 2 and n2 % 3 == 0:
            if n2 == 0:
                d1.pop(); d1.pop()
            else:
                d2.pop()
        elif n1 % 3 == 0 and n2 % 3 == 2:
            if n1 == 0:
                d2.pop(); d2.pop()
            else:
                d1.pop()
        return sorted(d0 + d1 + d2, reverse=True)
        
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        remain = [[],[],[]]
        [remain[it % 3].append(it) for it in digits]
        [it.sort(reverse=True) for it in remain]
        # print(remain)
        digits = self.select_digits(remain[0], remain[1], remain[2])
        # print(digits)
        ans = "".join([str(it) for it in digits])
        if ans != "" and ans[0] == "0":
            ans = ans.lstrip("0")
            if ans == "":
                ans = "0"
        return ans
        