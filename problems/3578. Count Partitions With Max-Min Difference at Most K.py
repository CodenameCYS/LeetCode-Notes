'''
=== 3578. Count Partitions With Max-Min Difference at Most K ===

You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.
Return the total number of ways to partition nums under this condition.
Since the answer may be too large, return it modulo 109 + 7.

Example 1:
    Input: nums = [9,4,1,3,7], k = 4
    Output: 6
    Explanation:
    There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:
    [[9], [4], [1], [3], [7]]
    [[9], [4], [1], [3, 7]]
    [[9], [4], [1, 3], [7]]
    [[9], [4, 1], [3], [7]]
    [[9], [4, 1], [3, 7]]
    [[9], [4, 1, 3], [7]]
Example 2:
    Input: nums = [3,3,4], k = 0
    Output: 2
    Explanation:
    There are 2 valid partitions that satisfy the given conditions:
    [[3], [3], [4]]
    [[3, 3], [4]]
    
Constraints:
    1. 2 <= nums.length <= 5 * 104
    2. 1 <= nums[i] <= 109
    3. 0 <= k <= 109
'''
MOD = 10**9+7
# === 964ms && 29.5MB === #
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if max(nums) - min(nums) <= k:
            return pow(2, n-1, mod=MOD)

        dp = [1, 1] + [0 for _ in range(n-1)]
        accum_dp = [0, 1, 2] + [0 for _ in range(n-1)] 
        cache = [(nums[0], 0)]
        left = -1
        for i in range(1, n):
            while cache and nums[i] - cache[0][0] > k:
                _, idx = cache.pop(0)
                left = max(left, idx)
            while cache and cache[-1][0] - nums[i] > k:
                _, idx = cache.pop()
                left = max(left, idx)
            bisect.insort(cache, (nums[i], i))
            dp[i+1] = (accum_dp[i+1] - accum_dp[left+1]) % MOD
            accum_dp[i+2] = (accum_dp[i+1] + dp[i+1]) % MOD
        # print(dp, accum_dp)
        return dp[-1] % MOD


            