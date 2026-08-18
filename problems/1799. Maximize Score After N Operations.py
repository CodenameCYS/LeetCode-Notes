'''
=== 1799. Maximize Score After N Operations ===

You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.
In the ith operation (1-indexed), you will:
    - Choose two elements, x and y.
    - Receive a score of i * gcd(x, y).
    - Remove x and y from nums.
Return the maximum score you can receive after performing n operations.
The function gcd(x, y) is the greatest common divisor of x and y.

Example 1:
    Input: nums = [1,2]
    Output: 1
    Explanation: The optimal choice of operations is:
    (1 * gcd(1, 2)) = 1
Example 2:
    Input: nums = [3,4,6,8]
    Output: 11
    Explanation: The optimal choice of operations is:
    (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:
    Input: nums = [1,2,3,4,5,6]
    Output: 14
    Explanation: The optimal choice of operations is:
    (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 
Constraints:
    1. 1 <= n <= 7
    2. nums.length == 2 * n
    3. 1 <= nums[i] <= 106
'''
# === 3860ms && 100MB === #
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        cache = []
        for i in range(n-1):
            for j in range(i+1, n):
                cache.append((gcd(nums[i], nums[j]), i, j))
        cache = sorted(cache, reverse=True)
        m = len(cache)
        
        @lru_cache(None)
        def dp(idx, ops, status):
            if ops == 0:
                return 0
            if idx >= m:
                return -math.inf
            res = 0
            for i in range(idx, m):
                g, x, y = cache[i]
                if (1 << x) & status or (1 << y) & status:
                    continue
                res = max(res, ops * g + dp(i+1, ops-1, status ^ (1<<x) ^ (1<<y)))
            return res
        
        return dp(0, n//2, 0)