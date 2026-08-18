'''
=== 3880. Minimum Absolute Difference Between Two Values ===

You are given an integer array nums consisting only of 0, 1, and 2.
A pair of indices (i, j) is called valid if nums[i] == 1 and nums[j] == 2.
Return the minimum absolute difference between i and j among all valid pairs. If no valid pair exists, return -1.
The absolute difference between indices i and j is defined as abs(i - j).

Example 1:
    Input: nums = [1,0,0,2,0,1]
    Output: 2
    Explanation:
    The valid pairs are:
    (0, 3) which has absolute difference of abs(0 - 3) = 3.
    (5, 3) which has absolute difference of abs(5 - 3) = 2.
    Thus, the answer is 2.
Example 2:
    Input: nums = [1,0,1,0]
    Output: -1
    Explanation:
    There are no valid pairs in the array, thus the answer is -1.

Constraints:
    1. 1 <= nums.length <= 100
    2. 0 <= nums[i] <= 2
'''
# === 4ms && 19.40MB === #
class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        index2 = [i for i, x in enumerate(nums) if x == 2]
        m = len(index2)
        if m == 0:
            return -1
        ans = math.inf
        for i, num in enumerate(nums):
            if num != 1:
                continue
            j = bisect.bisect(index2, i)
            ans = min(ans, abs(i-index2[j-1]), abs(i-index2[j%m]))
        return ans if ans != math.inf else -1