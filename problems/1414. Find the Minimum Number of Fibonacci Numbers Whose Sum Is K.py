'''
=== 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K ===

Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.
The Fibonacci numbers are defined as:
    1. F1 = 1
    2. F2 = 1
    3. Fn = Fn-1 + Fn-2 , for n > 2.
It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k.
 
Example 1:
    Input: k = 7
    Output: 2 
    Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
    For k = 7 we can use 2 + 5 = 7.
Example 2:
    Input: k = 10
    Output: 2 
    Explanation: For k = 10 we can use 2 + 8 = 10.
Example 3:
    Input: k = 19
    Output: 3 
    Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
 
Constraints:
    1. 1 <= k <= 10^9
'''
# === 52ms && 14MB === #
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [1, 1]
        while f[-1] < k:
            f.append(f[-1] + f[-2])
        ans = 0
        while k != 0:
            num = f.pop()
            if num <= k:
                k -= num
                ans += 1
        return ans
                