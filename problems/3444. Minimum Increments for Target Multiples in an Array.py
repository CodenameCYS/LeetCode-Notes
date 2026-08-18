'''
=== 3444. Minimum Increments for Target Multiples in an Array ===

You are given two arrays, nums and target.
In a single operation, you may increment any element of nums by 1.
Return the minimum number of operations required so that each element in target has at least one multiple in nums.

Example 1:
    Input: nums = [1,2,3], target = [4]
    Output: 1
    Explanation:
    The minimum number of operations required to satisfy the condition is 1.
    Increment 3 to 4 with just one operation, making 4 a multiple of itself.
Example 2:
    Input: nums = [8,4], target = [10,5]
    Output: 2
    Explanation:
    The minimum number of operations required to satisfy the condition is 2.
    Increment 8 to 10 with 2 operations, making 10 a multiple of both 5 and 10.
Example 3:
    Input: nums = [7,9,10], target = [7]
    Output: 0
    Explanation:
    Target 7 already has a multiple in nums, so no additional operations are needed.

Constraints:
    1. 1 <= nums.length <= 5 * 104
    2. 1 <= target.length <= 4
    3. target.length <= nums.length
    4. 1 <= nums[i], target[i] <= 104
'''
# === 12ms && 21.3MB === #
class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        nums, target = sorted(nums), sorted(target, reverse=True)
        n, m = len(nums), len(target)
        status = [0 for _ in range(m)]
        ans = math.inf
        # print("=" * 10)
        # print(f"nums = {nums}, target = {target}")
        
        def dfs(idx, nums, status):
            nonlocal ans
            # print(f"dfs({idx}, {nums}, {status})")
            if idx >= m:
                return 0
            elif status[idx] == 1:
                return dfs(idx+1, nums, status)
            need = math.inf
            tgt = 0
            while tgt < nums[-1]:
                tgt += target[idx]
                old_status = deepcopy(status)
                for i, x in enumerate(target):
                    if status[i] == 1 or tgt % x == 0:
                        status[i] = 1
                i = bisect.bisect_right(nums, tgt)
                if i > 0:
                    num = nums.pop(i-1)
                    if abs(num-tgt) < ans:
                        need = min(need, abs(num-tgt) + dfs(idx+1, nums, status))
                    nums.insert(i-1, num)
                status = old_status
                # print(tgt, nums, status, ans, need)
            if need >= ans:
                return math.inf
            if idx == 0:
                ans = need
            return need
        
        dfs(0, nums, status)
        return ans
                