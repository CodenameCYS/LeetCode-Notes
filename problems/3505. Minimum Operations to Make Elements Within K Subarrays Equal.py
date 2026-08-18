'''
=== 3505. Minimum Operations to Make Elements Within K Subarrays Equal ===

You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):
    - Increase or decrease any element of nums by 1.
Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2
    Output: 8
    Explanation:
    Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
    Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
    Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.
Example 2:
    Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2
    Output: 3
    Explanation:
    Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
    Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.
 
Constraints:
    1. 2 <= nums.length <= 105
    2. -106 <= nums[i] <= 106
    3. 2 <= x <= nums.length
    4. 1 <= k <= 15
    5. 2 <= k * x <= nums.length
'''
# === 4845ms && 194MB === #
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
#         def count_min_op(sub):
#             cumsum = list(accumulate(sub, initial=0))
#             ans = math.inf
#             for i in range(x):
#                 tgt = sub[i]
#                 left = i*tgt-cumsum[i]
#                 right = cumsum[-1] - cumsum[i] - (x-i)*tgt
#                 ans = min(ans, left+right)
#             return ans
        
#         min_ops = [math.inf for i in range(n-x+1)]
#         sub = sorted(nums[:x])
#         min_ops[0] = count_min_op(sub)
#         for i in range(n-x):
#             sub.pop(bisect.bisect_left(sub, nums[i]))
#             bisect.insort(sub, nums[i+x])
#             min_ops[i+1] = count_min_op(sub)
#         print(min_ops)

        # print(nums)
        min_ops = [math.inf for i in range(n-x+1)]
        sub = sorted(nums[:x])
        m = (x+1) // 2
        left, ls = sub[:m], sum(sub[:m])
        right, rs = sub[m:], sum(sub[m:])
        min_ops[0] = (m*2-x) * left[-1]  - ls + rs
        for i in range(n-x):
            # print("before: ", left, ls, right, rs)
            if bisect.bisect_left(left, nums[i]) < m:
                left.pop(bisect.bisect_left(left, nums[i]))
                ls -= nums[i]
            else:
                right.pop(bisect.bisect_left(right, nums[i]))
                rs -= nums[i]
            
            bisect.insort(left, nums[i+x])
            ls += nums[i+x]
            
            while len(left) < m:
                elem = right.pop(0)
                rs -= elem
                bisect.insort(left, elem)
                ls += elem
            while len(left) > m:
                elem = left.pop(-1)
                ls -= elem
                bisect.insort(right, elem)
                rs += elem
            while left[-1] > right[0]:
                l, r = left.pop(-1), right.pop(0)
                bisect.insort(left, r)
                bisect.insort(right, l)
                ls = ls - l + r
                rs = rs - r + l
            min_ops[i+1] = (m*2-x) * left[-1]  - ls + rs
        #     print("after: ", left, ls, right, rs)
        # print(min_ops, left, right, ls, rs)
        # print("=" * 10)
            
        
        @lru_cache(maxsize = 10000)
        def dp(idx, k):
            if k == 0:
                return 0
            if idx >= n:
                return math.inf 
            if idx+k*x > n:
                return math.inf
            elif idx+k*x == n:
                return min_ops[idx] + dp(idx+x, k-1)
            
            return min(dp(idx+1, k), min_ops[idx] + dp(idx+x, k-1))
        
        return dp(0, k)