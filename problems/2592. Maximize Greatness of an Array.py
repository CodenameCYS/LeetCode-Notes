'''
=== 2592. Maximize Greatness of an Array ===

You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.
We define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].
Return the maximum possible greatness you can achieve after permuting nums.

Example 1:
    Input: nums = [1,3,5,2,1,3,1]
    Output: 4
    Explanation: One of the optimal rearrangements is perm = [2,5,1,3,3,1,1].
    At indices = 0, 1, 3, and 4, perm[i] > nums[i]. Hence, we return 4.
Example 2:
    Input: nums = [1,2,3,4]
    Output: 3
    Explanation: We can prove the optimal perm is [2,3,4,1].
    At indices = 0, 1, and 2, perm[i] > nums[i]. Hence, we return 3.
    
Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i] <= 109
'''
# === 724ms && 40MB === #
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums = sorted(nums)
        cnt = Counter(nums)
        vals = sorted(cnt.keys())
        remain = Counter(nums)
        n = len(vals)
        res = 0
        for i in range(n-1):
            k = cnt[vals[i]]
            for j in range(i+1, n):
                if k == 0:
                    break
                elif remain[vals[j]] >= k:
                    remain[vals[j]] -= k
                    res += k
                    k = 0
                else:
                    k -= remain[vals[j]]
                    res += remain[vals[j]]
                    remain[vals[j]] = 0
        return res
                    