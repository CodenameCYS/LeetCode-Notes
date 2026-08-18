'''
=== 3918. Sum of Primes Between Number and Its Reverse ===

You are given an integer n.
Let r be the integer formed by reversing the digits of n.
Return the sum of all prime numbers between min(n, r) and max(n, r), inclusive.

Example 1:
    Input: n = 13
    Output: 132
    Explanation:
    The reverse of 13 is 31. Thus, the range is [13, 31].
    The prime numbers in this range are 13, 17, 19, 23, 29, and 31.
    The sum of these prime numbers is 13 + 17 + 19 + 23 + 29 + 31 = 132.
Example 2:
    Input: n = 10
    Output: 17
    Explanation:
    The reverse of 10 is 1. Thus, the range is [1, 10].
    The prime numbers in this range are 2, 3, 5, and 7.
    The sum of these prime numbers is 2 + 3 + 5 + 7 = 17.
Example 3:
    Input: n = 8
    Output: 0
    Explanation:
    The reverse of 8 is 8. Thus, the range is [8, 8].
    There are no prime numbers in this range, so the sum is 0.
 
Constraints:
    1. 1 <= n <= 1000
'''
# === 0ms && 19.43MB === #
def get_primes(n):
    status = [0 for _ in range(n+1)]
    primes = []
    for i in range(2, n+1):
        if status[i] != 0:
            continue
        primes.append(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(1000)
SUMS = list(accumulate(PRIMES, initial=0))

class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        
        def rev(n):
            r = 0
            while n != 0:
                r = r * 10 + n % 10
                n = n // 10
            return r
        
        r = rev(n)
        i, j = min(n, r), max(n, r)
        ii, jj = bisect.bisect_left(PRIMES, i), bisect.bisect_right(PRIMES, j)
        return SUMS[jj] - SUMS[ii]
