'''
=== 2537. Count the Number of Good Subarrays ===

Given an integer array nums and an integer k, return the number of good subarrays of nums.
A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,1,1,1,1], k = 10
    Output: 1
    Explanation: The only good subarray is the array nums itself.
Example 2:
    Input: nums = [3,1,4,3,2,2,4], k = 2
    Output: 4
    Explanation: There are 4 different good subarrays:
    - [3,1,4,3,2,2] that has 2 pairs.
    - [3,1,4,3,2,2,4] that has 3 pairs.
    - [1,4,3,2,2,4] that has 2 pairs.
    - [4,3,2,2,4] that has 2 pairs.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i], k <= 109
'''
# === 983ms && 31.8MB === #
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i, j, t = 0, 0, 0
        cnt = defaultdict(int)
        res = 0
        while i < n:
            while j < n and t < k:
                t -= cnt[nums[j]] * (cnt[nums[j]] - 1) // 2
                cnt[nums[j]] += 1
                t += cnt[nums[j]] * (cnt[nums[j]] - 1) // 2
                j += 1
            if t >= k:
                res += (n-j+1)
                t -= cnt[nums[i]] * (cnt[nums[i]] - 1) // 2
                cnt[nums[i]] -= 1
                t += cnt[nums[i]] * (cnt[nums[i]] - 1) // 2
                i += 1
            else:
                break
        return res
        
                
                
                