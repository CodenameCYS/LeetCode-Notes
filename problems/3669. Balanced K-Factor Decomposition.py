'''
# === 3669. Balanced K-Factor Decomposition === #

Given two integers n and k, split the number n into exactly k positive integers such that the product of these integers is equal to n.
Return any one split in which the maximum difference between any two numbers is minimized. You may return the result in any order.

Example 1:
    Input: n = 100, k = 2
    Output: [10,10]
    Explanation:
    The split [10, 10] yields 10 * 10 = 100 and a max-min difference of 0, which is minimal.
Example 2:
    Input: n = 44, k = 3
    Output: [2,2,11]
    Explanation:
    Split [1, 1, 44] yields a difference of 43
    Split [1, 2, 22] yields a difference of 21
    Split [1, 4, 11] yields a difference of 10
    Split [2, 2, 11] yields a difference of 9
    Therefore, [2, 2, 11] is the optimal split with the smallest difference 9.

Constraints:
    1. 4 <= n <= 105
    2. 2 <= k <= 5
    3. k is strictly less than the total number of positive divisors of n.
'''
def get_primes(n):
    primes = []
    status = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if status[i] == 1:
            continue
        primes.append(i)
        for j in range(i, n+1, i):
            status[j] = 1
    return primes

PRIMES = get_primes(10**5)
# === 12ms && 18.55MB === #
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        
        def split(n):
            factors = []
            for p in PRIMES:
                if n < p:
                    break
                while n % p == 0:
                    factors.append(p)
                    n = n // p
            return factors

        factors = split(n)
        if len(factors) <= k:
            return [1] * (k-len(factors)) + factors
        # print(factors)

        @lru_cache(None)
        def dfs(arr):
            if len(arr) == k:
                return arr
            ans = []
            e = arr[0]
            for i, num in enumerate(arr):
                if i == 0:
                    continue
                nxt = list(arr[1:i] + arr[i+1:])
                bisect.insort(nxt, e * num)
                candi = dfs(tuple(nxt))
                if ans == [] or candi[-1]-candi[0] < ans[-1]-ans[0]:
                    ans = candi
            return ans

        return dfs(tuple(factors))

            
        
