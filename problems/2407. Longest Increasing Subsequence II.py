'''
=== 2407. Longest Increasing Subsequence II ===

You are given an integer array nums and an integer k.
Find the longest subsequence of nums that meets the following requirements:
    - The subsequence is strictly increasing and
    - The difference between adjacent elements in the subsequence is at most k.
Return the length of the longest subsequence that meets the requirements.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: nums = [4,2,1,4,3,4,5,8,15], k = 3
    Output: 5
    Explanation:
    The longest subsequence that meets the requirements is [1,3,4,5,8].
    The subsequence has a length of 5, so we return 5.
    Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger than 3.
Example 2:
    Input: nums = [7,4,5,1,8,12,4,7], k = 5
    Output: 4
    Explanation:
    The longest subsequence that meets the requirements is [4,5,8,12].
    The subsequence has a length of 4, so we return 4.
Example 3:
    Input: nums = [1,5], k = 1
    Output: 1
    Explanation:
    The longest subsequence that meets the requirements is [1].
    The subsequence has a length of 1, so we return 1.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i], k <= 105
'''
# === 5014ms && 64.7MB === #
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        u = max(nums)
        mx = [0] * (4 * u)

        def modify(o: int, l: int, r: int, i: int, val: int) -> None:
            if l == r:
                mx[o] = val
                return
            m = (l + r) // 2
            if i <= m: modify(o * 2, l, m, i, val)
            else: modify(o * 2 + 1, m + 1, r, i, val)
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])

        # 返回区间 [L,R] 内的最大值
        def query(o: int, l: int, r: int, L: int, R: int) -> int:  # L 和 R 在整个递归过程中均不变，将其大写，视作常量
            if L <= l and r <= R: return mx[o]
            res = 0
            m = (l + r) // 2
            if L <= m: res = query(o * 2, l, m, L, R)
            if R > m: res = max(res, query(o * 2 + 1, m + 1, r, L, R))
            return res

        for x in nums:
            if x == 1:
                modify(1, 1, u, 1, 1)
            else:
                res = 1 + query(1, 1, u, max(x - k, 1), x - 1)
                modify(1, 1, u, x, res)
        return mx[1]
