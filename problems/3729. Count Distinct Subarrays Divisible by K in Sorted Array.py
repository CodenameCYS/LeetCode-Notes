'''
=== 3729. Count Distinct Subarrays Divisible by K in Sorted Array ===

You are given an integer array nums sorted in non-descending order and a positive integer k.
A subarray of nums is good if the sum of its elements is divisible by k.
Return an integer denoting the number of distinct good subarrays of nums.
Subarrays are distinct if their sequences of values are. For example, there are 3 distinct subarrays in [1, 1, 1], namely [1], [1, 1], and [1, 1, 1].

Example 1:
    Input: nums = [1,2,3], k = 3
    Output: 3
    Explanation:
    The good subarrays are [1, 2], [3], and [1, 2, 3]. For example, [1, 2, 3] is good because the sum of its elements is 1 + 2 + 3 = 6, and 6 % k = 6 % 3 = 0.
Example 2:
    Input: nums = [2,2,2,2,2,2], k = 6
    Output: 2
    Explanation:
    The good subarrays are [2, 2, 2] and [2, 2, 2, 2, 2, 2]. For example, [2, 2, 2] is good because the sum of its elements is 2 + 2 + 2 = 6, and 6 % k = 6 % 6 = 0.
    Note that [2, 2, 2] is counted only once.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. nums is sorted in non-descending order.
    4. 1 <= k <= 109
'''
# === 311ms && 41.28MB === #
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cumsum = list(accumulate(nums, initial=0))
        reminders = [x%k for x in cumsum]
        cnt = Counter(reminders)
        # print(cnt)
        ans = sum(x * (x-1) // 2 for x in cnt.values())
        # print(ans)
        idx = 0
        while idx < n:
            rb = bisect.bisect_right(nums, nums[idx])
            m = rb - idx
            if k == 1:
                ans -= m * (m+1) // 2 - m
            else:
                l = k // gcd(k, nums[idx])
                for i in range(l, m, l):
                    ans -= m-i
            idx = rb
        return ans
