'''
=== 3835. Count Subarrays With Cost Less Than or Equal to K ===

You are given an integer array nums, and an integer k.
For any subarray nums[l..r], define its cost as:
cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1).
Return an integer denoting the number of subarrays of nums whose cost is less than or equal to k.

Example 1:
    Input: nums = [1,3,2], k = 4
    Output: 5
    Explanation:
    We consider all subarrays of nums:
    nums[0..0]: cost = (1 - 1) * 1 = 0
    nums[0..1]: cost = (3 - 1) * 2 = 4
    nums[0..2]: cost = (3 - 1) * 3 = 6
    nums[1..1]: cost = (3 - 3) * 1 = 0
    nums[1..2]: cost = (3 - 2) * 2 = 2
    nums[2..2]: cost = (2 - 2) * 1 = 0
    There are 5 subarrays whose cost is less than or equal to 4.
Example 2:
    Input: nums = [5,5,5,5], k = 0
    Output: 10
    Explanation:
    For any subarray of nums, the maximum and minimum values are the same, so the cost is always 0.
    As a result, every subarray of nums has cost less than or equal to 0.
    For an array of length 4, the total number of subarrays is (4 * 5) / 2 = 10.
Example 3:
    Input: nums = [1,2,3], k = 0
    Output: 3
    Explanation:
    The only subarrays of nums with cost 0 are the single-element subarrays, and there are 3 of them.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. 0 <= k <= 1015
'''
# === 9393ms && 34.62MB === #
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i, j, n = 0, 0, len(nums)
        cache = []
        ans = 0
        while i < n:
            while j < n and (cache == [] or (cache[-1]-cache[0]) * len(cache) <= k):
                bisect.insort(cache, nums[j])
                j += 1
            if (cache[-1]-cache[0]) * len(cache) <= k:
                ans += len(cache)
            else:
                ans += len(cache) - 1
            cache.pop(bisect.bisect_left(cache, nums[i]))
            i += 1
        return ans