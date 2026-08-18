'''
=== 3953. Maximum Score with Co-Prime Element ===

You are given an integer array nums of length n and an integer maxVal.
You may change any element in nums to any positive integer less than or equal to maxVal. Each such change costs 1.
Two integers are co-prime if their greatest common divisor (GCD) is 1.
After all modifications, you must choose an index i such that, nums[i] is co-prime with every other element nums[j].
Let:
    - selectedValue be the final value of nums[i] after modifications.
    - modificationCost be the total number of elements changed.
The score is defined as score = selectedValue - modificationCost.
Return the maximum possible score.

Example 1:
    Input: nums = [3,4,6], maxVal = 5
    Output: 4
    Explanation:
    Change nums[2] from 6 to 5, which costs 1. Choose nums[2] = 5, since it is co-prime with 3 and 4.
    selectedValue = 5
    modificationCost = 1
    The score is 5 - 1 = 4
Example 2:
    Input: nums = [1,2,3], maxVal = 4
    Output: 3
    Explanation:
    No modifications are required. Choose nums[2] = 3, since it is co-prime with 1 and 2.
    selectedValue = 3
    modificationCost = 0
    The score is 3 - 0 = 3
Example 3:
    Input: nums = [2,2], maxVal = 1
    Output: 1
    Explanation:
    Change nums[0] from 2 to 1, which costs 1. Choose nums[1] = 2, since it is co-prime with 1.
    selectedValue = 2
    modificationCost = 1
    The score is ​​​​​​​2 - 1 = 1

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
    3. 1 <= maxVal <= 10​​​​​​​5
'''
# === 529ms && 49.50MB === #
MX = 100_001

# 预处理莫比乌斯函数
# 当 n > 1 时，sum_{d|n} mu[d] = 0
# 所以 mu[n] = -sum_{d|n ∧ d<n} mu[d]
mu = [0] * MX
mu[1] = 1
for i in range(1, MX):
    for j in range(i * 2, MX, i):
        mu[j] -= mu[i]  # i 是 j 的真因子

# 预处理不含平方因子的因子列表
# 本题不需要因子 1
divisors = [[] for _ in range(MX)]
for i in range(2, MX):
    if mu[i]:
        for j in range(i, MX, i):
            divisors[j].append(i)  # i 是 j 的因子，且 mu[i] != 0

class Solution:
    def maxScore(self, nums: list[int], maxVal: int) -> int:
        print(divisors[12])
        print([(x, mu[x]) for x in divisors[12]])

        max_num = max(nums)
        cnt = [0] * (max_num + 1)
        for x in nums:
            cnt[x] += 1

        cnt_multi = [0] * (max_num + 1)
        for i in range(2, max_num + 1):
            for j in range(i, max_num + 1, i):
                cnt_multi[i] += cnt[j]  # 统计 nums 中有多少个数是 i 的倍数

        # 单独计算 selected_value = 1 时的得分
        ans = 1 if cnt[1] > 0 else 0

        # 枚举 selected_value
        for selected_value in range(max(max_num, maxVal), 1, -1):
            # 优化：如果 selected_value <= ans，那么 ans 不会变大，跳出循环
            if selected_value <= ans:
                break

            if selected_value > maxVal and cnt[selected_value] == 0:
                continue  # 无法改成 selected_value

            # 与 selected_value 不互质的数，其中一个数改成 selected_value，其余数都改成 1
            cost = 0
            for d in divisors[selected_value]:
                if d > max_num:
                    break
                cost -= mu[d] * cnt_multi[d]

            if selected_value <= max_num and cnt[selected_value] > 0:
                cost -= 1  # 如果某个 nums[i] 恰好等于 selected_value，可以少改一次
            elif cost == 0:
                cost = 1  # 至少要有一个数改成 selected_value

            # print(selected_value, cost, ans)
            ans = max(ans, selected_value - cost)

        return ans
