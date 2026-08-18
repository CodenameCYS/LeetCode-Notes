'''
=== 3937. Minimum Operations to Make Array Modulo Alternating I ===

You are given an integer array nums and an integer k.
In one operation, you can increase or decrease any element of nums by 1.
An array is called modulo alternating if there exist two distinct integers x and y (0 <= x, y < k) such that:
    - For every even index i, nums[i] % k == x
    - For every odd index i, nums[i] % k == y
Return the minimum number of operations required to make nums modulo alternating.

Example 1:
    Input: nums = [1,4,2,8], k = 3
    Output: 2
    Explanation:
    Let's choose x = 1 for even indices and y = 2 for odd indices.
    Perform the following operations:
    Increment nums[1] = 4 by 1, giving nums = [1, 5, 2, 8].
    Decrement nums[2] = 2 by 1, giving nums = [1, 5, 1, 8].
    Now, for even indices, nums[i] % k = 1, and for odd indices, nums[i] % k = 2.
    Thus, the total number of operations required is 2.
Example 2:
    Input: nums = [1,1,1], k = 3
    Output: 1
    Explanation:
    Incrementing nums[1] by 1 gives nums = [1, 2, 1], which satisfies the condition with x = 1 and y = 2.
    Thus, the total number of operations required is 1.
 
Constraints:
    1. 1 <= nums.length <= 100
    2. 1 <= nums[i] <= 109
    3. 2 <= k <= 100
'''
import numpy as np
# === 5131ms && 31.47MB === #
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums = [x % k for x in nums]
        if len(nums) == 1:
            return 0
        even = sorted([x for x in nums[::2]])
        odd = sorted([x for x in nums[1::2]])
        # print(even, odd)

        def fn(nums, m):
            return sum(min(abs(x-m), abs(m+k-x), abs(x+k-m)) for x in nums)

        # print(fn([0, 6], 0))
        # print([min(abs(x-6), abs(6+k-x)) for x in [0, 6]])

        return min(fn(even, x) + fn(odd, y) for x in range(k) for y in range(k) if x != y)