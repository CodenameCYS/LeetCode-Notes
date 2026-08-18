'''
=== 3780. Maximum Sum of Three Numbers Divisible by Three ===

You are given an integer array nums.
Your task is to choose exactly three integers from nums such that their sum is divisible by three.
Return the maximum possible sum of such a triplet. If no such triplet exists, return 0.

Example 1:
    Input: nums = [4,2,3,1]
    Output: 9
    Explanation:
    The valid triplets whose sum is divisible by 3 are:
    (4, 2, 3) with a sum of 4 + 2 + 3 = 9.
    (2, 3, 1) with a sum of 2 + 3 + 1 = 6.
    Thus, the answer is 9.
Example 2:
    Input: nums = [2,1,5]
    Output: 0
    Explanation:
    No triplet forms a sum divisible by 3, so the answer is 0.

Constraints:
    1. 3 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
'''
# === 171ms && 28.75MB === #
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        s = defaultdict(list)
        for num in nums:
            s[num%3].append(num)
        ans = 0
        for i in range(3):
            s[i] = sorted(s[i])
            if len(s[i]) >= 3:
                ans = max(ans, sum(s[i][-3:]))
        if all(len(s[i]) > 0 for i in range(3)):
            ans = max(ans, sum([s[i][-1] for i in range(3)]))
        return ans