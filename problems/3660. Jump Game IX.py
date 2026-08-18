'''
=== 3660. Jump Game IX ===

You are given an integer array nums.
From any index i, you can jump to another index j under the following rules:
    - Jump to index j where j > i is allowed only if nums[j] < nums[i].
    - Jump to index j where j < i is allowed only if nums[j] > nums[i].
For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.
Return an array ans where ans[i] is the maximum value reachable starting from index i.

Example 1:
    Input: nums = [2,1,3]
    Output: [2,2,3]
    Explanation:
    For i = 0: No jump increases the value.
    For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
    For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
    Thus, ans = [2, 2, 3].
Example 2:
    Input: nums = [2,3,1]
    Output: [3,3,3]
    Explanation:
    For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
    For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
    For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.
    Thus, ans = [3, 3, 3].

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
'''
# === 6407ms && 51.25MB === #
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre_max = deepcopy(nums)
        for i in range(n-1):
            pre_max[i+1] = max(pre_max[i+1], pre_max[i])

        pre_index = [i for i in range(n)]
        for i in range(n-1):
            pre_index[i+1] = pre_index[i+1] if nums[pre_index[i+1]] >= nums[pre_index[i]] else pre_index[i]

        elems = [(i, num) for i, num in enumerate(nums)]
        elems = sorted(elems, key=lambda x: (x[1], x[0]))
        post_index = [i for i in range(n)]
        valid = []
        for idx, num in elems:
            bisect.insort(valid, idx)
            post_index[idx] = valid[-1]

        ans = [0 for _ in range(n)]
        for i in range(n):
            idx = i
            while idx != post_index[pre_index[idx]]:
                idx = post_index[pre_index[idx]]
            ans[i] = pre_max[idx]
        return ans

# === 1447ms && 173.40MB === #
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre_max = deepcopy(nums)
        for i in range(n-1):
            pre_max[i+1] = max(pre_max[i+1], pre_max[i])

        pre_index = [i for i in range(n)]
        for i in range(n-1):
            pre_index[i+1] = pre_index[i+1] if nums[pre_index[i+1]] >= nums[pre_index[i]] else pre_index[i]

        elems = [(i, num) for i, num in enumerate(nums)]
        elems = sorted(elems, key=lambda x: (x[1], x[0]))
        post_index = [i for i in range(n)]
        max_idx = -1
        for idx, num in elems:
            max_idx = max(max_idx, idx)
            post_index[idx] = max_idx

        @lru_cache(None)
        def dp(idx):
            if post_index[pre_index[idx]] == idx:
                return idx
            return dp(post_index[pre_index[idx]])

        ans = [dp(i) for i in range(n)]
        return [pre_max[idx] for idx in ans]