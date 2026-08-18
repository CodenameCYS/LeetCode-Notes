'''
=== 2195. Append K Integers With Minimal Sum ===

You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.
Return the sum of the k integers appended to nums.

Example 1:
    Input: nums = [1,4,25,10,25], k = 2
    Output: 5
    Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
    The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
    The sum of the two integers appended is 2 + 3 = 5, so we return 5.
Example 2:
    Input: nums = [5,6], k = 6
    Output: 25
    Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8.
    The resulting sum of nums is 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36, which is the minimum. 
    The sum of the six integers appended is 1 + 2 + 3 + 4 + 7 + 8 = 25, so we return 25.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i], k <= 109
'''
# === 995ms && 28.8MB === #
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        # print(nums)
        pre = 0
        res = 0
        for x in nums:
            if x <= pre+1:
                pre = x
                continue
            elif x > pre + k:
                res += k * (pre+1 + pre+k) // 2
                k = 0
                break
            else:
                t = x - pre - 1
                res += t * (pre+1 + pre+t) // 2
                k -= t
            pre = x
        # print(pre, res, k)
        if k > 0:
            res += k * (pre+1 + pre+k) // 2
            
        return res
                