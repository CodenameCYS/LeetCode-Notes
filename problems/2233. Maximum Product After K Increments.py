'''
=== 2233. Maximum Product After K Increments ===

You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.
Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: nums = [0,4], k = 5
    Output: 20
    Explanation: Increment the first number 5 times.
    Now nums = [5, 4], with a product of 5 * 4 = 20.
    It can be shown that 20 is maximum product possible, so we return 20.
    Note that there may be other ways to increment nums to have the maximum product.
Example 2:
    Input: nums = [6,3,3,2], k = 2
    Output: 216
    Explanation: Increment the second number 1 time and increment the fourth number 1 time.
    Now nums = [6, 4, 3, 3], with a product of 6 * 4 * 3 * 3 = 216.
    It can be shown that 216 is maximum product possible, so we return 216.
    Note that there may be other ways to increment nums to have the maximum product.
 
Constraints:
    1. 1 <= nums.length, k <= 105
    2. 0 <= nums[i] <= 106
'''
# === 1311ms && 26.1MB === #
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        nums = sorted(nums)
        cumsum = list(accumulate(nums))
        n = len(nums)
        i, j = nums[0], ceil((k + cumsum[-1]) / len(nums)) + 1
        while j-i > 1:
            m = (i+j) // 2
            idx = bisect.bisect_right(nums, m)
            delta = idx * m - cumsum[idx-1]
            if delta > k:
                j = m
            else:
                i = m
        # print(nums, k, i, j)
        
        idx = bisect.bisect_right(nums, i)
        j = k + cumsum[idx-1] - i * (idx)
        res = 1
        for _ in range(j):
            res = res * (i+1) % MOD
        for _ in range(idx-j):
            res = res * i % MOD
        for x in nums[idx:]:
            res = res * x % MOD
        return res
        
            
        