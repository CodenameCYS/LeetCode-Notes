'''
=== 3637. Trionic Array I ===

You are given an integer array nums of length n.
An array is trionic if there exist indices 0 < p < q < n − 1 such that:
    - nums[0...p] is strictly increasing,
    - nums[p...q] is strictly decreasing,
    - nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.

Example 1:
    Input: nums = [1,3,5,4,2,6]
    Output: true
    Explanation:
    Pick p = 2, q = 4:
    nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
    nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
    nums[4...5] = [2, 6] is strictly increasing (2 < 6).
Example 2:
    Input: nums = [2,1,3]
    Output: false
    Explanation:
    There is no way to pick p and q to form the required three segments.

Constraints:
    1. 3 <= n <= 100
    2. -1000 <= nums[i] <= 1000
'''
# === 0ms && 18.01MB === #
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        stage = 0
        pre, cnt = -math.inf, 0
        for num in nums:
            if stage == 0:
                if num > pre:
                    cnt += 1
                    pre = num
                elif num == pre:
                    return False
                elif cnt > 1:
                    stage = 1
                    cnt = 2
                    pre = num
                else:
                    return False
            elif stage == 1:
                if num < pre:
                    cnt += 1
                    pre = num
                elif num == pre:
                    return False
                else:
                    stage = 2
                    cnt = 2
                    pre = num
            else:
                if num > pre:
                    cnt += 1
                    pre = num
                else:
                    return False
        return stage == 2
