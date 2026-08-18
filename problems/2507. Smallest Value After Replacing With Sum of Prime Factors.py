'''
=== 2507. Smallest Value After Replacing With Sum of Prime Factors ===

You are given a positive integer n.
Continuously replace n with the sum of its prime factors.
    - Note that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.
Return the smallest value n will take on.

Example 1:
    Input: n = 15
    Output: 5
    Explanation: Initially, n = 15.
    15 = 3 * 5, so replace n with 3 + 5 = 8.
    8 = 2 * 2 * 2, so replace n with 2 + 2 + 2 = 6.
    6 = 2 * 3, so replace n with 2 + 3 = 5.
    5 is the smallest value n will take on.
Example 2:
    Input: n = 3
    Output: 3
    Explanation: Initially, n = 3.
    3 is the smallest value n will take on.
    
Constraints:
    1. 2 <= n <= 105
'''
# === 4153ms && 93.9MB === #
class Solution:
    @lru_cache(None)
    def get_primes(self):
        s = [0 for _ in range(10**5+1)]
        res = []
        for i in range(2, 10**5+1):
            if s[i] != 0:
                continue
            res.append(i)
            for j in range(i, 10**5+1, i):
                s[j] = 1
        return res
        
    def smallestValue(self, n: int) -> int:
        # print(n)
        primes = self.get_primes()
        # print(primes)
        m = n
        if n in primes:
            return n
        res = 0
        for p in primes:
            if p > n:
                break
            while n % p == 0:
                n = n // p
                res += p
        return self.smallestValue(res) if res < m else res
        
        