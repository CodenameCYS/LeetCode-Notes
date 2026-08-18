'''
=== 2597. The Number of Beautiful Subsets ===

You are given an array nums of positive integers and a positive integer k.
A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.
Return the number of non-empty beautiful subsets of the array nums.
A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Example 1:
    Input: nums = [2,4,6], k = 2
    Output: 4
    Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
    It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:
    Input: nums = [1], k = 1
    Output: 1
    Explanation: The beautiful subset of the array nums is [1].
    It can be proved that there is only 1 beautiful subset in the array [1].
 
Constraints:
    1. 1 <= nums.length <= 20
    2. 1 <= nums[i], k <= 1000
'''
# === 4614ms && 16.1MB === #
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        nums = sorted(cnt.keys())
        indices = {x: i for i, x in enumerate(nums)}
            
        n = len(nums)
        
        def dfs(idx, s):
            if idx == n:
                return 1 if s != 0 else 0
            
            res = dfs(idx+1, s)
            if (1 << idx) & s == 0:
                s = s | (1 << idx)
                if nums[idx] + k in indices:
                    s = s | (1 << indices[nums[idx] + k])
                res += (2**cnt[nums[idx]]-1) * dfs(idx+1, s)
            return res
        
        return dfs(0, 0)
                    
# === 90ms && 22.4MB === #
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        banned = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if abs(nums[i]-nums[j]) == k:
                    banned[i] = banned[i] | (1<<j)
        
        @lru_cache(None)
        def dfs(idx, s):
            if idx == n:
                return 1
            res = dfs(idx+1, s)
            if (1<<idx) & s == 0:
                res += dfs(idx+1, s | banned[idx])
            return res
        
        return dfs(0, 0) - 1