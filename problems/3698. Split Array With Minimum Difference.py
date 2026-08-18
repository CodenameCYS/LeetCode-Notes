'''
=== 3698. Split Array With Minimum Difference ===

You are given an integer array nums.
Split the array into exactly two subarrays, left and right, such that left is strictly increasing and right is strictly decreasing.
Return the minimum possible absolute difference between the sums of left and right. If no valid split exists, return -1.

Example 1:
    Input: nums = [1,3,2]
    Output: 2
    Explanation:
    i	left	right	Validity	left sum	right sum	Absolute difference
    0	[1]	[3, 2]	Yes	1	5	|1 - 5| = 4
    1	[1, 3]	[2]	Yes	4	2	|4 - 2| = 2
    Thus, the minimum absolute difference is 2.
Example 2:
    Input: nums = [1,2,4,3]
    Output: 4
    Explanation:
    i	left	right	Validity	left sum	right sum	Absolute difference
    0	[1]	[2, 4, 3]	No	1	9	-
    1	[1, 2]	[4, 3]	Yes	3	7	|3 - 7| = 4
    2	[1, 2, 4]	[3]	Yes	7	3	|7 - 3| = 4
    Thus, the minimum absolute difference is 4.
Example 3:
    Input: nums = [3,1,2]
    Output: -1
    Explanation:
    No valid split exists, so the answer is -1.

Constraints:
    1. 2 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
'''
# === 73ms && 30.68MB === #
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        while l < n-1 and nums[l] < nums[l+1]:
            l += 1
        r = n-1
        while r > 0 and nums[r] < nums[r-1]:
            r -= 1
        if r-l > 1:
            return -1
        elif r-l == 1:
            return abs(sum(nums[:r]) - sum(nums[r:]))
        else:
            return min(abs(sum(nums[:r]) - sum(nums[r:])), abs(sum(nums[:r+1]) - sum(nums[r+1:])))