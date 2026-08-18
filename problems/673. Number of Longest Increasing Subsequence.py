'''
=== 673. Number of Longest Increasing Subsequence ===

Given an integer array nums, return the number of longest increasing subsequences.

Example 1:
    Input: nums = [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
    Input: nums = [2,2,2,2,2]
    Output: 5
    Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Constraints:
    1. 0 <= nums.length <= 2000
    2. -106 <= nums[i] <= 106
'''
# === 1664ms（7.37%）&& 14.3MB === #
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [[1, 1] for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
                    elif dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0]+1, dp[j][1]]
        _max = max(dp)[0]
        return sum([x[1] for x in dp if x[0] == _max])
            
        