'''
=== 3866. First Unique Even Element ===

You are given an integer array nums.
Return an integer denoting the first even integer (earliest by array index) that appears exactly once in nums. If no such integer exists, return -1.
An integer x is considered even if it is divisible by 2.

Example 1:
    Input: nums = [3,4,2,5,4,6]
    Output: 2
    Explanation:
    Both 2 and 6 are even and they appear exactly once. Since 2 occurs first in the array, the answer is 2.
Example 2:
    Input: nums = [4,4]
    Output: -1
    Explanation:
    No even integer appears exactly once, so return -1.

Constraints:
    1. 1 <= nums.length <= 100
    2. 1 <= nums[i] <= 100
'''
# === 0ms && 19.25MB === #
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        for num in nums:
            if cnt[num] == 1 and num % 2 == 0:
                return num
        return -1