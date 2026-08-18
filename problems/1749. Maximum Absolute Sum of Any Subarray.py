'''
=== 1749. Maximum Absolute Sum of Any Subarray ===

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.
Note that abs(x) is defined as follows:
    - If x is a negative integer, then abs(x) = -x.
    - If x is a non-negative integer, then abs(x) = x.
 
Example 1:
    Input: nums = [1,-3,2,3,-4]
    Output: 5
    Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:
    Input: nums = [2,-5,1,-4,3,-2]
    Output: 8
    Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. -104 <= nums[i] <= 104
'''
# === 756ms && 28.7MB === #
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = [0] + list(accumulate(nums))
        n = len(s)
        l2r = [0]
        r2l = [0]
        res = 0
        for i in range(1, n):
            while l2r != [] and  l2r[-1] >= s[i]:
                l2r.pop()
            l2r.append(s[i])
            res = max(res, l2r[-1]-l2r[0])
            
            while r2l != [] and  r2l[-1] <= s[i]:
                r2l.pop()
            r2l.append(s[i])
            res = max(res, r2l[0] - r2l[-1])
        return res
        