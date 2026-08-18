'''
=== 3976. Maximum Subarray Sum After Multiplier ===

You are given an integer array nums and a positive integer k.
You must choose exactly one subarray of nums and perform exactly one of the following operations:
    - Multiply each number in the chosen subarray by k.
    - Divide each number in the chosen subarray by k.
        - When dividing a positive number by k, use the floor value of the division result.
        - When dividing a negative number by k, use the ceiling value of the division result.
Return the maximum possible sum of a non-empty subarray in the resulting array.
Note that the subarray chosen for the operation and the subarray chosen for the sum may be different.

Example 1:
    Input: nums = [1,-2,3,4,-5], k = 2
    Output: 14
    Explanation:
    Multiply each number in the subarray [3, 4] by 2.
    This results in nums = [1, -2, 6, 8, -5].
    The subarray with the largest sum is [6, 8], so the output is 6 + 8 = 14.
Example 2:
    Input: nums = [-5,-4,-3], k = 2
    Output: -1
    Explanation:
    Divide each number in the subarray [-3] by 2.
    This results in nums = [-5, -4, -1].
    The subarray with the largest sum is [-1], so the output is -1.
    
Constraints:
    1. 1 <= nums.length <= 105
    2. -105 <= nums[i] <= 105
    3. 1 <= k <= 105
'''
# === 1336ms && 50.12MB === #
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        _cumsum = list(accumulate(nums, initial = 0))
        ml = [0 for _ in _cumsum]
        for i in range(n):
            ml[i+1] = min(ml[i], _cumsum[i+1])
        ans = -math.inf

        op1 = [x * k for x in nums]
        cumsum = list(accumulate(op1, initial = 0))
        _max, _max2 = -math.inf, -math.inf
        for i in range(n-1, -1, -1):
            _max2 = max(_max2, _cumsum[i+1])
            _max = max(_max, cumsum[i+1], cumsum[i] + _max2 - _cumsum[i])
            ans = max(ans, _max - cumsum[i] + max(0, _cumsum[i] - ml[i]))
        _max, _max2 = -math.inf, -math.inf
        for i in range(n-1, -1, -1):
            _max2 = max(_max2, cumsum[i+1])
            _max = max(_max, _cumsum[i+1], _cumsum[i] + _max2 - cumsum[i])
            ans = max(ans, _max - _cumsum[i])


        op2 = [x // k if x >= 0 else math.ceil(x / k) for x in nums]
        cumsum = list(accumulate(op2, initial = 0))
        _max, _max2 = -math.inf, -math.inf
        for i in range(n-1, -1, -1):
            _max2 = max(_max2, _cumsum[i+1])
            _max = max(_max, cumsum[i+1], cumsum[i] + _max2 - _cumsum[i])
            ans = max(ans, _max - cumsum[i] + max(0, _cumsum[i] - ml[i]))
        _max, _max2 = -math.inf, -math.inf
        for i in range(n-1, -1, -1):
            _max2 = max(_max2, cumsum[i+1])
            _max = max(_max, _cumsum[i+1], _cumsum[i] + _max2 - cumsum[i])
            ans = max(ans, _max - _cumsum[i])

        return ans