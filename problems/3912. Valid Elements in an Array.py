'''
=== 3912. Valid Elements in an Array ===

You are given an integer array nums.
An element nums[i] is considered valid if it satisfies at least one of the following conditions:
    - It is strictly greater than every element to its left.
    - It is strictly greater than every element to its right.
The first and last elements are always valid.
Return an array of all valid elements in the same order as they appear in nums.

Example 1:
    Input: nums = [1,2,4,2,3,2]
    Output: [1,2,4,3,2]
    Explanation:
    nums[0] and nums[5] are always valid.
    nums[1] and nums[2] are strictly greater than every element to their left.
    nums[4] is strictly greater than every element to its right.
    Thus, the answer is [1, 2, 4, 3, 2].
Example 2:
    Input: nums = [5,5,5,5]
    Output: [5,5]
    Explanation:
    The first and last elements are always valid.
    No other elements are strictly greater than all elements to their left or to their right.
    Thus, the answer is [5, 5].
Example 3:
    Input: nums = [1]
    Output: [1]
    Explanation:
    Since there is only one element, it is always valid. Thus, the answer is [1].

Constraints:
    1. 1 <= nums.length <= 100
    2. 1 <= nums[i] <= 100
'''
# === 7ms && 19.32MB === # 
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 2:
            return nums
        l2r, r2l = deepcopy(nums), deepcopy(nums)
        for i in range(n-1):
            l2r[i+1] = max(nums[i+1], l2r[i])
            r2l[n-2-i] = max(nums[n-2-i], r2l[n-1-i])
        ans = []
        for i in range(1, n-1):
            if nums[i] > l2r[i-1] or nums[i] > r2l[i+1]:
                ans.append(nums[i])
        return [nums[0]] + ans + [nums[-1]]