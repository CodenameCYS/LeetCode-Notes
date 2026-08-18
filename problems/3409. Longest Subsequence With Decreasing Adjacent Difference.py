'''
=== 3409. Longest Subsequence With Decreasing Adjacent Difference ===

You are given an array of integers nums.
Your task is to find the length of the longest subsequence seq of nums, such that the absolute differences between consecutive elements form a non-increasing sequence of integers. In other words, for a subsequence seq0, seq1, seq2, ..., seqm of nums, |seq1 - seq0| >= |seq2 - seq1| >= ... >= |seqm - seqm - 1|.
Return the length of such a subsequence.
A subsequence is an non-empty array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: nums = [16,6,3]
    Output: 3
    Explanation: 
    The longest subsequence is [16, 6, 3] with the absolute adjacent differences [10, 3].
Example 2:
    Input: nums = [6,5,3,4,2,1]
    Output: 4
    Explanation:
    The longest subsequence is [6, 4, 2, 1] with the absolute adjacent differences [2, 2, 1].
Example 3:
    Input: nums = [10,20,10,19,10,20]
    Output: 5
    Explanation: 
    The longest subsequence is [10, 20, 10, 19, 10] with the absolute adjacent differences [10, 10, 9, 9].

Constraints:
    1. 2 <= nums.length <= 104
    2. 1 <= nums[i] <= 300
'''
# === 11133ms && 21.8MB === #
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        m = max(nums)
        nums = [x-1 for x in nums]
        dp = [[-m for _ in range(m)] for _ in range(m)]
        for num in nums:
            for pre in range(m):
                delta = abs(num - pre)
                dp[num][delta] = max(dp[num][delta], dp[pre][delta]+1)
            
            for delta in range(m-1, -1, -1):
                dp[num][delta] = max(dp[num][delta], 1)
                if delta < m-1:
                    dp[num][delta] = max(dp[num][delta], dp[num][delta+1])
        return max(dp[num][0] for num in range(m))
            