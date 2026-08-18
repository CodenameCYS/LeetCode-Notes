'''
=== 2719. Count of Integers ===

You are given two numeric strings num1 and num2 and two integers max_sum and min_sum. We denote an integer x to be good if:
    - num1 <= x <= num2
    - min_sum <= digit_sum(x) <= max_sum.
Return the number of good integers. Since the answer may be large, return it modulo 109 + 7.
Note that digit_sum(x) denotes the sum of the digits of x.

Example 1:
    Input: num1 = "1", num2 = "12", min_num = 1, max_num = 8
    Output: 11
    Explanation: There are 11 integers whose sum of digits lies between 1 and 8 are 1,2,3,4,5,6,7,8,10,11, and 12. Thus, we return 11.
Example 2:
    Input: num1 = "1", num2 = "5", min_num = 1, max_num = 5
    Output: 5
    Explanation: The 5 integers whose sum of digits lies between 1 and 5 are 1,2,3,4, and 5. Thus, we return 5.
 
Constraints:
    1. 1 <= num1 <= num2 <= 1022
    2. 1 <= min_sum <= max_sum <= 400
'''
# === 1042ms && 44MB === #
class Solution:
    @lru_cache(None)
    def dp(self, num, _sum):
        MOD = 10**9+7
        
        @lru_cache(None)
        def fn(n, s):
            if s < 0:
                # print(f"fn({n}, {s}) = 0")
                return 0
            elif s == 0 or n == 0:
                # print(f"fn({n}, {s}) = 1")
                return 1
            res = sum(fn(n-1, s-i) for i in range(10))
            # print(f"fn({n}, {s}) = {res}")
            return res % MOD
            
        n = len(num)
        if _sum < 0 or n == 0:
            # print(f"dp({num}, {_sum}) = 0")
            return 0
        elif _sum == 0:
            # print(f"dp({num}, {_sum}) = 1")
            return 1
        elif n == 1:
            res = min(10, min(int(num), _sum)+1)
            # print(f"dp({num}, {_sum}) = {res}")
            return res
        d = int(num[0])
        res = self.dp(num[1:], _sum-d)
        for j in range(d):
            res += fn(n-1, _sum-j)
                
        # print(f"dp({num}, {_sum}) = {res}")
        return res % MOD
    
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9+7
        num1 = str(int(num1) - 1)
        # print(num2, max_sum, self.dp(num2, max_sum))
        # print("=" * 5)
        # print(num2, min_sum-1, self.dp(num2, min_sum-1))
        # print("=" * 5)
        # print(num1, max_sum, self.dp(num1, max_sum))
        # print("=" * 5)
        # print(num1, min_sum-1, self.dp(num1, min_sum-1))
        # print("=" * 10)
        s1 = self.dp(num2, max_sum) - self.dp(num2, min_sum-1)
        s2 = self.dp(num1, max_sum) - self.dp(num1, min_sum-1)
        return (s1 - s2 + MOD) % MOD

# === 345ms && 35.9MB === #
class Solution:
    MOD = 10**9 + 7
    
    @lru_cache(None)
    def fn(self, n, s):
        '''
        number of x, satisfying:
        1. len(digit for digit in x) <= n
        2. sum(digit for digit in x) <= s
        '''
        if s < 0:
            return 0
        elif s == 0 or n == 0:
            return 1
        res = sum(self.fn(n-1, s-i) for i in range(10))
        return res % self.MOD
        
    @lru_cache(None)
    def gn(self, num, s):
        '''
        number of x, satisfying:
        1. x <= num
        2. sum(digit for digit in x) <= s
        '''
        n = len(num)
        if s < 0:
            return 0
        elif s == 0:
            return 1
        elif n == 1:
            res = min(10, min(int(num), s)+1)
            return res
        d = int(num[0])
        res = self.gn(num[1:], s-d)
        for j in range(d):
            res += self.fn(n-1, s-j)
        return res % self.MOD
    
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        num1 = str(int(num1) - 1)
        s1 = self.gn(num2, max_sum) - self.gn(num2, min_sum-1)
        s2 = self.gn(num1, max_sum) - self.gn(num1, min_sum-1)
        return (s1 - s2 + self.MOD) % self.MOD