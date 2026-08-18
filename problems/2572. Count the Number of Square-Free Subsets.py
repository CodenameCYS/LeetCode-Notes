'''
=== 2572. Count the Number of Square-Free Subsets ===

You are given a positive integer 0-indexed array nums.
A subset of the array nums is square-free if the product of its elements is a square-free integer.
A square-free integer is an integer that is divisible by no square number other than 1.
Return the number of square-free non-empty subsets of the array nums. Since the answer may be too large, return it modulo 109 + 7.
A non-empty subset of nums is an array that can be obtained by deleting some (possibly none but not all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Example 1:
    Input: nums = [3,4,4,5]
    Output: 3
    Explanation: There are 3 square-free subsets in this example:
    - The subset consisting of the 0th element [3]. The product of its elements is 3, which is a square-free integer.
    - The subset consisting of the 3rd element [5]. The product of its elements is 5, which is a square-free integer.
    - The subset consisting of 0th and 3rd elements [3,5]. The product of its elements is 15, which is a square-free integer.
    It can be proven that there are no more than 3 square-free subsets in the given array.
Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: There is 1 square-free subset in this example:
    - The subset consisting of the 0th element [1]. The product of its elements is 1, which is a square-free integer.
    It can be proven that there is no more than 1 square-free subset in the given array.
 
Constraints:
    1. 1 <= nums.length <= 1000
    2. 1 <= nums[i] <= 30
'''
# === 133ms && 19.2MB === #
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
            
        primes = [2,3,5,7,11,13,17,19,23,29]
        cnt = Counter(nums)
        keys = [x for x in cnt.keys() if x != 1 and x % 4 != 0 and x % 9 != 0 and x % 25 != 0]
        n = len(keys)
        
        def get_status(num):
            res = 0
            for p in primes:
                res = (res << 1) if num % p != 0 else (res << 1) + 1
            return res
        
        n = len(keys)
        # print(n, [bin(get_status(x))[2:] for x in keys], cnt)
        
        @lru_cache(None)
        def dp(idx, status):
            if idx == n:
                return 0 if status == 0 else 1
            x = keys[idx]
            digits = get_status(x)
            if digits & status > 0:
                return dp(idx+1, status)
            else:
                return (dp(idx+1, status) + cnt[x] * dp(idx+1, status | digits)) % MOD
            
        res = dp(0, 0)
        dup = 1
        for _ in range(cnt[1]):
            dup = (dup * 2) % MOD
        res = (dup * res + dup-1) % MOD
            
        return res
            
        