'''
=== 3428. Maximum and Minimum Sums of at Most Size K Subsequences ===

You are given an integer array nums and a positive integer k. Return the sum of the maximum and minimum elements of all subsequences of nums with at most k elements.
A non-empty subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: nums = [1,2,3], k = 2
    Output: 24
    Explanation:
    The subsequences of nums with at most 2 elements are:
    Subsequence	Minimum	Maximum	Sum
    [1]	1	1	2
    [2]	2	2	4
    [3]	3	3	6
    [1, 2]	1	2	3
    [1, 3]	1	3	4
    [2, 3]	2	3	5
    Final Total	 	 	24
    The output would be 24.
Example 2:
    Input: nums = [5,0,6], k = 1
    Output: 22
    Explanation:
    For subsequences with exactly 1 element, the minimum and maximum values are the element itself. Therefore, the total is 5 + 5 + 0 + 0 + 6 + 6 = 22.
Example 3:
    Input: nums = [1,1,1], k = 2
    Output: 12
    Explanation:
    The subsequences [1, 1] and [1] each appear 3 times. For all of them, the minimum and maximum are both 1. Thus, the total is 12.

Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i] <= 109
    3. 1 <= k <= min(100, nums.length)
'''
MOD = 10**9+7

Factorials = [1 for _ in range(10**5+1)]
Revs = [1 for _ in range(10**5+1)]
for i in range(2, 10**5+1):
    Factorials[i] = (i * Factorials[i-1]) % MOD
    Revs[i] = pow(Factorials[i], -1, mod=MOD)

def C(n, m):
    return (Factorials[n] * Revs[n-m] * Revs[m]) % MOD if n >= m else 0

# === 8359ms && 37.6MB === #
class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        
        ans = 0
        for i, x in enumerate(nums):
            for m in range(1, k+1):
                ans = (ans + x * (C(i, m-1) + C(n-1-i, m-1))) % MOD
        return ans
        
            