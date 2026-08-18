'''
=== 3105. Longest Strictly Increasing or Strictly Decreasing Subarray ===

You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

Example 1:
    Input: nums = [1,4,3,3,2]
    Output: 2
    Explanation:
    The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
    The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
    Hence, we return 2.
Example 2:
    Input: nums = [3,3,3,3]
    Output: 1
    Explanation:
    The strictly increasing subarrays of nums are [3], [3], [3], and [3].
    The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
    Hence, we return 1.
Example 3:
    Input: nums = [3,2,1]
    Output: 3
    Explanation:
    The strictly increasing subarrays of nums are [3], [2], and [1].
    The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
    Hence, we return 3.

Constraints:
    1. 1 <= nums.length <= 50
    2. 1 <= nums[i] <= 50
'''
# === 44ms && 16.5MB === #
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        pre, incre, cnt = 0, 0, 0
        for x in nums:
            if x > pre:
                cnt += 1
            else:
                incre = max(incre, cnt)
                cnt = 1
            pre = x
        incre = max(incre, cnt)
        
        pre, decre, cnt = math.inf, 0, 0
        for x in nums:
            if x < pre:
                cnt += 1
            else:
                decre = max(decre, cnt)
                cnt = 1
            pre = x
        decre = max(decre, cnt)
        
        return max(incre, decre)
            