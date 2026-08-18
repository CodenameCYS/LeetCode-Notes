'''
=== 2962. Count Subarrays Where Max Element Appears at Least K Times ===

You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.

Example 1:
    Input: nums = [1,3,2,3,3], k = 2
    Output: 6
    Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:
    Input: nums = [1,4,2,1], k = 3
    Output: 0
    Explanation: No subarray contains the element 4 at least 3 times.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 106
    3. 1 <= k <= 105
'''
# === 1040ms && 30.7MB === #
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        _max = max(nums)
        n = len(nums)
        flags = []
        for i, x in enumerate(nums):
            if x == _max:
                flags.append(i)
        m = len(flags)
        if m < k:
            return 0
        
        ans = 0
        flags.insert(0, -1)
        for i in range(m-k+1):
            ans += (flags[i+1]-flags[i]) * (n-flags[i+k])
        return ans