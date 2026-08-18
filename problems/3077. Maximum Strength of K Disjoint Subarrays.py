'''
=== 3077. Maximum Strength of K Disjoint Subarrays ===

You are given a 0-indexed array of integers nums of length n, and a positive odd integer k.
The strength of x subarrays is defined as strength = sum[1] * x - sum[2] * (x - 1) + sum[3] * (x - 2) - sum[4] * (x - 3) + ... + sum[x] * 1 where sum[i] is the sum of the elements in the ith subarray. Formally, strength is sum of (-1)i+1 * sum[i] * (x - i + 1) over all i's such that 1 <= i <= x.
You need to select k disjoint subarrays from nums, such that their strength is maximum.
Return the maximum possible strength that can be obtained.
Note that the selected subarrays don't need to cover the entire array.

Example 1:
    Input: nums = [1,2,3,-1,2], k = 3
    Output: 22
    Explanation: The best possible way to select 3 subarrays is: nums[0..2], nums[3..3], and nums[4..4]. The strength is (1 + 2 + 3) * 3 - (-1) * 2 + 2 * 1 = 22.
Example 2:
    Input: nums = [12,-2,-2,-2,-2], k = 5
    Output: 64
    Explanation: The only possible way to select 5 disjoint subarrays is: nums[0..0], nums[1..1], nums[2..2], nums[3..3], and nums[4..4]. The strength is 12 * 5 - (-2) * 4 + (-2) * 3 - (-2) * 2 + (-2) * 1 = 64.
Example 3:
    Input: nums = [-1,-2,-3], k = 1
    Output: -1
    Explanation: The best possible way to select 1 subarray is: nums[0..0]. The strength is -1.
 
Constraints:
    1. 1 <= n <= 104
    2. -109 <= nums[i] <= 109
    3. 1 <= k <= n
    4. 1 <= n * k <= 106
    5. k is odd.
'''
# === 2386ms && 18MB === #
class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        factors = [(k-i)*(-1)**(i%2) for i in range(k)]
        
        # dp0 stand for consecutive and dp1 for inconsecutive
        dp0 = [-math.inf for _ in range(k)]
        dp1 = [-math.inf for _ in range(k)]
        
        for num in nums:
            # s[i] stand for max result including num in ith subarray
            s = [-math.inf for _ in range(k)]
            s[0] = num * factors[0] + max(0, dp0[0])
            
            for i in range(1, k):
                s[i] = num * factors[i] + max(dp0[i], dp1[i-1])
            
            for i in range(k):
                dp1[i] = max(dp1[i], s[i])
                
            dp0 = s
        
        return dp1[-1]