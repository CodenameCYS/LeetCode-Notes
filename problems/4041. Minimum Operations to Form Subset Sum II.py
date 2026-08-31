'''
=== 4041. Minimum Operations to Form Subset Sum II ===

You are given an integer array nums and an integer sum.
In one operation, choose an element with current value x and replace it with either 2 * x or floor(x / 2).
For each element, multiplication and division operations may be performed in any order.
Return the minimum number of operations needed so that some subset of the resulting array has a sum exactly equal to sum. If it is impossible, return -1.
The floor() function returns the integer part of the division.

Example 1:
    Input: nums = [10,2], sum = 13
    Output: 3
    Explanation:
    Divide nums[0] = 10 once: 10 → 5, costing 1 operation.
    Multiply nums[1] = 2 twice: 2 → 4 → 8, costing 2 operations.
    After these operations, nums = [5, 8]. The subset {5, 8} sums to 13 using 3 operations in total.
Example 2:
    Input: nums = [6,3], sum = 8
    Output: 2
    Explanation:​​​​​​​
    Turn nums[1] = 3 into 2 using 2 operations:
    Divide nums[1] to get 1.
    Multiply nums[1] = 1 to get 2.
    After these operations, nums = [6, 2]. The subset {6, 2} sums to 8 using 2 operations in total.
Example 3:
    Input: nums = [2,2], sum = 7
    Output: -1
    Explanation:
    No sequence of operations lets a subset of nums sum to 7, so the answer is -1.
    
Constraints:
    1. 1 <= nums.length <= 100
    2. 1 <= nums[i] <= 500
    3. 1 <= sum <= 5000
'''
# === 9404ms && 19.38MB === #
class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        f = [0] + [inf] * sum

        for x in nums:
            # 生成这一组的所有物品，相同体积的物品，只保留价值最小的物品
            costs = defaultdict(lambda: inf)
            a = 0
            while x >> a:
                b = 0
                while x >> a << b <= sum:
                    v = x >> a << b
                    costs[v] = min(costs[v], a + b)
                    b += 1
                a += 1

            # 按照体积从小到大排序，方便跳出循环
            items = sorted(costs.items())

            for i in range(sum, 0, -1):
                for v, c in items:
                    if v > i:
                        break
                    f[i] = min(f[i], f[i - v] + c)  # 手写 min 更快，见【Python3 更快的写法】

        return -1 if f[sum] == inf else f[sum]
