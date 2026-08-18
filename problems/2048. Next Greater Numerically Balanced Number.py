'''
=== 2048. Next Greater Numerically Balanced Number ===

An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.
Given an integer n, return the smallest numerically balanced number strictly greater than n.

Example 1:
    Input: n = 1
    Output: 22
    Explanation: 
    22 is numerically balanced since:
    - The digit 2 occurs 2 times. 
    It is also the smallest numerically balanced number strictly greater than 1.
Example 2:
    Input: n = 1000
    Output: 1333
    Explanation: 
    1333 is numerically balanced since:
    - The digit 1 occurs 1 time.
    - The digit 3 occurs 3 times. 
    It is also the smallest numerically balanced number strictly greater than 1000.
    Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:
    Input: n = 3000
    Output: 3133
    Explanation: 
    3133 is numerically balanced since:
    - The digit 1 occurs 1 time.
    - The digit 3 occurs 3 times.
    It is also the smallest numerically balanced number strictly greater than 3000.
 
Constraints:
    1. 0 <= n <= 106
'''
# === 352ms && 14.2MB === #
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def create_beautiful_nums(s):
            res = {int("".join(x)) for x in permutations(s)}
            return list(res)
        
        bnums = []
        for s in ["1", "22", "122", "333", "1333", "4444", "14444", "22333", "55555", "122333", "155555", "224444", "666666", "1224444"]:
            bnums +=  create_beautiful_nums(s)
        
        for x in sorted(bnums):
            if x > n:
                return x
            