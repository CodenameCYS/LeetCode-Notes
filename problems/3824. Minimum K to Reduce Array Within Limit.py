'''
=== 3824. Minimum K to Reduce Array Within Limit ===

You are given a positive integer array nums.
For a positive integer k, define nonPositive(nums, k) as the minimum number of operations needed to make every element of nums non-positive. In one operation, you can choose an index i and reduce nums[i] by k.
Return an integer denoting the minimum value of k such that nonPositive(nums, k) <= k2.

Example 1:
    Input: nums = [3,7,5]
    Output: 3
    Explanation:
    When k = 3, nonPositive(nums, k) = 6 <= k2.
    Reduce nums[0] = 3 one time. nums[0] becomes 3 - 3 = 0.
    Reduce nums[1] = 7 three times. nums[1] becomes 7 - 3 - 3 - 3 = -2.
    Reduce nums[2] = 5 two times. nums[2] becomes 5 - 3 - 3 = -1.
Example 2:
    Input: nums = [1]
    Output: 1
    Explanation:
    When k = 1, nonPositive(nums, k) = 1 <= k2.
    Reduce nums[0] = 1 one time. nums[0] becomes 1 - 1 = 0.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
'''
# === 1327ms && 33.66MB === #
class Solution:
    def minimumK(self, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums) <= 1:
            return 1

        def is_possible(k):
            return sum(ceil(x/k) for x in nums) <= k*k

        i, j = 1, max(max(nums), ceil(sqrt(n)))
        while j-i > 1:
            m = (i+j) // 2
            if is_possible(m):
                j = m
            else:
                i = m
        return j