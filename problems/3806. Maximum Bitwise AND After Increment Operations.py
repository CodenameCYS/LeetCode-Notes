'''
=== 3806. Maximum Bitwise AND After Increment Operations ===

You are given an integer array nums and two integers k and m.
You may perform at most k operations. In one operation, you may choose any index i and increase nums[i] by 1.
Return an integer denoting the maximum possible bitwise AND of any subset of size m after performing up to k operations optimally.

Example 1:
    Input: nums = [3,1,2], k = 8, m = 2
    Output: 6
    Explanation:
    We need a subset of size m = 2. Choose indices [0, 2].
    Increase nums[0] = 3 to 6 using 3 operations, and increase nums[2] = 2 to 6 using 4 operations.
    The total number of operations used is 7, which is not greater than k = 8.
    The two chosen values become [6, 6], and their bitwise AND is 6, which is the maximum possible.
Example 2:
    Input: nums = [1,2,8,4], k = 7, m = 3
    Output: 4
    Explanation:
    We need a subset of size m = 3. Choose indices [0, 1, 3].
    Increase nums[0] = 1 to 4 using 3 operations, increase nums[1] = 2 to 4 using 2 operations, and keep nums[3] = 4.
    The total number of operations used is 5, which is not greater than k = 7.
    The three chosen values become [4, 4, 4], and their bitwise AND is 4, which is the maximum possible.​​​​​​​
Example 3:
    Input: nums = [1,1], k = 3, m = 2
    Output: 2
    Explanation:
    We need a subset of size m = 2. Choose indices [0, 1].
    Increase both values from 1 to 2 using 1 operation each.
    The total number of operations used is 2, which is not greater than k = 3.
    The two chosen values become [2, 2], and their bitwise AND is 2, which is the maximum possible.
 
Constraints:
    1. 1 <= n == nums.length <= 5 * 104
    2. 1 <= nums[i] <= 109
    3. 1 <= k <= 109
    4. 1 <= m <= n
'''
# === 702ms && 24.01MB === #
class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        ops = [0] * len(nums)  # 每个数的操作次数
        ans = 0
        max_width = (max(nums) + k).bit_length()
        for bit in range(max_width - 1, -1, -1):
            target = ans | (1 << bit)  # 注意 target 要带着 ans 已经填好的 1
            for i, x in enumerate(nums):
                j = (target & ~x).bit_length()
                # j-1 是从高到低第一个 target 是 1，x 是 0 的比特位
                # target = 10110
                #      x = 11010
                #            ^
                #           j-1
                # x 高于 j-1 的比特位不变，其余变成和 target 一样
                # 上面的例子要把 010 变成 110
                mask = (1 << j) - 1
                ops[i] = (target & mask) - (x & mask)

            # 贪心，取前 m 小的操作次数
            if sum(sorted(ops)[:m]) <= k:
                ans = target  # 答案的 bit 位可以填 1
        return ans
