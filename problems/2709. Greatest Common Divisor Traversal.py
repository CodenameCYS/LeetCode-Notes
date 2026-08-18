'''
=== 2709. Greatest Common Divisor Traversal ===

You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.
Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.
Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

Example 1:
    Input: nums = [2,3,6]
    Output: true
    Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
    To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
    To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
Example 2:
    Input: nums = [3,9,5]
    Output: false
    Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
Example 3:
    Input: nums = [4,3,12,8]
    Output: true
    Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
'''
# === 3540ms && 128.9MB === #
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        
    def find(self, k):
        if self.root[k] == k:
            return k
        self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
        return
    
class PrimeTable:
    def __init__(self):
        self.primes = self.get_primes()

    def get_primes(self):
        n = 10**5
        status = [0 for _ in range(n+1)]
        res = []
        for i in range(2, n):
            if status[i] == 0:
                res.append(i)
                for j in range(i, n, i):
                    status[j] = 1
        return res
    
    @lru_cache(None)
    def get_factors(self, n):
        if n == 1:
            return []
        for p in self.primes:
            if n % p == 0:
                while n % p == 0:
                    n = n // p
                return [p] + self.get_factors(n)

prime_table = PrimeTable()

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        if any(x == 1 for x in nums):
            return len(nums) == 1
        primes = set()
        for x in nums:
            factors = prime_table.get_factors(x)
            for p in factors:
                primes.add(p)
        # print(primes)
        primes = sorted(primes)
        index = {p: i for i, p in enumerate(primes)}
        m, n = len(primes), len(nums)
        dsu = DSU(n+m)
        for i, x in enumerate(nums):
            for p in prime_table.get_factors(x):
                if x % p == 0:
                    dsu.union(i, n+index[p])
        tgt = dsu.find(0)
        return all(dsu.find(i) == tgt for i in range(n))
        