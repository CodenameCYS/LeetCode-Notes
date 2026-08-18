'''
=== 3892. Minimum Operations to Achieve At Least K Peaks ===

You are given a ​​​​​​​circular integer array​​​​​​​ nums of length n.
An index i is a peak if its value is strictly greater than its neighbors:
    - The previous neighbor of i is nums[i - 1] if i > 0, otherwise nums[n - 1].
    - The next neighbor of i is nums[i + 1] if i < n - 1, otherwise nums[0].
You are allowed to perform the following operation any number of times:
    - Choose any index i and increase nums[i] by 1.
Return an integer denoting the minimum number of operations required to make the array contain at least k peaks. If it is impossible, return -1.

Example 1:
    Input: nums = [2,1,2], k = 1
    Output: 1
    Explanation:
    To achieve at least k = 1 peak, we can increase nums[2] = 2 to 3.
    After this operation, nums[2] = 3 is strictly greater than its neighbors nums[0] = 2 and nums[1] = 1.
    Therefore, the minimum number of operations required is 1.
Example 2:
    Input: nums = [4,5,3,6], k = 2
    Output: 0
    Explanation:
    The array already contains at least k = 2 peaks with zero operations.
    Index 1: nums[1] = 5 is strictly greater than its neighbors nums[0] = 4 and nums[2] = 3.
    Index 3: nums[3] = 6 is strictly greater than its neighbors nums[2] = 3 and nums[0] = 4.
    Therefore, the minimum number of operations required is 0.
Example 3:
    Input: nums = [3,7,3], k = 2
    Output: -1
    Explanation:
    It is impossible to have at least k = 2 peaks in this array. Therefore, the answer is -1.

Constraints:
    1. 2 <= n == nums.length <= 5000
    2. -105 <= nums[i] <= 105
    3. 0 <= k <= n​​​​​​​
'''
# === 8455ms && 396.65MB === #
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums = nums + nums[:2]
        
        @lru_cache(maxsize=10**5)
        def dp(idx, k, allow_change):
            if k == 0:
                return 0
            if allow_change and idx >= n:
                return math.inf
            elif not allow_change and idx >= n-1:
                return math.inf
            
            m = (n-idx+1)//2 if allow_change else (n-idx)//2
            if m < k:
                return math.inf
            
            if idx == 0:
                return min(
                    dp(idx+1, k, True),
                    max(0, max(nums[idx], nums[idx+2]) + 1 - nums[idx+1]) + dp(idx+2, k-1, False)
                )
            else:
                return min(
                    dp(idx+1, k, allow_change),
                    max(0, max(nums[idx], nums[idx+2]) + 1 - nums[idx+1]) + dp(idx+2, k-1, allow_change)
                )

        ans = dp(0, k, True) 
        return ans if ans != math.inf else -1
