'''
=== 220. Contains Duplicate III ===

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true
Example 2:
    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true
Example 3:
    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false
'''
import bisect
# === 100ms && 15.4MB === #
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        window = []
        for i, n in enumerate(nums):
            if i > k:
                window.pop(bisect_left(window, nums[i-k-1]))
            left_idx = bisect.bisect_left(window, n-t)
            right_idx = bisect.bisect_right(window, n+t)
            # print(window, n, left_idx, right_idx)
            if left_idx != right_idx:
                return True
            bisect.insort(window, n)
        return False