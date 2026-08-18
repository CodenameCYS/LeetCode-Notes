'''
=== 2523. Closest Prime Numbers in Range ===

Given two positive integers left and right, find the two integers num1 and num2 such that:
    - left <= nums1 < nums2 <= right .
    - nums1 and nums2 are both prime numbers.
    - nums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions, return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.
A number greater than 1 is called prime if it is only divisible by 1 and itself.

Example 1:
    Input: left = 10, right = 19
    Output: [11,13]
    Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
    The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
    Since 11 is smaller than 17, we return the first pair.
Example 2:
    Input: left = 4, right = 6
    Output: [-1,-1]
    Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 
Constraints:
    1. 1 <= left <= right <= 106
'''
# === 246ms && 24.8MB === #
class Solution:
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primes = Solution.get_primes()
        
    
    @staticmethod
    @lru_cache(None)
    def get_primes():
        status = [0 for _ in range(1000001)]
        primes = []
        for i in range(2, 1000001):
            if status[i] == 0:
                primes.append(i)
                for j in range(i, 1000001, i):
                    status[j] = 1
        return primes
    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        i = bisect.bisect_left(self.primes, left)
        j = bisect.bisect_right(self.primes, right)
        res, delta = [-1, -1], math.inf
        for k in range(i, j-1):
            if self.primes[k+1] - self.primes[k] < delta:
                res = [self.primes[k], self.primes[k+1]]
                delta = self.primes[k+1] - self.primes[k]
                if delta == 2:
                    break
        return res