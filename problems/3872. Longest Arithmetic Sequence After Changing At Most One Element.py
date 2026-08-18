'''
=== 3872. Longest Arithmetic Sequence After Changing At Most One Element ===

You are given an integer array nums.
A subarray is arithmetic if the difference between consecutive elements in the subarray is constant.
You can replace at most one element in nums with any integer. Then, you select an arithmetic subarray from nums.
Return an integer denoting the maximum length of the arithmetic subarray you can select.

Example 1:
    Input: nums = [9,7,5,10,1]
    Output: 5
    Explanation:
    Replace nums[3] = 10 with 3. The array becomes [9, 7, 5, 3, 1].
    Select the subarray [9, 7, 5, 3, 1], which is arithmetic because consecutive elements have a common difference of -2.
Example 2:
    Input: nums = [1,2,6,7]
    Output: 3
    Explanation:
    Replace nums[0] = 1 with -2. The array becomes [-2, 2, 6, 7].
    Select the subarray [-2, 2, 6, 7], which is arithmetic because consecutive elements have a common difference of 4.
 
Constraints:
    1. 4 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
'''
# === 1329ms && 38.96MB === #
class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        l2r = [2 for _ in nums]
        r2l = [2 for _ in nums]
        r2l[0] = 1
        l2r[-1] = 1
        for i in range(n-2):
            if nums[i+1]-nums[i] == nums[i+2]-nums[i+1]:
                r2l[i+2] = r2l[i+1]+1
            if nums[n-1-i]-nums[n-2-i] == nums[n-2-i]-nums[n-3-i]:
                l2r[n-3-i]=l2r[n-2-i]+1
        ans = 0
        for i in range(n):
            if i == 0:
                ans = max(ans, l2r[i+1]+1)
            elif i == n-1:
                ans = max(ans, r2l[i-1]+1)
            elif i == 1:
                if nums[2] - nums[0] == 2 * (nums[3]-nums[2]):
                    ans = max(ans, 2 + l2r[i+1])
                else:
                    ans = max(ans, 1 + l2r[i+1])
            elif i == n-2:
                if nums[-1] - nums[-3] == 2 * (nums[-3]-nums[-4]):
                    ans = max(ans, 2 + r2l[i-1])
                else:
                    ans = max(ans, 1 + r2l[i-1])
            elif nums[i-1]-nums[i-2] == nums[i+2]-nums[i+1]:
                if nums[i+1]-nums[i-1] == 2 * (nums[i+2]-nums[i+1]):
                    ans = max(ans, 1 + l2r[i+1] + r2l[i-1])
                else:
                    ans = max(ans, 1 + l2r[i+1], 1 + r2l[i-1])
            elif nums[i+1]-nums[i-1] == 2 * (nums[i+2]-nums[i+1]):
                ans = max(ans, 2 + l2r[i+1], 1 + r2l[i-1])
            elif nums[i+1]-nums[i-1] == 2 * (nums[i-1]-nums[i-2]):
                ans = max(ans, 1 + l2r[i+1], 2 + r2l[i-1])
            else:
                ans = max(ans, 1 + l2r[i+1], 1 + r2l[i-1])
        return ans