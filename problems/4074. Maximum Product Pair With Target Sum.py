'''
=== 4074. Maximum Product Pair With Target Sum ===

You are given an integer array nums and an integer target.
A pair of distinct indices (i, j) is valid if:
    - nums[i] + nums[j] == target
    - nums[i] > nums[j]
Return a valid pair [i, j] whose product nums[i] * nums[j] is maximum among all valid pairs. If no valid pair exists, return [-1, -1].
If multiple valid pairs achieve the maximum product, you may return any of them.

Example 1:
    Input: nums = [1,2,3,4], target = 5
    Output: [2,1]
    Explanation:
    There are 2 valid pairs:
    No.	(i, j)	nums[i]	nums[j]	Sum	Product
    1	(3, 0)	4	1	5	4
    2	(2, 1)	3	2	5	6
    Both pairs sum to 5 and satisfy nums[i] > nums[j]. The second pair has the larger product, 3 * 2 = 6, so the answer is [2, 1].
Example 2:
    Input: nums = [-3,-1,4,2], target = 1
    Output: [3,1]
    Explanation:
    There are 2 valid pairs:
    No.	(i, j)	nums[i]	nums[j]	Sum	Product
    1	(2, 0)	4	-3	1	-12
    2	(3, 1)	2	-1	1	-2
    Since -2 > -12, the pair at indices (3, 1) is chosen and the answer is [3, 1].
Example 3:
    Input: nums = [3,3,5], target = 6
    Output: [-1,-1]
    Explanation:
    ​​​​​​​No valid pair exists, since nums[0] and nums[1] sum to 6 but are equal.

Constraints:
    1. 2 <= nums.length <= 100
    2. -100 <= nums[i], target <= 100​​​​​​​
'''
# === 3ms && 19.34MB === #
class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        locs = defaultdict(int)
        prod = -math.inf
        ans = [-1, -1]
        for i, num in enumerate(nums):
            locs[num] = i
        for i, x in enumerate(nums):
            y = target - x
            if x == y or y not in locs or prod >= x * y:
                continue
            j = locs[y]
            ans = [i, j] if x > y else [j, i]
            prod = x * y
        return ans