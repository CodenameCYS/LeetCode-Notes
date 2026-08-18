'''
=== 1793. Maximum Score of a Good Subarray ===

You are given an array of integers nums (0-indexed) and an integer k.
The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.
Return the maximum possible score of a good subarray.

Example 1:
    Input: nums = [1,4,3,7,4,5], k = 3
    Output: 15
    Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
Example 2:
    Input: nums = [5,5,4,5,4,1,1,1], k = 0
    Output: 20
    Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 2 * 104
    3. 0 <= k < nums.length
'''
# === 1320ms && 24.6MB === #
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i, j, n = k, k, len(nums)
        _min = nums[k]
        res = nums[k]
        while i-1 >= 0 and j+1 < n:
            if nums[i-1] <= nums[j+1]:
                _min = min(_min, nums[j+1])
                j += 1
            else:
                _min = min(_min, nums[i-1])
                i -= 1
            res = max(res, (j-i+1)*_min)
        while i-1 >= 0:
            _min = min(_min, nums[i-1])
            i -= 1
            res = max(res, (j-i+1)*_min)
        while j+1 < n:
            _min = min(_min, nums[j+1])
            j += 1
            res = max(res, (j-i+1)*_min)
        return res
                