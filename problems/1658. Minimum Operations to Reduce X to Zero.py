'''
=== 1658. Minimum Operations to Reduce X to Zero ===

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

Example 1:
    Input: nums = [1,1,4,2,3], x = 5
    Output: 2
    Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:
    Input: nums = [5,6,7,8,9], x = 4
    Output: -1
Example 3:
    Input: nums = [3,2,20,1,1,3], x = 10
    Output: 5
    Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 104
    3. 1 <= x <= 109
'''
import math
# === 1164ms && 28.9MB === #
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        tot = sum(nums)
        if tot < x:
            return -1
        elif tot == x:
            return len(nums)
        
        n = len(nums)
        l, r = 0, n-1
        s = 0
        used = 0
        while s < x:
            s += nums[r]
            r -= 1
            used += 1
        res = -1 if s != x else used
        while r < n-1 and l <= r :
            used -= 1
            r += 1
            s -= nums[r]
            while s < x and l <= r:
                s += nums[l]
                l += 1
                used += 1
            if s == x:
                res = used if res == -1 else min(res, used)
        return res
            