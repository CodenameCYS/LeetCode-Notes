'''
=== 3176. Find the Maximum Length of a Good Subsequence I ===

You are given an integer array nums and a non-negative integer k. A sequence of integers seq is called good if there are at most k indices i in the range [0, seq.length - 2] such that seq[i] != seq[i + 1].
Return the maximum possible length of a good subsequence of nums.

Example 1:
    Input: nums = [1,2,1,1,3], k = 2
    Output: 4
    Explanation:
    The maximum length subsequence is [1,2,1,1,3].
Example 2:
    Input: nums = [1,2,3,4,5,1], k = 0
    Output: 2
    Explanation:
    The maximum length subsequence is [1,2,3,4,5,1].

Constraints:
    1. 1 <= nums.length <= 500
    2. 1 <= nums[i] <= 109
    3. 0 <= k <= min(nums.length, 25)
'''
# === 150ms && 17.1MB === #
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0 for _ in range(k+1)] for _ in range(n)]
        same = [defaultdict(int) for _ in range(k+1)]
        diff = [0 for _ in range(k+1)]
        ans = 0
        for i, num in enumerate(nums):
            dp[i][0] = 1
            for j in range(k+1):
                dp[i][j] = 1 + same[j][num]
                if j > 0:
                    dp[i][j] = max(dp[i][j], diff[j-1]+1)
                ans = max(ans, dp[i][j])
            for j in range(k+1):
                same[j][num] = max(same[j][num], dp[i][j])
                diff[j] = max(diff[j], dp[i][j])
        return ans
                
    
                