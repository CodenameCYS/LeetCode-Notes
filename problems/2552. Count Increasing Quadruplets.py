'''
=== 2552. Count Increasing Quadruplets ===

Given a 0-indexed integer array nums of size n containing all numbers from 1 to n, return the number of increasing quadruplets.
A quadruplet (i, j, k, l) is increasing if:
    - 0 <= i < j < k < l < n, and
    - nums[i] < nums[k] < nums[j] < nums[l].
 
Example 1:
    Input: nums = [1,3,2,4,5]
    Output: 2
    Explanation: 
    - When i = 0, j = 1, k = 2, and l = 3, nums[i] < nums[k] < nums[j] < nums[l].
    - When i = 0, j = 1, k = 2, and l = 4, nums[i] < nums[k] < nums[j] < nums[l]. 
    There are no other quadruplets, so we return 2.
Example 2:
    Input: nums = [1,2,3,4]
    Output: 0
    Explanation: There exists only one quadruplet with i = 0, j = 1, k = 2, l = 3, but since nums[j] < nums[k], we return 0.
 
Constraints:
    1. 4 <= nums.length <= 4000
    2. 1 <= nums[i] <= nums.length
    3. All the integers of nums are unique. nums is a permutation.
'''
# === 9216ms && 688.1MB === #
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [x-1 for x in nums]
        
        left_small = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1):
            for j in range(nums[i]):
                left_small[i+1][j] = left_small[i][j]
            for j in range(nums[i]+1, n):
                left_small[i+1][j] = left_small[i][j] + 1
        # print(left_small)
        
        right_big = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(nums[i+1]):
                right_big[i][j] = right_big[i+1][j] + 1
            for j in range(nums[i+1], n):
                right_big[i][j] = right_big[i+1][j]
        # print(right_big)
        
        res = 0
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                if nums[i] < nums[j]:
                    continue
                res += left_small[i][nums[j]] * right_big[j][nums[i]]
        return res