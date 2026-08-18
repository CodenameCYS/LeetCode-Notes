'''
=== 3098. Find the Sum of Subsequence Powers ===

You are given an integer array nums of length n, and a positive integer k.
The power of a subsequence is defined as the minimum absolute difference between any two elements in the subsequence.
Return the sum of powers of all subsequences of nums which have length equal to k.
Since the answer may be large, return it modulo 109 + 7.

Example 1:
    Input: nums = [1,2,3,4], k = 3
    Output: 4
    Explanation:
    There are 4 subsequences in nums which have length 3: [1,2,3], [1,3,4], [1,2,4], and [2,3,4]. The sum of powers is |2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4.
Example 2:
    Input: nums = [2,2], k = 2
    Output: 0
    Explanation:
    The only subsequence in nums which has length 2 is [2,2]. The sum of powers is |2 - 2| = 0.
Example 3:
    Input: nums = [4,3,-1], k = 2
    Output: 10
    Explanation:
    There are 3 subsequences in nums which have length 2: [4,3], [4,-1], and [3,-1]. The sum of powers is |4 - 3| + |4 - (-1)| + |3 - (-1)| = 10.

Constraints:
    1. 2 <= n == nums.length <= 50
    2. -108 <= nums[i] <= 108
    3. 2 <= k <= n
'''
# === 796ms && 329.2MB === #
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        nums = sorted(nums)
        delta = set()
        for i in range(n-1):
            for j in range(i+1, n):
                delta.add(nums[j]-nums[i])
        delta = sorted(delta, reverse=True)
                
        @lru_cache(None)
        def dp(idx, md, k, pre):
            if k == 0:
                return 1
            if n-idx < k:
                return 0
            if pre is not None and nums[idx] - pre < md:
                return dp(idx+1, md, k, pre) % MOD
            else:
                return (dp(idx+1, md, k, pre) + dp(idx+1, md, k-1, nums[idx])) % MOD
        
        ans = 0
        s = 0
        for d in delta:
            cnt = dp(0, d, k, None)
            ans = (ans + d * (cnt-s)) % MOD
            s = cnt
        return ans
                
                            
                            