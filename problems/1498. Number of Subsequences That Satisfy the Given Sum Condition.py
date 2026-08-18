'''
=== 1498. Number of Subsequences That Satisfy the Given Sum Condition ===

Given an array of integers nums and an integer target.
Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal than target.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: nums = [3,5,6,7], target = 9
    Output: 4
    Explanation: There are 4 subsequences that satisfy the condition.
    [3] -> Min value + max value <= target (3 + 3 <= 9)
    [3,5] -> (3 + 5 <= 9)
    [3,5,6] -> (3 + 6 <= 9)
    [3,6] -> (3 + 6 <= 9)
Example 2:
    Input: nums = [3,3,6,8], target = 10
    Output: 6
    Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
    [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:
    Input: nums = [2,3,3,4,6,7], target = 12
    Output: 61
    Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
    Number of valid subsequences (63 - 2 = 61).
Example 4:
    Input: nums = [5,2,4,1,7,6,8], target = 16
    Output: 127
    Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127

Constraints:
    1. 1 <= nums.length <= 10^5
    2. 1 <= nums[i] <= 10^6
    3. 1 <= target <= 10^6
'''
# === 864ms(76.08%) && 25.2MB === #
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 1000000007
        
        nums = sorted(nums)
        n = len(nums)
        
        factor = [1 for i in range(n)]
        for i in range(1, n):
            factor[i] = 2 * factor[i-1] % MOD
        
        # print(n, nums)
        st = 0
        ed = 0
        ans = 0
        while ed < n and nums[st] + nums[ed] <= target:
            ed += 1
        ed -= 1
        if st <= ed:
            ans = (ans + factor[ed-st]) % MOD
        # print(st, ed, ans)
        st += 1
        while st <= ed:
            while st <= ed and nums[st] + nums[ed] > target:
                ed -= 1
            if st <= ed:
                ans = (ans + factor[ed-st]) % MOD
            # print(st, ed, ans)
            st += 1
        return ans