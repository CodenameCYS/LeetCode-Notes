'''
=== 1567. Maximum Length of Subarray With Positive Product ===

Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
Return the maximum length of a subarray with positive product.

Example 1:
    Input: nums = [1,-2,-3,4]
    Output: 4
    Explanation: The array nums already has a positive product of 24.
Example 2:
    Input: nums = [0,1,-2,-3,-4]
    Output: 3
    Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
    Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:
    Input: nums = [-1,-2,-3,0,1]
    Output: 2
    Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
Example 4:
    Input: nums = [-1,2]
    Output: 1
Example 5:
    Input: nums = [1,2,3,5,-6,4,0,10]
    Output: 4
 
Constraints:
    1. 1 <= nums.length <= 10^5
    2. -10^9 <= nums[i] <= 10^9
'''
# === 640ms && 28.1MB === #
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def get_max(cache):
            n = len(cache)
            ans = n-1 - cache[::-1].index(1)
            if -1 in cache:
                st = cache.index(-1)
                ed = n-1 - cache[::-1].index(-1)
                ans = max(ans, ed - st)
            return ans
        
        cache = [1]
        ans = 0
        for n in nums:
            if n > 0:
                cache.append(cache[-1])
            elif n < 0:
                cache.append(-cache[-1])
            else:
                ans = max(ans, get_max(cache))
                # print(cache, ans)
                cache = [1]
        ans = max(ans, get_max(cache))
        return ans