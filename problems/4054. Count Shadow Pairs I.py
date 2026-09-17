'''
=== 4054. Count Shadow Pairs I ===

You are given an integer array nums of length n.
A pair of indices (i, j) is called a shadow pair if all of the following conditions are satisfied:
    - 0 <= i < j < n
    - nums[i] < nums[j]
    - There does not exist an index k such that i < k < j and nums[k] < nums[i] < nums[j].
Return the total number of shadow pairs.

Example 1:
    Input: nums = [3,1,4,1,5]
    Output: 3
    Explanation:
    (i, j)	nums[i]	nums[j]	Shadow Pair
    (1, 2)	1	4	No index k exists such that 1 < k < 2
    (1, 4)	1	5	nums[2] = 4 and nums[3] = 1 are not smaller than 1
    (3, 4)	1	5	No index k exists such that 3 < k < 4
    Thus, the answer is 3.
Example 2:
    Input: nums = [6,7,6,6,7]
    Output: 4
    Explanation:
    (i, j)	nums[i]	nums[j]	Shadow Pair
    (0, 1)	6	7	No index k exists such that 0 < k < 1
    (0, 4)	6	7	nums[1] = 7, nums[2] = 6, and nums[3] = 6 are not smaller than 6
    (2, 4)	6	7	nums[3] = 6 is not smaller than 6
    (3, 4)	6	7	No index k exists such that 3 < k < 4
    Thus, the answer is 4.
Example 3:
    Input: nums = [1,2,3,4]
    Output: 6
    Explanation:
    (i, j)	nums[i]	nums[j]	Shadow Pair
    (0, 1)	1	2	No index k exists such that 0 < k < 1
    (0, 2)	1	3	nums[1] = 2 is not smaller than 1
    (0, 3)	1	4	nums[1] = 2 and nums[2] = 3 are not smaller than 1
    (1, 2)	2	3	No index k exists such that 1 < k < 2
    (1, 3)	2	4	nums[2] = 3 is not smaller than 2
    (2, 3)	3	4	No index k exists such that 2 < k < 3
    Thus, the answer is 6.

Constraints:
    1. 3 <= n == nums.length <= 105
    2. 1 <= nums[i] <= 109
'''
# === 362ms && 32.28MB === #
class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        stack = []
        ans = 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            idx = bisect.bisect_left(stack, num)
            ans += idx
            stack.append(num)
        return ans