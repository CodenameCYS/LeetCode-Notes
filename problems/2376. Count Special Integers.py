'''
=== 2376. Count Special Integers ===

We call a positive integer special if all of its digits are distinct.
Given a positive integer n, return the number of special integers that belong to the interval [1, n].

Example 1:
    Input: n = 20
    Output: 19
    Explanation: All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers.
Example 2:
    Input: n = 5
    Output: 5
    Explanation: All the integers from 1 to 5 are special.
Example 3:
    Input: n = 135
    Output: 110
    Explanation: There are 110 integers from 1 to 135 that are special.
    Some of the integers that are not special are: 22, 114, and 131.
 
Constraints:
    1. 1 <= n <= 2 * 109
'''
# === 42ms && 13.9MB === #
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
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
                
        return res
