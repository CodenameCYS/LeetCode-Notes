'''
=== 3350. Adjacent Increasing Subarrays Detection II ===

Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:
    - Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
    - The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [2,5,7,8,9,2,3,4,3,1]
    Output: 3
    Explanation:
    The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
    The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
    These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:
    Input: nums = [1,2,3,4,4,4,4,5,6,7]
    Output: 2
    Explanation:
    The subarray starting at index 0 is [1, 2], which is strictly increasing.
    The subarray starting at index 2 is [3, 4], which is also strictly increasing.
    These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
 
Constraints:
    1. 2 <= nums.length <= 2 * 105
    2. -109 <= nums[i] <= 109
'''
# === 1274ms && 44.7MB === #
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        s = []
        pre, cnt = -math.inf, 0
        for num in nums:
            if num <= pre:
                s.append(cnt)
                cnt = 0
            pre = num
            cnt += 1
        if cnt > 0:
            s.append(cnt)
            
        n = len(s)
        ans = max(x // 2 for x in s)
        for i in range(n-1):
            ans = max(ans, min(s[i], s[i+1]))
        return ans