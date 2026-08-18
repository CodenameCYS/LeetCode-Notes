'''
=== 3040. Maximum Number of Operations With the Same Score II ===

Given an array of integers called nums, you can perform any of the following operation while nums contains at least 2 elements:
    - Choose the first two elements of nums and delete them.
    - Choose the last two elements of nums and delete them.
    - Choose the first and the last elements of nums and delete them.
The score of the operation is the sum of the deleted elements.
Your task is to find the maximum number of operations that can be performed, such that all operations have the same score.
Return the maximum number of operations possible that satisfy the condition mentioned above.

Example 1:
    Input: nums = [3,2,1,2,3,4]
    Output: 3
    Explanation: We perform the following operations:
    - Delete the first two elements, with score 3 + 2 = 5, nums = [1,2,3,4].
    - Delete the first and the last elements, with score 1 + 4 = 5, nums = [2,3].
    - Delete the first and the last elements, with score 2 + 3 = 5, nums = [].
    We are unable to perform any more operations as nums is empty.
Example 2:
    Input: nums = [3,2,6,1,4]
    Output: 2
    Explanation: We perform the following operations:
    - Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
    - Delete the last two elements, with score 1 + 4 = 5, nums = [6].
    It can be proven that we can perform at most 2 operations.
 
Constraints:
    1. 2 <= nums.length <= 2000
    2. 1 <= nums[i] <= 1000
'''
# === 1992ms && 362.7MB === #
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dp(i, j, tgt):
            if i >= j:
                return 0
            if tgt == -1:
                return 1 + max(dp(i, j-2, nums[j-1] + nums[j]), dp(i+1, j-1, nums[i] + nums[j]), dp(i+2, j, nums[i] + nums[i+1]))
            ans = 0
            if nums[i] + nums[i+1] == tgt:
                ans = max(ans, 1 + dp(i+2, j, tgt))
            if nums[i] + nums[j] == tgt:
                ans = max(ans, 1 + dp(i+1, j-1, tgt))
            if nums[j-1] + nums[j] == tgt:
                ans = max(ans, 1 + dp(i, j-2, tgt))
            return ans
        
        return dp(0, n-1, -1)