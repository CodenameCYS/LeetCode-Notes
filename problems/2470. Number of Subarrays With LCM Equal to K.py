'''
=== 2470. Number of Subarrays With LCM Equal to K ===

Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.
A subarray is a contiguous non-empty sequence of elements within an array.
The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.

Example 1:
    Input: nums = [3,6,2,7,1], k = 6
    Output: 4
    Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
    - [3,6,2,7,1]
    - [3,6,2,7,1]
    - [3,6,2,7,1]
    - [3,6,2,7,1]
Example 2:
    Input: nums = [3], k = 2
    Output: 0
    Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.
 
Constraints:
    1. 1 <= nums.length <= 1000
    2. 1 <= nums[i], k <= 1000
'''
# === 468ms && 14MB === #
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        s = 1
        for i in range(n):
            s = 1
            for j in range(i, n):
                if k % nums[j] != 0:
                    break
                s = math.lcm(s, nums[j])
                if s == k:
                    res += 1
        return res
            