'''
=== 3473. Sum of K Subarrays With Length at Least M ===

You are given an integer array nums and two integers, k and m.
Return the maximum sum of k non-overlapping subarrays of nums, where each subarray has a length of at least m.
A subarray is a contiguous sequence of elements within an array.
 
Example 1:
    Input: nums = [1,2,-1,3,3,4], k = 2, m = 2
    Output: 13
    Explanation:
    The optimal choice is:
    Subarray nums[3..5] with sum 3 + 3 + 4 = 10 (length is 3 >= m).
    Subarray nums[0..1] with sum 1 + 2 = 3 (length is 2 >= m).
    The total sum is 10 + 3 = 13.
Example 2:
    Input: nums = [-10,3,-1,-2], k = 4, m = 1
    Output: -10
    Explanation:
    The optimal choice is choosing each element as a subarray. The output is (-10) + 3 + (-1) + (-2) = -10.

Constraints:
    1. 1 <= nums.length <= 2000
    2. -104 <= nums[i] <= 104
    3. 1 <= k <= floor(nums.length / m)
    4. 1 <= m <= 3
'''
# === 4233ms && 793.4MB === #
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dp(idx, k, in_subarray):
            if idx >= n:
                return 0 if k == 0 else -math.inf
            elif k == 0:
                return 0 if not in_subarray else max(nums[idx] + dp(idx+1, k, in_subarray), 0)
            if (n-idx) < m * k:
                return -math.inf
            elif (n-idx) == m * k:
                return sum(nums[idx:])
            
            if not in_subarray:
                return max(sum(nums[idx:idx+m]) + dp(idx+m, k-1, True), dp(idx+1, k, False))
            else:
                return max(nums[idx] + dp(idx+1, k, True), sum(nums[idx:idx+m]) + dp(idx+m, k-1, True), dp(idx+1, k, False))
            
        return dp(0, k, False)
            
        