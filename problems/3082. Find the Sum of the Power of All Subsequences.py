'''
=== 3082. Find the Sum of the Power of All Subsequences ===

You are given an integer array nums of length n and a positive integer k.
The power of an array of integers is defined as the number of subsequences with their sum equal to k.
Return the sum of power of all subsequences of nums.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input:  nums = [1,2,3], k = 3 
    Output:  6 
    Explanation:
    There are 5 subsequences of nums with non-zero power:
    - The subsequence [1,2,3] has 2 subsequences with sum == 3: [1,2,3] and [1,2,3].
    - The subsequence [1,2,3] has 1 subsequence with sum == 3: [1,2,3].
    - The subsequence [1,2,3] has 1 subsequence with sum == 3: [1,2,3].
    - The subsequence [1,2,3] has 1 subsequence with sum == 3: [1,2,3].
    - The subsequence [1,2,3] has 1 subsequence with sum == 3: [1,2,3].
    Hence the answer is 2 + 1 + 1 + 1 + 1 = 6.
Example 2:
    Input:  nums = [2,3,3], k = 5 
    Output:  4 
    Explanation:
    There are 3 subsequences of nums with non-zero power:
    - The subsequence [2,3,3] has 2 subsequences with sum == 5: [2,3,3] and [2,3,3].
    - The subsequence [2,3,3] has 1 subsequence with sum == 5: [2,3,3].
    - The subsequence [2,3,3] has 1 subsequence with sum == 5: [2,3,3].
    Hence the answer is 2 + 1 + 1 = 4.
Example 3:
    Input:  nums = [1,2,3], k = 7 
    Output:  0 
    Explanation: There exists no subsequence with sum 7. Hence all subsequences of nums have power = 0.

Constraints:
    1. 1 <= n <= 100
    2. 1 <= nums[i] <= 104
    3. 1 <= k <= 100
'''
MOD = 10**9 + 7
FACTS = [1]
for _ in range(100):
    FACTS.append(FACTS[-1] * 2 % MOD)
    
# === 387ms && 122.8MB === #    
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dp(idx, cnt, remain):
            if remain == 0:
                return FACTS[n-cnt]
            elif idx >= n:
                return 0
            elif nums[idx] > remain:
                return dp(idx+1, cnt, remain) % MOD
            else:
                return (dp(idx+1, cnt, remain) + dp(idx+1, cnt+1, remain-nums[idx])) % MOD
        
        return dp(0, 0, k) 
            