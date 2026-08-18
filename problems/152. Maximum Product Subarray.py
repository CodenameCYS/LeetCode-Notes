'''
=== 152. Maximum Product Subarray ===

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
Example 2:
    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
# === 52ms(91.37%) && 14.8MB(16.60%) === #
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        pos = [1]
        neg = []
        last = 1
        for n in nums:
            if n == 0:
                if len(pos) > 1:
                    ans = max(ans, pos[-1])
                if len(neg) >= 2:
                    ans = max(ans, neg[-1] // neg[0])
                pos = [1]
                neg = []
                last = 1
            else:
                last = last * n
                if last > 0:
                    pos.append(last)
                else:
                    neg.append(last)
        if len(pos) > 1:
            ans = max(ans, pos[-1])
        if len(neg) >= 2:
            ans = max(ans, neg[-1] // neg[0])
        return ans
        