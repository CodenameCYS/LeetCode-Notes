'''
=== 2770. Maximum Number of Jumps to Reach the Last Index ===

You are given a 0-indexed array nums of n integers and an integer target.
You are initially positioned at index 0. In one step, you can jump from index i to any index j such that:
    - 0 <= i < j < n
    - -target <= nums[j] - nums[i] <= target
Return the maximum number of jumps you can make to reach index n - 1.
If there is no way to reach index n - 1, return -1.

Example 1:
    Input: nums = [1,3,6,4,1,2], target = 2
    Output: 3
    Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
    - Jump from index 0 to index 1. 
    - Jump from index 1 to index 3.
    - Jump from index 3 to index 5.
    It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 3 jumps. Hence, the answer is 3. 
Example 2:
    Input: nums = [1,3,6,4,1,2], target = 3
    Output: 5
    Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
    - Jump from index 0 to index 1.
    - Jump from index 1 to index 2.
    - Jump from index 2 to index 3.
    - Jump from index 3 to index 4.
    - Jump from index 4 to index 5.
    It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 5 jumps. Hence, the answer is 5. 
Example 3:
    Input: nums = [1,3,6,4,1,2], target = 0
    Output: -1
    Explanation: It can be proven that there is no jumping sequence that goes from 0 to n - 1. Hence, the answer is -1. 
 
Constraints:
    1. 2 <= nums.length == n <= 1000
    2. -109 <= nums[i] <= 109
    3. 0 <= target <= 2 * 109
'''
# === 1073ms && 56.2MB === #
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        reachable = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(nums[i] - nums[j]) <= target:
                    reachable[i].append(j)
        # print(reachable)
        
        @lru_cache(None)
        def dp(idx):
            if idx == n-1:
                return 0
            return max([-math.inf] + [1 + dp(i) for i in reachable[idx]])
                
        res = dp(0)
        return res if res > 0 else -1
                