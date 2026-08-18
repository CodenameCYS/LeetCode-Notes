'''
=== 3049. Earliest Second to Mark Indices II ===

You are given two 1-indexed integer arrays, nums and, changeIndices, having lengths n and m, respectively.
Initially, all indices in nums are unmarked. Your task is to mark all indices in nums.
In each second, s, in order from 1 to m (inclusive), you can perform one of the following operations:
    - Choose an index i in the range [1, n] and decrement nums[i] by 1.
    - Set nums[changeIndices[s]] to any non-negative value.
    - Choose an index i in the range [1, n], where nums[i] is equal to 0, and mark index i.
    - Do nothing.
Return an integer denoting the earliest second in the range [1, m] when all indices in nums can be marked by choosing operations optimally, or -1 if it is impossible.

Example 1:
    Input: nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]
    Output: 6
    Explanation: In this example, we have 7 seconds. The following operations can be performed to mark all indices:
    Second 1: Set nums[changeIndices[1]] to 0. nums becomes [0,2,3].
    Second 2: Set nums[changeIndices[2]] to 0. nums becomes [0,2,0].
    Second 3: Set nums[changeIndices[3]] to 0. nums becomes [0,0,0].
    Second 4: Mark index 1, since nums[1] is equal to 0.
    Second 5: Mark index 2, since nums[2] is equal to 0.
    Second 6: Mark index 3, since nums[3] is equal to 0.
    Now all indices have been marked.
    It can be shown that it is not possible to mark all indices earlier than the 6th second.
    Hence, the answer is 6.
Example 2:
    Input: nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2]
    Output: 7
    Explanation: In this example, we have 8 seconds. The following operations can be performed to mark all indices:
    Second 1: Mark index 1, since nums[1] is equal to 0.
    Second 2: Mark index 2, since nums[2] is equal to 0.
    Second 3: Decrement index 4 by one. nums becomes [0,0,1,1].
    Second 4: Decrement index 4 by one. nums becomes [0,0,1,0].
    Second 5: Decrement index 3 by one. nums becomes [0,0,0,0].
    Second 6: Mark index 3, since nums[3] is equal to 0.
    Second 7: Mark index 4, since nums[4] is equal to 0.
    Now all indices have been marked.
    It can be shown that it is not possible to mark all indices earlier than the 7th second.
    Hence, the answer is 7.
Example 3:
    Input: nums = [1,2,3], changeIndices = [1,2,3]
    Output: -1
    Explanation: In this example, it can be shown that it is impossible to mark all indices, as we don't have enough seconds. 
    Hence, the answer is -1.
 
Constraints:
    1. 1 <= n == nums.length <= 5000
    2. 0 <= nums[i] <= 109
    3. 1 <= m == changeIndices.length <= 5000
    4. 1 <= changeIndices[i] <= n
'''
# === 1219ms && 288.9MB === #
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        changeIndices = [x-1 for x in changeIndices]
        needed = sum(nums) + n
        first_seen = {}
        for i, x in enumerate(changeIndices):
            if x not in first_seen and nums[x] > 1:
                first_seen[x] = i
        first_seen = {v:k for k, v in first_seen.items()}
        # print(n, m, first_seen)
        
        @lru_cache(None)
        def dp(idx, need, extra):
            if need <= 1 and extra <= 1:
                return idx
            elif idx >= m:
                return m
            if idx not in first_seen:
                return dp(idx+1, need-1, max(extra-1, 0))
            i = first_seen[idx]
            if nums[i] >= 100:
                return dp(idx+1, need-nums[i], extra+1)
            else:
                return min(dp(idx+1, need-1, max(extra-1, 0)), dp(idx+1, need-nums[i], extra+1))
            
        ans = dp(0, needed, 0)
        return ans+1 if ans != m else -1