'''
=== 3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND ===

You are given an integer array nums.
Return the length of the longest strictly increasing subsequence in nums whose bitwise AND is non-zero. If no such subsequence exists, return 0.
A subsequence is a non-empty array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: nums = [5,4,7]
    Output: 2
    Explanation:
    One longest strictly increasing subsequence is [5, 7]. The bitwise AND is 5 AND 7 = 5, which is non-zero.
Example 2:
    Input: nums = [2,3,6]
    Output: 3
    Explanation:
    The longest strictly increasing subsequence is [2, 3, 6]. The bitwise AND is 2 AND 3 AND 6 = 2, which is non-zero.
Example 3:
    Input: nums = [0,1]
    Output: 1
    Explanation:
    One longest strictly increasing subsequence is [1]. The bitwise AND is 1, which is non-zero.

Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i] <= 109​​​​​​​
'''
# === 1885ms && 36.06MB === #
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        def LIS(arr):
            cache = []
            for num in arr:
                idx = bisect.bisect_left(cache, num)
                if idx >= len(cache):
                    cache.append(num)
                else:
                    cache[idx] = num
            # print(arr, len(cache), cache)
            return len(cache)

        ans = 0
        for i in range(32):
            flag = 1<<i
            arr = [num for num in nums if num & flag != 0]
            if len(arr) <= ans:
                continue
            ans = max(ans, LIS(arr))
        return ans
            