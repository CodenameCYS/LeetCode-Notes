'''
=== 3862. Find the Smallest Balanced Index ===

You are given an integer array nums.
An index i is balanced if the sum of elements strictly to the left of i equals the product of elements strictly to the right of i.
If there are no elements to the left, the sum is considered as 0. Similarly, if there are no elements to the right, the product is considered as 1.
Return an integer denoting the smallest balanced index. If no balanced index exists, return -1.

Example 1:
    Input: nums = [2,1,2]
    Output: 1
    Explanation:
    For index i = 1:
    Left sum = nums[0] = 2
    Right product = nums[2] = 2
    Since the left sum equals the right product, index 1 is balanced.
    No smaller index satisfies the condition, so the answer is 1.
Example 2:
    Input: nums = [2,8,2,2,5]
    Output: 2
    Explanation:
    For index i = 2:
    Left sum = 2 + 8 = 10
    Right product = 2 * 5 = 10
    Since the left sum equals the right product, index 2 is balanced.
    No smaller index satisfies the condition, so the answer is 2.
Example 3:
    Input: nums = [1]
    Output: -1
    For index i = 0:
    The left side is empty, so the left sum is 0.
    The right side is empty, so the right product is 1.
    Since the left sum does not equal the right product, index 0 is not balanced.
    Therefore, no balanced index exists and the answer is -1.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
'''
# === 218ms && 31.71MB === #
class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        
        tot, _max = 0, 0
        for num in nums:
            tot += num
            _max = max(_max, abs(tot))
        
        ans = -1
        _sum, _prd = tot, 1
        for i in range(n-1, -1, -1):
            _sum -= nums[i]
            if _sum == _prd:
                ans = i
            if nums[i] == 0 or _prd <= _max:
                _prd *= nums[i]
        return ans
