'''
=== 2563. Count the Number of Fair Pairs ===

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
A pair (i, j) is fair if:
    - 0 <= i < j < n, and
    - lower <= nums[i] + nums[j] <= upper
 
Example 1:
    Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
    Output: 6
    Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:
    Input: nums = [1,7,9,2,5], lower = 11, upper = 11
    Output: 1
    Explanation: There is a single fair pair: (2,3).
    
Constraints:
    1. 1 <= nums.length <= 105
    2. nums.length == n
    3. -109 <= nums[i] <= 109
    4. -109 <= lower <= upper <= 109
'''
# === 908ms && 29MB === #
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        res = 0
        for i, x in enumerate(nums):
            lb = bisect.bisect_left(nums, lower - x)
            rb = bisect.bisect_right(nums, upper - x)
            if lower-x <= x <= upper-x:
                res += rb - lb -1
            else:
                res += rb - lb
        return res // 2
            