'''
=== 3850. Count Sequences to K ===

You are given an integer array nums, and an integer k.
Start with an initial value val = 1 and process nums from left to right. At each index i, you must choose exactly one of the following actions:
    - Multiply val by nums[i].
    - Divide val by nums[i].
    - Leave val unchanged.
After processing all elements, val is considered equal to k only if its final rational value exactly equals k.
Return the count of distinct sequences of choices that result in val == k.
Note: Division is rational (exact), not integer division. For example, 2 / 4 = 1 / 2.

Example 1:
    Input: nums = [2,3,2], k = 6
    Output: 2
    Explanation:
    The following 2 distinct sequences of choices result in val == k:
    Sequence	Operation on nums[0]	Operation on nums[1]	Operation on nums[2]	Final val
    1	Multiply: val = 1 * 2 = 2	Multiply: val = 2 * 3 = 6	Leave val unchanged	6
    2	Leave val unchanged	Multiply: val = 1 * 3 = 3	Multiply: val = 3 * 2 = 6	6
Example 2:
    Input: nums = [4,6,3], k = 2
    Output: 2
    Explanation:
    The following 2 distinct sequences of choices result in val == k:
    Sequence	Operation on nums[0]	Operation on nums[1]	Operation on nums[2]	Final val
    1	Multiply: val = 1 * 4 = 4	Divide: val = 4 / 6 = 2 / 3	Multiply: val = (2 / 3) * 3 = 2	2
    2	Leave val unchanged	Multiply: val = 1 * 6 = 6	Divide: val = 6 / 3 = 2	2
Example 3:
    Input: nums = [1,5], k = 1
    Output: 3
    Explanation:
    The following 3 distinct sequences of choices result in val == k:
    Sequence	Operation on nums[0]	Operation on nums[1]	Final val
    1	Multiply: val = 1 * 1 = 1	Leave val unchanged	1
    2	Divide: val = 1 / 1 = 1	Leave val unchanged	1
    3	Leave val unchanged	Leave val unchanged	1

Constraints:
    1. 1 <= nums.length <= 19
    2. 1 <= nums[i] <= 6
    3. 1 <= k <= 1015
'''
DELTA = 1e-6
# === 561ms && 203.53MB === #
class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(idx, val):
            if idx >= n:
                return 1 if abs(val - k) <= DELTA else 0
            return dp(idx+1, val * nums[idx]) + dp(idx+1, val / nums[idx]) + dp(idx+1, val)

        return dp(0, 1)