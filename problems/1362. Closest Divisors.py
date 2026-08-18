'''
=== 1362. Closest Divisors ===

Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.
Return the two integers in any order.

Example 1:
    Input: num = 8
    Output: [3,3]
    Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
Example 2:
    Input: num = 123
    Output: [5,25]
Example 3:
    Input: num = 999
    Output: [40,25]
 
Constraints:
    1. 1 <= num <= 10^9
'''
# === 192ms && 12.8MB === #
class Solution:
    def find_closest_divisor(self, num):
        import math
        n = int(math.sqrt(num))
        for i in range(n+1,0,-1):
            if num % i == 0:
                return [i, num // i]
        
    def closestDivisors(self, num: int) -> List[int]:
        a1 = self.find_closest_divisor(num+1)
        a2 = self.find_closest_divisor(num+2)
        return a1 if a1[1]-a1[0] < a2[1]-a2[0] else a2
        