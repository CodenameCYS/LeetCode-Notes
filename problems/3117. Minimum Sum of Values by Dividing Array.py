'''
=== 3117. Minimum Sum of Values by Dividing Array ===

You are given two arrays nums and andValues of length n and m respectively.
The value of an array is equal to the last element of that array.
You have to divide nums into m disjoint contiguous subarrays such that for the ith subarray [li, ri], the bitwise AND of the subarray elements is equal to andValues[i], in other words, nums[li] & nums[li + 1] & ... & nums[ri] == andValues[i] for all 1 <= i <= m, where & represents the bitwise AND operator.
Return the minimum possible sum of the values of the m subarrays nums is divided into. If it is not possible to divide nums into m subarrays satisfying these conditions, return -1.

Example 1:
    Input: nums = [1,4,3,3,2], andValues = [0,3,3,2]
    Output: 12
    Explanation:
    The only possible way to divide nums is:
    [1,4] as 1 & 4 == 0.
    [3] as the bitwise AND of a single element subarray is that element itself.
    [3] as the bitwise AND of a single element subarray is that element itself.
    [2] as the bitwise AND of a single element subarray is that element itself.
    The sum of the values for these subarrays is 4 + 3 + 3 + 2 = 12.
Example 2:
    Input: nums = [2,3,5,7,7,7,5], andValues = [0,7,5]
    Output: 17
    Explanation:
    There are three ways to divide nums:
    [[2,3,5],[7,7,7],[5]] with the sum of the values 5 + 7 + 5 == 17.
    [[2,3,5,7],[7,7],[5]] with the sum of the values 7 + 7 + 5 == 19.
    [[2,3,5,7,7],[7],[5]] with the sum of the values 7 + 7 + 5 == 19.
    The minimum possible sum of the values is 17.
Example 3:
    Input: nums = [1,2,3,4], andValues = [2]
    Output: -1
    Explanation:
    The bitwise AND of the entire array nums is 0. As there is no possible way to divide nums into a single subarray to have the bitwise AND of elements 2, return -1.

Constraints:
    1. 1 <= n == nums.length <= 104
    2. 1 <= m == andValues.length <= min(n, 10)
    3. 1 <= nums[i] < 105
    4. 0 <= andValues[j] < 105
'''
# === 1353ms && 414.1MB === #
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)

        @lru_cache(None)
        def dp(idx, k, pre):
            if idx >= n:
                return 0 if k >= m else math.inf
            if k >= m:
                return math.inf
            if pre & nums[idx] < andValues[k]:
                return math.inf
            elif pre & nums[idx] == andValues[k]:
                return min(nums[idx] + dp(idx+1, k+1, nums[idx+1] if idx+1 < n else -1), dp(idx+1, k, pre & nums[idx]))
            else:
                return dp(idx+1, k, pre & nums[idx])
        
        ans = dp(0, 0, nums[0])
        return ans if ans != math.inf else -1
            