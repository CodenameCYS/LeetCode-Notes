'''
=== 2750. Ways to Split Array Into Good Subarrays ===

You are given a binary array nums.
A subarray of an array is good if it contains exactly one element with the value 1.
Return an integer denoting the number of ways to split the array nums into good subarrays. As the number may be too large, return it modulo 109 + 7.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [0,1,0,0,1]
    Output: 3
    Explanation: There are 3 ways to split nums into good subarrays:
    - [0,1] [0,0,1]
    - [0,1,0] [0,1]
    - [0,1,0,0] [1]
Example 2:
    Input: nums = [0,1,0]
    Output: 1
    Explanation: There is 1 way to split nums into good subarrays:
    - [0,1,0]
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i] <= 1
'''
# === 2321ms && 22.1MB === #
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9+7
        
        if 1 not in nums:
            return 0
        res = 1
        ones = [i for i, x in enumerate(nums) if x == 1]
        n = len(ones)
        for i in range(n-1):
            res = res * (ones[i+1] - ones[i]) % MOD
        return res
        
        