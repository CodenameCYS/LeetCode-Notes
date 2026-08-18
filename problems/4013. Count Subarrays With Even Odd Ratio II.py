'''
=== 4013. Count Subarrays With Even Odd Ratio II ===

You are given an integer array nums and two integers a and b.
For a subarray, let:
    - x be the number of even elements.
    - y be the number of odd elements.
The ratio of even to odd elements in a subarray is defined as x / y, where ratios are compared by their exact rational values.
A subarray is considered valid if:
    - y > 0, and
    - x / y <= a / b.
Return the number of valid subarrays in nums.

Example 1:
    Input: nums = [1,2,1,2], a = 3, b = 2
    Output: 7
    Explanation:
    The following are the valid subarrays:
    Subarray	Values	Even Count	Odd Count	Ratio
    nums[0..0]	[1]	0	1	0 / 1
    nums[0..1]	[1, 2]	1	1	1 / 1
    nums[0..2]	[1, 2, 1]	1	2	1 / 2
    nums[0..3]	[1, 2, 1, 2]	2	2	2 / 2
    nums[1..2]	[2, 1]	1	1	1 / 1
    nums[2..2]	[1]	0	1	0 / 1
    nums[2..3]	[1, 2]	1	1	1 / 1
    Thus, the number of valid subarrays is 7.
Example 2:
    Input: nums = [2,2,1], a = 2, b = 1
    Output: 3
    Explanation:
    The following are the valid subarrays:
    Subarray	Values	Even Count	Odd Count	Ratio
    nums[0..2]	[2, 2, 1]	2	1	2 / 1
    nums[1..2]	[2, 1]	1	1	1 / 1
    nums[2..2]	[1]	0	1	0 / 1
    Thus, the number of valid subarrays is 3.
Example 3:
    Input: nums = [2,2,2], a = 1, b = 1
    Output: 0
    Explanation:
    Every subarray contains 0 odd numbers, so no subarray is valid.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. 1 <= a, b <= 109
'''
# === 113ms && 27.87MB === #
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        nums = [x%2 for x in nums]
        nums = [-b if x == 0 else a for x in nums]
        tot = 0
        cache = [0]
        ans = 0
        for num in nums:
            tot += num
            idx = bisect.bisect_right(cache, tot)
            ans += idx
            cache.insert(idx, tot)
        return ans
