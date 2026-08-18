'''
=== 3233. Find the Count of Numbers Which Are Not Special ===

You are given 2 positive integers l and r. For any number x, all positive divisors of x except x are called the proper divisors of x.
A number is called special if it has exactly 2 proper divisors. For example:
    - The number 4 is special because it has proper divisors 1 and 2.
    - The number 6 is not special because it has proper divisors 1, 2, and 3.
Return the count of numbers in the range [l, r] that are not special.

Example 1:
    Input: l = 5, r = 7
    Output: 3
    Explanation:
    There are no special numbers in the range [5, 7].
Example 2:
    Input: l = 4, r = 16
    Output: 11
    Explanation:
    The special numbers in the range [4, 16] are 4 and 9.

Constraints:
    1. 1 <= l <= r <= 109
'''
# === 45ms && 17.3MB === #
def get_primes_power():
    n = 10**5+1
    status = [0 for _ in range(n)]
    ans = []
    for i in range(2, n):
        if status[i] == 1:
            continue
        ans.append(i*i)
        for j in range(i, n, i):
            status[j] = 1
    return ans

PRIMES2 = get_primes_power()

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def get_count(num):
            idx = bisect.bisect_right(PRIMES2, num)
            return idx
        
        return r-l+1-(get_count(r) - get_count(l-1))