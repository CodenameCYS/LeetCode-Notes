'''
=== 3469. Find Minimum Cost to Remove Array Elements ===

You are given an integer array nums. Your task is to remove all elements from the array by performing one of the following operations at each step until nums is empty:
    - Choose any two elements from the first three elements of nums and remove them. The cost of this operation is the maximum of the two elements removed.
    - If fewer than three elements remain in nums, remove all the remaining elements in a single operation. The cost of this operation is the maximum of the remaining elements.
Return the minimum cost required to remove all the elements.

Example 1:
    Input: nums = [6,2,8,4]
    Output: 12
    Explanation:
    Initially, nums = [6, 2, 8, 4].
    In the first operation, remove nums[0] = 6 and nums[2] = 8 with a cost of max(6, 8) = 8. Now, nums = [2, 4].
    In the second operation, remove the remaining elements with a cost of max(2, 4) = 4.
    The cost to remove all elements is 8 + 4 = 12. This is the minimum cost to remove all elements in nums. Hence, the output is 12.
Example 2:
    Input: nums = [2,1,3,3]
    Output: 5
    Explanation:
    Initially, nums = [2, 1, 3, 3].
    In the first operation, remove nums[0] = 2 and nums[1] = 1 with a cost of max(2, 1) = 2. Now, nums = [3, 3].
    In the second operation remove the remaining elements with a cost of max(3, 3) = 3.
    The cost to remove all elements is 2 + 3 = 5. This is the minimum cost to remove all elements in nums. Hence, the output is 5.

Constraints:
    1. 1 <= nums.length <= 1000
    2. 1 <= nums[i] <= 106
'''
# === 6234ms && 344.7MB === #
class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        if len(set(nums)) == 1:
            return nums[0] * ((n+1) // 2)
        
        @lru_cache(10**4)
        def dp(pre, idx):
            if idx == n-1:
                return max(nums[pre], nums[idx])
            elif idx == n-2:
                candidates = sorted([nums[pre], nums[idx], nums[idx+1]])
                return candidates[0] + candidates[-1]
            return min(
                max(nums[idx], nums[idx+1]) + dp(pre, idx+2),
                max(nums[pre], nums[idx+1]) + dp(idx, idx+2),
                max(nums[pre], nums[idx]) + dp(idx+1, idx+2)
            )
        
        return dp(0, 1)