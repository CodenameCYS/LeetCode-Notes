'''
=== 2401. Longest Nice Subarray ===

You are given an array nums consisting of positive integers.
We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
Return the length of the longest nice subarray.
A subarray is a contiguous part of an array.
Note that subarrays of length 1 are always considered nice.

Example 1:
    Input: nums = [1,3,8,48,10]
    Output: 3
    Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
    - 3 AND 8 = 0.
    - 3 AND 48 = 0.
    - 8 AND 48 = 0.
    It can be proven that no longer nice subarray can be obtained, so we return 3.
Example 2:
    Input: nums = [3,1,5,11,13]
    Output: 1
    Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
'''
# === 5171ms && 28.9MB === #
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        digits = [0 for _ in range(32)]
        res = 0
        i, j, n = 0, 0, len(nums)
        while j < n:
            x = nums[j]
            k = 0
            while x != 0:
                digits[k] += x % 2
                x = x // 2
                k += 1
            j += 1
            while i < j and any(d > 1 for d in digits):
                x = nums[i]
                k = 0
                while x != 0:
                    digits[k] -= x % 2
                    x = x // 2
                    k += 1
                i += 1
            res = max(res, j-i)
        return res

# === 766ms && 28.8MB === #
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        s = 0
        res = 0
        i, j, n = 0, 0, len(nums)
        while j < n:
            x = nums[j]
            j += 1
            while i < j and s & x != 0:
                s = s ^ nums[i]
                i += 1
            s = s | x
            res = max(res, j-i)
        return res
                        