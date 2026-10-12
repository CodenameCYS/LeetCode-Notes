'''
=== 4081. Prime Subset Selection II ===

You are given two integers n and s.
Consider all prime numbers less than or equal to n. Select a subset of these primes such that:
    - Each prime can be selected at most once.
    - The sum of the selected primes is as large as possible while remaining less than or equal to s.
    - Among subsets with the maximum sum, select one containing the fewest primes.
    - If multiple subsets remain tied, select the one whose elements, written in increasing order, form the lexicographically smallest array.
Return an integer array containing the selected primes in increasing order. If no valid non-empty subset exists, return an empty array.

Example 1:
    Input: n = 7, s = 20
    Output: [2, 3, 5, 7]
    Explanation:
    The prime numbers less than or equal to n = 7 are 2, 3, 5, and 7.
    The sum of all these primes is 2 + 3 + 5 + 7 = 17, which is less than or equal to s = 20.
    Thus, the answer is [2, 3, 5, 7].
Example 2:
    Input: n = 15, s = 18
    Output: [5,13]
    Explanation:
    The prime numbers less than or equal to 15 are 2, 3, 5, 7, 11, and 13.
    The subsets with sum 18 are [5, 13], [7, 11], [2, 3, 13], and [2, 5, 11]. Since this sum equals s, it is the maximum possible sum.
    Among these subsets, [5, 13] and [7, 11] contain the fewest primes: two.
    Between these two subsets, [5, 13] is lexicographically smaller because its first element, 5, is smaller than 7. Thus, the answer is [5, 13].
Example 3:
    Input: n = 5, s = 1
    Output: []
    Explanation:
    The smallest prime number is 2, which is greater than s = 1.
    Thus, no prime can be selected, so the answer is an empty array.
 
Constraints:
    1. 1 <= n <= 1000
    2. 1 <= s <= 1000
'''
# === 3901ms && 92.03MB === #
def get_primes(n):
    status = [0 for _ in range(n+1)]
    primes = []
    for i in range(2, n+1):
        if status[i] == 1:
            continue
        primes.append(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(1000)

class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        m = len(PRIMES)
        
        @cache
        def dp(idx, remain):
            if idx >= m or PRIMES[idx] > n:
                return 0, []
            if PRIMES[idx] > remain:
                return 0, []
            _s1, _ans1 = dp(idx+1, remain - PRIMES[idx])
            s1, ans1 = PRIMES[idx] + _s1, [PRIMES[idx]] + _ans1
            s2, ans2 = dp(idx+1, remain)
            if s2 > s1:
                return s2, ans2
            elif s1 > s2:
                return s1, ans1
            else:
                return (s2, ans2) if len(ans2) < len(ans1) else (s1, ans1)

        tot, seq = dp(0, s)
        return seq