'''
=== 2815. Max Pair Sum in an Array ===

You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the maximum digit in both numbers are equal.
Return the maximum sum or -1 if no such pair exists.

Example 1:
    Input: nums = [51,71,17,24,42]
    Output: 88
    Explanation: 
    For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a pair sum of 71 + 17 = 88. 
    For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a pair sum of 24 + 42 = 66.
    It can be shown that there are no other pairs with equal maximum digits, so the answer is 88.
Example 2:
    Input: nums = [1,2,3,4]
    Output: -1
    Explanation: No pair exists in nums with equal maximum digits.
 
Constraints:
    1. 2 <= nums.length <= 100
    2. 1 <= nums[i] <= 104
'''
# === 122ms && 16.3MB === #
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        def get_max_digit(num):
            res = 0
            while num != 0:
                res = max(res, num % 10)
                num = num // 10
            return res
        
        s = defaultdict(list)
        for num in nums:
            bisect.insort(s[get_max_digit(num)], num)
        # print(s)
        
        res = -1
        for v in s.values():
            if len(v) > 1:
                res = max(res, v[-1] + v[-2])
        return res
        