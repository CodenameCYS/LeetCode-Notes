'''
=== 1802. Maximum Value at a Given Index in a Bounded Array ===

You are given three positive integers n, index and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:
    - nums.length == n
    - nums[i] is a positive integer where 0 <= i < n.
    - abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
    - The sum of all the elements of nums does not exceed maxSum.
    - nums[index] is maximized.
Return nums[index] of the constructed array.
Note that abs(x) equals x if x >= 0, and -x otherwise.

Example 1:
    Input: n = 4, index = 2,  maxSum = 6
    Output: 2
    Explanation: The arrays [1,1,2,1] and [1,2,2,1] satisfy all the conditions. There are no other valid arrays with a larger value at the given index.
Example 2:
    Input: n = 6, index = 1,  maxSum = 10
    Output: 3
 
Constraints:
    1. 1 <= n <= maxSum <= 109
    2. 0 <= index < n
'''
# === 32ms && 14.2MB === #
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def fn(k):
            res = k
            left = index
            if k-left > 0:
                res += (k-1+k-left)*left // 2
            else:
                res += (left-k+1) + k*(k-1) // 2
            right = n-1-index
            if k-right > 0:
                res += (k-1+k-right)*right // 2
            else:
                res += (right-k+1) + k*(k-1) // 2
            return res
            
        l, r = 1, maxSum+1
        while l < r-1:
            m = (l+r) // 2
            s = fn(m)
            # print(m, s)
            if s == maxSum:
                # print("=" * 20)
                return m
            elif s < maxSum:
                l = m
            else:
                r = m
        # print("=" * 20)
        return l
            