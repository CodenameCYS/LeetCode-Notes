'''
=== 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target ===

Given an array nums and an integer target.
Return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

Example 1:
    Input: nums = [1,1,1,1,1], target = 2
    Output: 2
    Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
Example 2:
    Input: nums = [-1,3,5,1,4,2,-9], target = 6
    Output: 2
    Explanation: There are 3 subarrays with sum equal to 6.
    ([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
Example 3:
    Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
    Output: 3
Example 4:
    Input: nums = [0,0,0], target = 0
    Output: 3
 
Constraints:
    1. 1 <= nums.length <= 10^5
    2. -10^4 <= nums[i] <= 10^4
    3. 0 <= target <= 10^6
'''
# === 2560ms && 202.9MB === #
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cumsum = [0 for i in range(n+1)]
        for i in range(n):
            cumsum[i+1] = cumsum[i] + nums[i]
            
        cache = {}
        for idx, s in enumerate(cumsum):
            cache[s] = cache.get(s, []) + [idx]
            
        @lru_cache(None)
        def dp(idx):
            if idx > n:
                return 0
            s1 = dp(idx+1)
            aim = target + cumsum[idx]
            next_loc = [i for i in cache.get(aim, []) if i > idx]
            if next_loc == []:
                return s1
            else:
                return max(s1, 1 + dp(next_loc[0]))
            
        return dp(0)
    
# === 812ms && 33.8MB === #
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memory = {0: 0}
        prefix_sum = 0
        dp = [0 for i in range(n+1)]
        
        for i, k in enumerate(nums):
            prefix_sum += k
            if prefix_sum - target in memory.keys():
                dp[i+1] = max(1+dp[memory[prefix_sum - target]], dp[i])
            else:
                dp[i+1] = dp[i]
            memory[prefix_sum] = i+1
            
        return dp[-1]