'''
=== 18. 4Sum ===

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
    Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
    A solution set is:
    [
        [-1,  0, 0, 1],
        [-2, -1, 1, 2],
        [-2,  0, 0, 2]
    ]
'''
# === 192ms(67.77%) && 12.8MB(100%) === #
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        n = len(nums)
        for st in range(n-3):
            if 4*nums[st] > target:
                break
            for ed in range(n-1,st+2,-1):
                if nums[st] + 3*nums[ed] < target:
                    break
                i = st + 1; j = ed - 1
                s = target - nums[st] - nums[ed]
                while i<j:
                    if nums[i] + nums[j] == s:
                        result.add((nums[st], nums[i], nums[j], nums[ed]))
                        i += 1
                        j -= 1
                    elif nums[i] + nums[j] < s:
                        i += 1
                    else:
                        j -= 1
        result = [list(it) for it in result]
        return result
            
            