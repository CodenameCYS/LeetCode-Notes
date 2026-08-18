'''
=== 1995. Count Special Quadruplets ===

Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
    1. nums[a] + nums[b] + nums[c] == nums[d], and
    2. a < b < c < d
 
Example 1:
    Input: nums = [1,2,3,6]
    Output: 1
    Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
Example 2:
    Input: nums = [3,3,6,4,5]
    Output: 0
    Explanation: There are no such quadruplets in [3,3,6,4,5].
Example 3:
    Input: nums = [1,1,1,3,5]
    Output: 4
    Explanation: The 4 quadruplets that satisfy the requirement are:
    - (0, 1, 2, 3): 1 + 1 + 1 == 3
    - (0, 1, 3, 4): 1 + 1 + 3 == 5
    - (0, 2, 3, 4): 1 + 1 + 3 == 5
    - (1, 2, 3, 4): 1 + 1 + 3 == 5
 
Constraints:
    1. 4 <= nums.length <= 50
    2. 1 <= nums[i] <= 100
'''
# === 920ms && 14MB === #
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        n = len(nums)
        res = 0
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    s = nums[i] + nums[j] + nums[k]
                    for l in range(k+1, n):
                        if nums[l] == s:
                            res += 1
        return res
                    