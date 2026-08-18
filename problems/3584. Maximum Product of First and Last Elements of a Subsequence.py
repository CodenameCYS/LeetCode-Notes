'''
=== 3584. Maximum Product of First and Last Elements of a Subsequence ===

You are given an integer array nums and an integer m.
Return the maximum product of the first and last elements of any subsequence of nums of size m.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: nums = [-1,-9,2,3,-2,-3,1], m = 1
    Output: 81
    Explanation:
    The subsequence [-9] has the largest product of the first and last elements: -9 * -9 = 81. Therefore, the answer is 81.
Example 2:
    Input: nums = [1,3,-5,5,6,-4], m = 3
    Output: 20
    Explanation:
    The subsequence [-5, 6, -4] has the largest product of the first and last elements.
Example 3:
    Input: nums = [2,-1,2,-6,5,2,-5,7], m = 2
    Output: 35
    Explanation:
    The subsequence [5, 7] has the largest product of the first and last elements.

Constraints:
    1. 1 <= nums.length <= 105
    2. -105 <= nums[i] <= 105
    3. 1 <= m <= nums.length
'''
# === 812ms && 33.05MB === #
class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        if m == 1:
            return max([abs(x) for x in nums])**2
        n = len(nums)
        right_min, right_max = deepcopy(nums), deepcopy(nums)
        for i in range(n-2, -1, -1):
            right_min[i] = min(nums[i], right_min[i+1])
            right_max[i] = max(nums[i], right_max[i+1])
        ans = -math.inf
        for i in range(n-m+1):
            x = nums[i]
            y1, y2 = right_min[i+m-1], right_max[i+m-1]
            ans = max(ans, x*y1, x*y2)
        return ans
