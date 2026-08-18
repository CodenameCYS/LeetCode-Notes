'''
=== 3795. Minimum Subarray Length With Distinct Sum At Least K ===

You are given an integer array nums and an integer k.
Return the minimum length of a subarray whose sum of the distinct values present in that subarray (each value counted once) is at least k. If no such subarray exists, return -1.

Example 1:
    Input: nums = [2,2,3,1], k = 4
    Output: 2
    Explanation:
    The subarray [2, 3] has distinct elements {2, 3} whose sum is 2 + 3 = 5, which is ​​​​​​​at least k = 4. Thus, the answer is 2.
Example 2:
    Input: nums = [3,2,3,4], k = 5
    Output: 2
    Explanation:
    The subarray [3, 2] has distinct elements {3, 2} whose sum is 3 + 2 = 5, which is ​​​​​​​at least k = 5. Thus, the answer is 2.
Example 3:
    Input: nums = [5,5,4], k = 5
    Output: 1
    Explanation:
    The subarray [5] has distinct elements {5} whose sum is 5, which is at least k = 5. Thus, the answer is 1.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
    3. 1 <= k <= 109
'''
# === 743ms && 37.06MB === #
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        elems, tot = set(), 0
        i, j = 0, 0
        ans = n+1
        while j < n:
            cnt[nums[j]] += 1
            if cnt[nums[j]] == 1:
                elems.add(nums[j])
                tot += nums[j]
            j += 1
            while i < j and tot >= k:
                ans = min(ans, j-i)
                cnt[nums[i]] -= 1
                if cnt[nums[i]] == 0:
                    elems.remove(nums[i])
                    tot -= nums[i]
                i += 1
        return ans if ans <= n else -1
            
