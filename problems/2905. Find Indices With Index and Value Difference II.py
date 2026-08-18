'''
=== 2905. Find Indices With Index and Value Difference II ===

You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.
Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:
    - abs(i - j) >= indexDifference, and
    - abs(nums[i] - nums[j]) >= valueDifference
Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.
Note: i and j may be equal.

Example 1:
    Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
    Output: [0,3]
    Explanation: In this example, i = 0 and j = 3 can be selected.
    abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
    Hence, a valid answer is [0,3].
    [3,0] is also a valid answer.
Example 2:
    Input: nums = [2,1], indexDifference = 0, valueDifference = 0
    Output: [0,0]
    Explanation: In this example, i = 0 and j = 0 can be selected.
    abs(0 - 0) >= 0 and abs(nums[0] - nums[0]) >= 0.
    Hence, a valid answer is [0,0].
    Other valid answers are [0,1], [1,0], and [1,1].
Example 3:
    Input: nums = [1,2,3], indexDifference = 2, valueDifference = 4
    Output: [-1,-1]
    Explanation: In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
    Hence, [-1,-1] is returned.
 
Constraints:
    1. 1 <= n == nums.length <= 105
    2. 0 <= nums[i] <= 109
    3. 0 <= indexDifference <= 105
    4. 0 <= valueDifference <= 109
'''
# === 852ms && 42.9MB === #
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        maxs = [(x, i) for i, x in enumerate(nums)]
        mins = [(x, i) for i, x in enumerate(nums)]
        for i in range(n-2, -1, -1):
            maxs[i] = max(maxs[i], maxs[i+1])
            mins[i] = min(mins[i], mins[i+1])
        for i in range(n-indexDifference):
            val, idx = maxs[i+indexDifference]
            if abs(val - nums[i]) >= valueDifference:
                return [i, idx]
            val, idx = mins[i+indexDifference]
            if abs(val - nums[i]) >= valueDifference:
                return [i, idx]
        return [-1, -1]