'''
=== 3830. Longest Alternating Subarray After Removing At Most One Element ===

You are given an integer array nums.
A subarray nums[l..r] is alternating if one of the following holds:
    - nums[l] < nums[l + 1] > nums[l + 2] < nums[l + 3] > ...
    - nums[l] > nums[l + 1] < nums[l + 2] > nums[l + 3] < ...
In other words, if we compare adjacent elements in the subarray, then the comparisons alternate between strictly greater and strictly smaller.
You can remove at most one element from nums. Then, you select an alternating subarray from nums.
Return an integer denoting the maximum length of the alternating subarray you can select.
A subarray of length 1 is considered alternating.

Example 1:
    Input: nums = [2,1,3,2]
    Output: 4
    Explanation:
    Choose not to remove elements.
    Select the entire array [2, 1, 3, 2], which is alternating because 2 > 1 < 3 > 2.
Example 2:
    Input: nums = [3,2,1,2,3,2,1]
    Output: 4
    Explanation:
    Choose to remove nums[3] i.e., [3, 2, 1, 2, 3, 2, 1]. The array becomes [3, 2, 1, 3, 2, 1].
    Select the subarray [3, 2, 1, 3, 2, 1].
Example 3:
    Input: nums = [100000,100000]
    Output: 1
    Explanation:
    Choose not to remove elements.
    Select the subarray [100000, 100000].
 
Constraints:
    1. 2 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
'''
# === 1065ms && 39.26MB === #
class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        l2ra = [1 for _ in range(n)] # left to right, start with ↘
        l2rb = [1 for _ in range(n)] # left to right, start with ↗
        r2la = [1 for _ in range(n)] # right to left, start with ↙
        r2lb = [1 for _ in range(n)] # right to left, start with ↖
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                l2ra[i] = l2rb[i+1] + 1
            elif nums[i] < nums[i+1]:
                l2rb[i] = l2ra[i+1] + 1
        
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                r2la[i+1] = r2lb[i] + 1
            elif nums[i+1] < nums[i]:
                r2lb[i+1] = r2la[i] + 1

        ans = 0
        for i in range(n):
            ans = max(ans, max(r2la[i] + l2ra[i], r2lb[i] + l2rb[i]) - 1)
            if i != 0 and i != n-1:
                if nums[i-1] > nums[i+1]:
                    ans = max(ans, r2la[i-1] + l2rb[i+1])
                elif nums[i-1] < nums[i+1]:
                    ans = max(ans, r2lb[i-1] + l2ra[i+1])
        return ans