'''
=== 2741. Special Permutations ===

You are given a 0-indexed integer array nums containing n distinct positive integers. A permutation of nums is called special if:
    - For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] % nums[i] == 0.
Return the total number of special permutations. As the answer could be large, return it modulo 109 + 7.

Example 1:
    Input: nums = [2,3,6]
    Output: 2
    Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.
Example 2:
    Input: nums = [1,4,3]
    Output: 2
    Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.
 
Constraints:
    1. 2 <= nums.length <= 14
    2. 1 <= nums[i] <= 109
'''
# === 3257ms && 219.7MB === #
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        n = len(nums)
        allowlist = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    allowlist[i].append(j)
                    allowlist[j].append(i)
               
        @lru_cache(None)
        def dp(idx, status):
            if status == 2**n-1:
                return 1
            res = 0
            for i in allowlist[idx]:
                if status & (1 << i) == 0:
                    res += dp(i, status | 1 << i)
            return res % MOD
        
        return sum(dp(i, 1 << i) for i in range(n)) % MOD
        