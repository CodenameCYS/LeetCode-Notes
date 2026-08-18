'''
=== 3891. Minimum Increase to Maximize Special Indices ===

You are given an integer array nums of length n.
An index i (0 < i < n - 1) is special if nums[i] > nums[i - 1] and nums[i] > nums[i + 1].
You may perform operations where you choose any index i and increase nums[i] by 1.
Your goal is to:
    - Maximize the number of special indices.
    - Minimize the total number of operations required to achieve that maximum.
Return an integer denoting the minimum total number of operations required.

Example 1:
    Input: nums = [1,2,2]
    Output: 1
    Explanation:​​​​​​​
    Start with nums = [1, 2, 2].
    Increase nums[1] by 1, array becomes [1, 3, 2].
    The final array is [1, 3, 2] has 1 special index, which is the maximum achievable.
    It is impossible to achieve this number of special indices with fewer operations. Thus, the answer is 1.
Example 2:
    Input: nums = [2,1,1,3]
    Output: 2
    Explanation:​​​​​​​
    Start with nums = [2, 1, 1, 3].
    Perform 2 operations at index 1, array becomes [2, 3, 1, 3].
    The final array is [2, 3, 1, 3] has 1 special index, which is the maximum achievable. Thus, the answer is 2.
Example 3:
    Input: nums = [5,2,1,4,3]
    Output: 4
    Explanation:​​​​​​​​​​​​​​​​​​​​​
    Start with nums = [5, 2, 1, 4, 3].
    Perform 4 operations at index 1, array becomes [5, 6, 1, 4, 3].
    The final array is [5, 6, 1, 4, 3] has 2 special indices, which is the maximum achievable. Thus, the answer is 4.​​​​​​​
 
Constraints:
    1. 3 <= n <= 105
    2. 1 <= nums[i] <= 109
'''
# === 457ms && 221.12MB === #
class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def get_op_num(idx):
            if n < 3:
                return 0
            elif idx+2 >= n:
                return 0
            if nums[idx+1] > nums[idx] and nums[idx+1] > nums[idx+2]:
                return get_op_num(idx+2)
            else:
                return max(nums[idx], nums[idx+2]) - nums[idx+1] + 1 + get_op_num(idx+2)

        if n % 2 == 1:
            return get_op_num(0)
        
        @lru_cache(None)
        def dp(idx):
            if idx >= n-1:
                return 0
            if nums[idx] > nums[idx-1] and nums[idx] > nums[idx+1]:
                return dp(idx+2)
            return min(
                max(nums[idx-1], nums[idx+1])-nums[idx]+1 + dp(idx+2), 
                get_op_num(idx)
            )
        
        return dp(1)
            