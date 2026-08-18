'''
=== 1755. Closest Subsequence Sum ===

You are given an integer array nums and an integer goal.
You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).
Return the minimum possible value of abs(sum - goal).
Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

Example 1:
    Input: nums = [5,-7,3,5], goal = 6
    Output: 0
    Explanation: Choose the whole array as a subsequence, with a sum of 6.
    This is equal to the goal, so the absolute difference is 0.
Example 2:
    Input: nums = [7,-9,15,-2], goal = -5
    Output: 1
    Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
    The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
Example 3:
    Input: nums = [1,2,3], goal = -7
    Output: 7
 
Constraints:
    1. 1 <= nums.length <= 40
    2. -107 <= nums[i] <= 107
    3. -109 <= goal <= 109
'''
# === 3068ms && 679.2MB === #
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        s = sum(nums)
        
        @lru_cache(None)
        def dp(i, j, s):
            if s == goal:
                return 0
            elif i > j:
                return abs(goal-s)
            elif s > goal:
                if nums[j] <= 0:
                    return abs(goal - s)
                return min(dp(i, j-1, s-nums[j]), dp(i, j-1, s))
            else:
                if nums[i] >= 0:
                    return abs(goal - s)
                return min(dp(i+1, j, s-nums[i]), dp(i+1, j, s))
            
        return dp(0, n-1, s)
                
        