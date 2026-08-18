'''
=== 1994. The Number of Good Subsets ===

You are given an integer array nums. We call a subset of nums good if its product can be represented as a product of one or more distinct prime numbers.
    - For example, if nums = [1, 2, 3, 4]:
        - [2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, and 3 = 3 respectively.
        - [1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.
Return the number of different good subsets in nums modulo 109 + 7.
A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 6
    Explanation: The good subsets are:
    - [1,2]: product is 2, which is the product of distinct prime 2.
    - [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
    - [1,3]: product is 3, which is the product of distinct prime 3.
    - [2]: product is 2, which is the product of distinct prime 2.
    - [2,3]: product is 6, which is the product of distinct primes 2 and 3.
    - [3]: product is 3, which is the product of distinct prime 3.
Example 2:
    Input: nums = [4,2,3,15]
    Output: 5
    Explanation: The good subsets are:
    - [2]: product is 2, which is the product of distinct prime 2.
    - [2,3]: product is 6, which is the product of distinct primes 2 and 3.
    - [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
    - [3]: product is 3, which is the product of distinct prime 3.
    - [15]: product is 15, which is the product of distinct primes 3 and 5.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 30
'''
# === 2116ms && 66MB === #
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9+7
        
        primes = [2,3,5,7,11,13,17,19,23,29]
        impossible = {4, 8, 12, 16, 20, 24, 28, 9, 18, 27, 25}
        cnt = Counter(nums)
        
        ones = 1
        for i in range(cnt[1]):
            ones = ones * 2 % MOD
        
        status_map = defaultdict(int)
        for i in range(2, 31):
            status = 0
            for p in primes:
                if i % p == 0:
                    status = (status << 1) + 1
                else:
                    status = status << 1
            status_map[i] = status
        
        @lru_cache(None)
        def dp(k, status):
            if k > 30:
                return 1 if status != 0 else 0
            res = dp(k+1, status)
            if k not in impossible and status_map[k] & status == 0:
                res += cnt[k] * dp(k+1, status ^ status_map[k])
            return res % MOD
        
        return (ones * dp(2, 0)) % MOD
        
            
        
            