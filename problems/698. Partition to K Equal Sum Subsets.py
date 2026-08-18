'''
=== 698. Partition to K Equal Sum Subsets ===

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
    Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
    Output: True
    Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 
Note:
    1. 1 <= k <= len(nums) <= 16.
    2. 0 < nums[i] < 10000.
'''
# === 36ms(94.94%) && 12.8MB(100%) === #
class Solution:
    def split_nums(self, nums, states, k, target, tmp, st, n):
        if k <= 1:
            return True
        is_succeed = False
        for i in range(st, n):
            if states[i] == 1:
                continue
            if nums[i] + tmp < target:
                states[i] = 1
                is_succeed = is_succeed or self.split_nums(nums, states, k, target, tmp+nums[i], i+1, n)
                states[i] = 0
            elif nums[i] + tmp == target:
                states[i] = 1
                is_succeed = is_succeed or self.split_nums(nums, states, k-1, target, 0, 0, n)
                states[i] = 0
        return is_succeed
            
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums = sorted(nums, reverse=True)
        s = sum(nums)
        if s % k != 0:
            return False
        s = s // k
        while nums != [] and nums[0] == s:
            k -= 1
            nums.pop(0)
        states = [0 for it in nums]
        return self.split_nums(nums, states, k, s, 0, 0, len(nums))
        