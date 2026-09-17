'''
=== 4051. Count Subarrays with Distant Sums ===

You are given an integer array nums and two integers goal and k.
A subarray nums[i..j] is considered distant if the absolute difference between its sum and goal is at least k.
Return the number of distant subarrays.

Example 1:
    Input: nums = [1,2,1], goal = 4, k = 1
    Output: 5
    Explanation:
    The distant subarrays for k = 1 are:
    i	j	nums[i..j]	Sum	abs(sum - goal)
    0	0	[1]	1	3
    1	1	[2]	2	2
    2	2	[1]	1	3
    0	1	[1, 2]	3	1
    1	2	[2, 1]	3	1
    Thus, the answer is 5.
Example 2:
    Input: nums = [2,-1,3], goal = 2, k = 2
    Output: 2
    Explanation:
    The distant subarrays for k = 2 are:
    i	j	nums[i..j]	Sum	abs(sum - goal)
    1	1	[-1]	-1	3
    0	2	[2, -1, 3]	4	2
    Thus, the answer is 2.
Example 3:
    Input: nums = [-3,1,2], goal = 0, k = 3
    Output: 2
    Explanation:
    The distant subarrays for k = 3 are:
    i	j	nums[i..j]	Sum	abs(sum - goal)
    0	0	[-3]	-3	3
    1	2	[1, 2]	3	3
    Thus, the answer is 2.

Constraints:
    1. 1 <= nums.length <= 105
    2. -109 <= nums[i] <= 109
    3. -109 <= goal <= 109
    4. 0 <= k <= 109
'''
# === 839ms && 33.62MB === #
class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        if k == 0:
            n = len(nums)
            return n * (n+1) // 2
        prefix = [0]
        ans, tot = 0, 0
        for num in nums:
            tot += num
            lb, rb = tot-goal-k, tot-goal+k
            left = bisect.bisect_right(prefix, lb)
            right = bisect.bisect_left(prefix, rb)
            # print(f"prefix={prefix}, sj={tot}, lb={lb}, rb={rb}, lidx={left}, ridx={right}, valid={left + (len(prefix)-right)}")
            ans += left + (len(prefix)-right)
            bisect.insort(prefix, tot)
        return ans
