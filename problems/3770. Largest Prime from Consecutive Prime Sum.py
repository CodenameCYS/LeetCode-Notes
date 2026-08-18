'''
=== 3770. Largest Prime from Consecutive Prime Sum ===

You are given an integer n.
Return the largest prime number less than or equal to n that can be expressed as the sum of one or more consecutive prime numbers starting from 2. If no such number exists, return 0.

Example 1:
    Input: n = 20
    Output: 17
    Explanation:
    The prime numbers less than or equal to n = 20 which are consecutive prime sums are:
    2 = 2
    5 = 2 + 3
    17 = 2 + 3 + 5 + 7
    The largest is 17, so it is the answer.
Example 2:
    Input: n = 2
    Output: 2
    Explanation:
    The only consecutive prime sum less than or equal to 2 is 2 itself.

Constraints:
    1. 1 <= n <= 5 * 105
'''
def get_primes(n):
    primes = []
    status = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if status[i] == 1:
            continue
        for j in range(i, n+1, i):
            status[j] = 1
        primes.append(i)
    return primes

PRIMES = get_primes(5*(10**5))
SPRIMES = set(PRIMES)
PREFIXS = [x for x in list(accumulate(PRIMES)) if x in SPRIMES]
# === 0ms && 23.43MB === #
class Solution:
    def largestPrime(self, n: int) -> int:
        if n < 2:
            return 0
        idx = bisect.bisect_right(PREFIXS, n)
        return PREFIXS[idx-1]
        