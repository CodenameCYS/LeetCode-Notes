'''
=== 3346. Maximum Frequency of an Element After Performing Operations I ===

You are given an integer array nums and two integers k and numOperations.
You must perform an operation numOperations times on nums, where in each operation you:
    - Select an index i that was not selected in any previous operations.
    - Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.
The frequency of an element x is the number of times it occurs in the array.

Example 1:
    Input: nums = [1,4,5], k = 1, numOperations = 2
    Output: 2
    Explanation:
    We can achieve a maximum frequency of two by:
    Adding 0 to nums[1]. nums becomes [1, 4, 5].
    Adding -1 to nums[2]. nums becomes [1, 4, 4].
Example 2:
    Input: nums = [5,11,20,20], k = 5, numOperations = 1
    Output: 2
    Explanation:
    We can achieve a maximum frequency of two by:
    Adding 0 to nums[1].

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
    3. 0 <= k <= 105
    4. 0 <= numOperations <= nums.length
'''
# === 878ms && 47.2MB === #
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)
        nums = sorted(nums)
        
        @lru_cache(None)
        def count(num):
            left = bisect.bisect_left(nums, num-k)
            right = bisect.bisect_right(nums, num+k)
            return min(right-left-cnt[num], numOperations) + cnt[num]
        
        ans = 1
        for num in nums:
            ans = max(ans, count(num-k), count(num), count(num+k))
            
        return ans