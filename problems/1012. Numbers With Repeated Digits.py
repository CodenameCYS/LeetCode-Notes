'''
=== 1012. Numbers With Repeated Digits ===

Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

Example 1:
    Input: n = 20
    Output: 1
    Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:
    Input: n = 100
    Output: 10
    Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:
    Input: n = 1000
    Output: 262
    
Constraints:
    1. 1 <= n <= 109
'''
# === 59ms && 13.9MB === #
class Solution:    
    def numDupDigitsAtMostN(self, n: int) -> int:
        nums = [int(i) for i in str(n+1)] 
        d = len(nums) 
        res = 0 
        
       
        for i in range(1,d):
            res += 9 * math.perm(9,i-1)
        
		
        for i, x in enumerate(nums):
            if i == 0:
                digit_range = range(1,x) 
            else:
                digit_range = range(x)
                
            for y in digit_range:
                if y not in nums[:i]:
                    res += math.perm(9-i,d-1-i)
            if x in nums[:i]: break
                
        return n-res