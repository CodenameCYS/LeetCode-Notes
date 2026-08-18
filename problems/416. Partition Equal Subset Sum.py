'''
=== 416. Partition Equal Subset Sum ===

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.
    
Constraints:
    1. 1 <= nums.length <= 200
    2. 1 <= nums[i] <= 100
'''
# === 356ms(75.70%) && 31.4MB(5.09%) === #
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        n = len(nums)
        nums = sorted(nums, reverse=True)

        @lru_cache(None)
        def dp(idx, target):
            if target == 0:
                return True
            if target < 0 or idx >= n or sum(nums[idx:]) < target:
                return False
            return dp(idx+1, target-nums[idx]) or dp(idx+1, target)

        return dp(1, target-nums[0])