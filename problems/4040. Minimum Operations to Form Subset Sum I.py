'''
=== 4040. Minimum Operations to Form Subset Sum I ===

You are given an integer array nums and an integer sum.
In one operation, choose an element with current value x and replace it with either 2 * x or floor(x / 2).
For each element, all multiplication operations performed on it must occur before any division operations performed on it.
Return the minimum number of operations needed so that some subset of the resulting array has a sum exactly equal to sum. If it is impossible, return -1.
The floor() function returns the integer part of the division.

Example 1:
    Input: nums = [5,6,10], sum = 4
    Output: 3
    Explanation:
    Divide nums[0] = 5 twice: 5 → 2 → 1, costing 2 operations.
    Divide nums[1] = 6 once: 6 → 3, costing 1 operation.
    After these operations, nums = [1, 3, 10]. The subset {1, 3} sums to 4 using 3 operations in total.
Example 2:
    Input: nums = [10,2], sum = 13
    Output: 3
    Explanation:
    Divide nums[0] = 10 once: 10 → 5, costing 1 operation.
    Multiply nums[1] = 2 twice: 2 → 4 → 8, costing 2 operations.
    After these operations, nums = [5, 8]. The subset {5, 8} sums to 13 using 3 operations in total.
Example 3:
    Input: nums = [6,3], sum = 8
    Output: -1
    Explanation:​​​​​​​
    No sequence of operations lets a subset of nums sum to 8, so the answer is -1.

Constraints:
    1. 1 <= nums.length <= 100
    2. 1 <= nums[i] <= 500
    3. 1 <= sum <= 5000
'''
# === 5433ms && 19.38MB === #
class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        f = [0] + [inf] * sum

        for x in nums:
            w = x.bit_length()  # x 的二进制长度
            for i in range(sum, 0, -1):
                # 回想一下，0-1 背包是选或不选，状态转移方程为 f[i] = min(f[i], f[i-物品体积] + 物品价值)
                # 本题是分组背包，要枚举选哪个物品（枚举乘了 a 次或者除了 a 次）
                a = 0
                while x << a <= i:
                    # 物品体积为 x<<a，价值为 a
                    f[i] = min(f[i], f[i - (x << a)] + a)
                    a += 1

                # 从小到大枚举 x>>a，方便在 x>>a > i 时跳出循环
                a = w - 1
                while a > 0 and x >> a <= i:
                    # 物品体积为 x>>a，价值为 a
                    f[i] = min(f[i], f[i - (x >> a)] + a)
                    a -= 1

        return -1 if f[sum] == inf else f[sum]
