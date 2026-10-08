'''
=== 4072. Maximum Alternating Subarray Sum With One Deletion ===

You are given an integer array nums.
You may delete at most one element from nums, then choose a subarray of the resulting array.
Return the maximum possible alternating sum of the chosen subarray.
The alternating sum of an array is the sum of its elements at even indices minus the sum of its elements at odd indices. The chosen subarray is reindexed starting from 0 before calculating its alternating sum.

Example 1:
    Input: nums = [5,-5,1]
    Output: 11
    Explanation:
    Choose not to delete an element and select the entire array. Its alternating sum is 5 - (-5) + 1 = 11, which is the maximum possible.
Example 2:
    Input: nums = [10,-5,-100]
    Output: 110
    Explanation:
    Delete nums[1] = -5 to obtain [10,-100], then select the entire resulting array. Its alternating sum is 10 - (-100) = 110, which is the maximum possible.
Example 3:
    Input: nums = [4,7]
    Output: 7
    Explanation:
    Choose not to delete an element and select the subarray [7]. Its alternating sum is 7, which is the maximum possible.

Constraints:
    1. 1 <= nums.length <= 105
    2. -105 <= nums[i] <= 105
'''
# === 4794ms && 296.20MB === #
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # 只需在 1186 的基础上增加参数 rev
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, j: int, rev: bool) -> int:
            if i == n:
                return -inf  # 子数组至少要有一个数，不合法
            x = -nums[i] if rev else nums[i]
            if j == 0:
                return max(dfs(i + 1, 0, not rev), 0) + x
            return max(dfs(i + 1, 1, not rev) + x, dfs(i + 1, 0, rev))

        n = len(nums)
        ans = max(max(dfs(i, 0, False), dfs(i, 1, False)) for i in range(n))
        dfs.cache_clear()
        return ans