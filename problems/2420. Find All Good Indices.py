'''
=== 2420. Find All Good Indices ===

You are given a 0-indexed integer array nums of size n and a positive integer k.
We call an index i in the range k <= i < n - k good if the following conditions are satisfied:
    - The k elements that are just before the index i are in non-increasing order.
    - The k elements that are just after the index i are in non-decreasing order.
Return an array of all good indices sorted in increasing order.

Example 1:
    Input: nums = [2,1,1,1,3,4,1], k = 2
    Output: [2,3]
    Explanation: There are two good indices in the array:
    - Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in non-decreasing order.
    - Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in non-decreasing order.
    Note that the index 4 is not good because [4,1] is not non-decreasing.
Example 2:
    Input: nums = [2,1,1,2], k = 2
    Output: []
    Explanation: There are no good indices in this array.
 
Constraints:
    1. n == nums.length
    2. 3 <= n <= 105
    3. 1 <= nums[i] <= 106
    4. 1 <= k <= n / 2
'''
# === 2439ms && 30.7MB === #
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        lcnt, rcnt = [1 for _ in range(n)], [1 for _ in range(n)]
        for i in range(n-1):
            if nums[i+1] <= nums[i]:
                lcnt[i+1] = lcnt[i]+1
            if nums[n-1-i] >= nums[n-2-i]:
                rcnt[n-2-i] = rcnt[n-1-i]+1
        
        return [i for i in range(k, n-k) if lcnt[i-1] >= k and rcnt[i+1] >= k]