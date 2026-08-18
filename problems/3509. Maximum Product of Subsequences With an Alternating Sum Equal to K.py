'''
=== 3509. Maximum Product of Subsequences With an Alternating Sum Equal to K ===

You are given an integer array nums and two integers, k and limit. Your task is to find a non-empty subsequence of nums that:
    - Has an alternating sum equal to k.
    - Maximizes the product of all its numbers without the product exceeding limit.
Return the product of the numbers in such a subsequence. If no subsequence satisfies the requirements, return -1.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

Example 1:
    Input: nums = [1,2,3], k = 2, limit = 10
    Output: 6
    Explanation:
    The subsequences with an alternating sum of 2 are:
    [1, 2, 3]
    Alternating Sum: 1 - 2 + 3 = 2
    Product: 1 * 2 * 3 = 6
    [2]
    Alternating Sum: 2
    Product: 2
    The maximum product within the limit is 6.
Example 2:
    Input: nums = [0,2,3], k = -5, limit = 12
    Output: -1
    Explanation:
    A subsequence with an alternating sum of exactly -5 does not exist.
Example 3:
    Input: nums = [2,2,3,3], k = 0, limit = 9
    Output: 9
    Explanation:
    The subsequences with an alternating sum of 0 are:
    [2, 2]
    Alternating Sum: 2 - 2 = 0
    Product: 2 * 2 = 4
    [3, 3]
    Alternating Sum: 3 - 3 = 0
    Product: 3 * 3 = 9
    [2, 2, 3, 3]
    Alternating Sum: 2 - 2 + 3 - 3 = 0
    Product: 2 * 2 * 3 * 3 = 36
    The subsequence [2, 2, 3, 3] has the greatest product with an alternating sum equal to k, but 36 > 9. The next greatest product is 9, which is within the limit.

Constraints:
    1. 1 <= nums.length <= 150
    2. 0 <= nums[i] <= 12
    3. -105 <= k <= 105
    4. 1 <= limit <= 5000
'''
# === 602ms && 281.8MB === #
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        
        n = len(nums)
        ans = -1
        
        upper_bounds = [x for x in nums]
        lower_bounds = [x for x in nums]
        lower_bounds[-1] = 0
        for i in range(n-2, -1, -1):
            upper_bounds[i] = max(upper_bounds[i] - lower_bounds[i+1], upper_bounds[i], upper_bounds[i+1])
            lower_bounds[i] = min(lower_bounds[i], lower_bounds[i] - upper_bounds[i+1], lower_bounds[i+1])
        # print(upper_bounds)
        # print(lower_bounds)
        
        @lru_cache(maxsize=1000000)
        def dp(idx, is_even, s, prod):
            nonlocal ans, upper_bounds, lower_bounds
            if idx >= n:
                return
            if prod == 0 and ans != -1:
                return
            if prod > limit and ans != -1:
                return
            if prod <= ans and prod * 2 > limit:
                return
            if is_even and s + upper_bounds[idx] < k:
                return
            elif (not is_even) and s - upper_bounds[idx] > k:
                return
            nxt_sum = s + nums[idx] if is_even else s - nums[idx]
            if nxt_sum == k and prod * nums[idx] <= limit:
                ans = max(ans, prod * nums[idx])
            if ans == -1 or nums[idx] != 0:
                dp(idx+1, not is_even, nxt_sum, prod*nums[idx])
            dp(idx+1, is_even, s, prod)
            return
        
        dp(0, True, 0, 1)
        return ans
                