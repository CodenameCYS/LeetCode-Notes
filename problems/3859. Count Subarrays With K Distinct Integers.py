'''
=== 3859. Count Subarrays With K Distinct Integers ===

You are given an integer array nums and two integers k and m.
Return an integer denoting the count of subarrays of nums such that:
    - The subarray contains exactly k distinct integers.
    - Within the subarray, each distinct integer appears at least m times.

Example 1:
    Input: nums = [1,2,1,2,2], k = 2, m = 2
    Output: 2
    Explanation:
    The possible subarrays with k = 2 distinct integers, each appearing at least m = 2 times are:
    Subarray	Distinct
    numbers	Frequency
    [1, 2, 1, 2]	{1, 2} → 2	{1: 2, 2: 2}
    [1, 2, 1, 2, 2]	{1, 2} → 2	{1: 2, 2: 3}
    Thus, the answer is 2.
Example 2:
    Input: nums = [3,1,2,4], k = 2, m = 1
    Output: 3
    Explanation:
    The possible subarrays with k = 2 distinct integers, each appearing at least m = 1 times are:
    Subarray	Distinct
    numbers	Frequency
    [3, 1]	{3, 1} → 2	{3: 1, 1: 1}
    [1, 2]	{1, 2} → 2	{1: 1, 2: 1}
    [2, 4]	{2, 4} → 2	{2: 1, 4: 1}
    Thus, the answer is 3.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
    3. 1 <= k, m <= nums.length
'''
# === 219ms && 28.75MB === #
class Solution:
    def countSubarrays(self, nums, k: int, m: int) -> int:
        def calc(distinct_limit: int) -> int:
            cnt = defaultdict(int)
            ge_m = 0  # 窗口中的出现次数 >= m 的元素个数
            ans = left = 0
            for x in nums:
                # 1. 入
                cnt[x] += 1
                if cnt[x] == m:
                    ge_m += 1

                # 2. 出
                while len(cnt) >= distinct_limit and ge_m >= k:
                    out = nums[left]
                    if cnt[out] == m:
                        ge_m -= 1
                    cnt[out] -= 1
                    if cnt[out] == 0:
                        del cnt[out]
                    left += 1

                # 3. 更新答案
                ans += left
            return ans

        return calc(k) - calc(k + 1)