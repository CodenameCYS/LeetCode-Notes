'''
=== 3351. Sum of Good Subsequences ===

You are given an integer array nums. A good subsequence is defined as a subsequence of nums where the absolute difference between any two consecutive elements in the subsequence is exactly 1.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
Return the sum of all possible good subsequences of nums.
Since the answer may be very large, return it modulo 109 + 7.
Note that a subsequence of size 1 is considered good by definition.

Example 1:
    Input: nums = [1,2,1]
    Output: 14
    Explanation:
    Good subsequences are: [1], [2], [1], [1,2], [2,1], [1,2,1].
    The sum of elements in these subsequences is 14.
Example 2:
    Input: nums = [3,4,5]
    Output: 40
    Explanation:
    Good subsequences are: [3], [4], [5], [3,4], [4,5], [3,4,5].
    The sum of elements in these subsequences is 40.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i] <= 105
'''
MOD = 10**9+7
# === 655ms && 41.6MB === #
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [0 for _ in range(n)]
        s = [0 for _ in range(n)]
        cumcnt = defaultdict(int)
        cumsum = defaultdict(int)
        for i in range(n-1, -1, -1):
            cnt[i] = (1 + cumcnt[nums[i]-1] + cumcnt[nums[i]+1]) % MOD
            s[i] = (nums[i] + (cumcnt[nums[i]-1]+cumcnt[nums[i]+1])*nums[i] + cumsum[nums[i]-1] + cumsum[nums[i]+1]) % MOD
            
            cumcnt[nums[i]] += cnt[i]
            cumsum[nums[i]] += s[i]

        ans = 0
        for x in s:
            ans = (ans+x) % MOD
        return ans