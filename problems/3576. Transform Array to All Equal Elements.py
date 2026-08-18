'''
=== 3576. Transform Array to All Equal Elements ===

You are given an integer array nums of size n containing only 1 and -1, and an integer k.
You can perform the following operation at most k times:
Choose an index i (0 <= i < n - 1), and multiply both nums[i] and nums[i + 1] by -1.
Note that you can choose the same index i more than once in different operations.
Return true if it is possible to make all elements of the array equal after at most k operations, and false otherwise.

Example 1:
    Input: nums = [1,-1,1,-1,1], k = 3
    Output: true
    Explanation:
    We can make all elements in the array equal in 2 operations as follows:
    Choose index i = 1, and multiply both nums[1] and nums[2] by -1. Now nums = [1,1,-1,-1,1].
    Choose index i = 2, and multiply both nums[2] and nums[3] by -1. Now nums = [1,1,1,1,1].
Example 2:
    Input: nums = [-1,-1,-1,1,1,1], k = 5
    Output: false
    Explanation:
    It is not possible to make all array elements equal in at most 5 operations.

Constraints:
    1. 1 <= n == nums.length <= 105
    2. nums[i] is either -1 or 1.
    3. 1 <= k <= n
'''
# === 329ms && 50.1MB === #
class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1:
            return True

        def is_possible(idx, k, tgt, flag):
            if idx == n-2:
                if nums[idx] * flag != nums[-1]:
                    return False
                elif nums[-1] != tgt and k == 0:
                    return False
                return True
            if nums[idx] * flag != tgt:
                if k == 0:
                    return False
                return is_possible(idx+1, k-1, tgt, -1)
            else:
                return is_possible(idx+1, k, tgt, 1)

        return is_possible(0, k, 1, 1) or is_possible(0, k, -1, 1)
