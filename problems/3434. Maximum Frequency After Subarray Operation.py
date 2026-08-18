'''
=== 3434. Maximum Frequency After Subarray Operation ===

You are given an array nums of length n. You are also given an integer k.
You perform the following operation on nums once:
    - Select a subarray nums[i..j] where 0 <= i <= j <= n - 1.
    - Select an integer x and add x to all the elements in nums[i..j].
Find the maximum frequency of the value k after the operation.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,2,3,4,5,6], k = 1
    Output: 2
    Explanation:
    After adding -5 to nums[2..5], 1 has a frequency of 2 in [1, 2, -2, -1, 0, 1].
Example 2:
    Input: nums = [10,2,3,4,5,5,4,3,2,2], k = 10
    Output: 4
    Explanation:
    After adding 8 to nums[1..9], 10 has a frequency of 4 in [10, 10, 11, 12, 13, 13, 12, 11, 10, 10].

Constraints:
    1. 1 <= n == nums.length <= 105
    2. 1 <= nums[i] <= 50
    3. 1 <= k <= 50
'''
# === 5715ms && 21.7MB === #
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)[k]
        ans = cnt
        
        for t in range(1, 51):
            if t == k:
                continue
            pre_min, delta, max_delta = 0, 0, 0
            for x in nums:
                if x == k:
                    delta -= 1
                elif x == t:
                    delta += 1
                max_delta = max(delta - pre_min, max_delta)
                pre_min = min(delta, pre_min)
            ans = max(ans, cnt+max_delta)
            
        return ans