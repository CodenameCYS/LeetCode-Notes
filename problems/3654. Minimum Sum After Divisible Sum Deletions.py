'''
=== 3654. Minimum Sum After Divisible Sum Deletions ===

You are given an integer array nums and an integer k.
You may repeatedly choose any contiguous subarray of nums whose sum is divisible by k and delete it; after each deletion, the remaining elements close the gap.
Return the minimum possible sum of nums after performing any number of such deletions.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 1
    Explanation:
    Delete the subarray nums[0..1] = [1, 1], whose sum is 2 (divisible by 2), leaving [1].
    The remaining sum is 1.
Example 2:
    Input: nums = [3,1,4,1,5], k = 3
    Output: 5
    Explanation:
    First, delete nums[1..3] = [1, 4, 1], whose sum is 6 (divisible by 3), leaving [3, 5].
    Then, delete nums[0..0] = [3], whose sum is 3 (divisible by 3), leaving [5].
    The remaining sum is 5.​​​​​​​
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 106
    3. 1 <= k <= 105
'''
# === 1989ms && 149.33MB === #
class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(nums)
        remains = [0 for _ in range(n+1)]
        boundries = defaultdict(list)
        boundries[0].append(0)
        for i in range(n):
            remains[i+1] = (remains[i] + nums[i]) % k
            boundries[remains[i+1]].append(i+1)
        if len(boundries) == 1:
            return 0
        
        @lru_cache(None)
        def dp(idx):
            if idx >= n:
                return 0
            ans = math.inf
            j = bisect.bisect_right(boundries[remains[idx]], idx)
            for r in boundries[remains[idx]][j:][::-1]:
                ans = min(ans, dp(r))
                if ans == 0:
                    return ans
            if ans > nums[idx]:
                ans = min(ans, nums[idx] + dp(idx+1))
            return ans

        return dp(0)

# === 1677ms && 158.82MB === #   
class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(nums)
        remains = [0 for _ in range(n+1)]
        boundries = defaultdict(list)
        boundries[0].append(0)
        for i in range(n):
            remains[i+1] = (remains[i] + nums[i]) % k
            boundries[remains[i+1]].append(i+1)
        if len(boundries) == 1:
            return 0
        
        @lru_cache(None)
        def dp(idx):
            if idx >= n:
                return 0
            ans = math.inf
            j = bisect.bisect_right(boundries[remains[idx]], idx)
            if j < len(boundries[remains[idx]]):
                ans = min(ans, dp(boundries[remains[idx]][j]))
                if ans == 0:
                    return ans
            if ans > nums[idx]:
                ans = min(ans, nums[idx] + dp(idx+1))
            return ans

        return dp(0)
            