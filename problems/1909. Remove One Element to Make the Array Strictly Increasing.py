'''
=== 1909. Remove One Element to Make the Array Strictly Increasing ===

Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.
The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

Example 1:
    Input: nums = [1,2,10,5,7]
    Output: true
    Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
    [1,2,5,7] is strictly increasing, so return true.
Example 2:
    Input: nums = [2,3,1,2]
    Output: false
    Explanation:
    [3,1,2] is the result of removing the element at index 0.
    [2,1,2] is the result of removing the element at index 1.
    [2,3,2] is the result of removing the element at index 2.
    [2,3,1] is the result of removing the element at index 3.
    No resulting array is strictly increasing, so return false.
Example 3:
    Input: nums = [1,1,1]
    Output: false
    Explanation: The result of removing any element is [1,1].
    [1,1] is not strictly increasing, so return false.
Example 4:
    Input: nums = [1,2,3]
    Output: true
    Explanation: [1,2,3] is already strictly increasing, so return true.
 
Constraints:
    1. 2 <= nums.length <= 1000
    2. 1 <= nums[i] <= 1000
'''
# === 80ms && 14.6MB === #
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def is_convex(nums):
            nums = [0] + nums
            pre = 0
            cnt = 0
            for idx, x in enumerate(nums):
                if idx == 0:
                    continue
                if x <= pre:
                    if x <= nums[idx-2]:
                        return False
                    else:
                        cnt +=1
                pre = x
            return cnt <= 1
        
        def is_concave(nums):
            pre = 0
            cnt = 0
            for idx, x in enumerate(nums):
                if x <= pre:
                    cnt += 1
                else:
                    pre = x
            return cnt <= 1
        
        return is_convex(nums) or is_concave(nums)