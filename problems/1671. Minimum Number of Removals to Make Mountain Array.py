'''
=== 1671. Minimum Number of Removals to Make Mountain Array ===

You may recall that an array arr is a mountain array if and only if:
    - arr.length >= 3
    - There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

Example 1:
    Input: nums = [1,3,1]
    Output: 0
    Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:
    Input: nums = [2,1,1,5,6,2,3,1]
    Output: 3
    Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
Example 3:
    Input: nums = [4,3,2,1,1,2,3,1]
    Output: 4
Example 4:
    Input: nums = [1,2,3,4,4,3,2,1]
    Output: 1
 
Constraints:
    1. 3 <= nums.length <= 1000
    2. 1 <= nums[i] <= 109
    3. It is guaranteed that you can make a mountain array out of nums.
'''
# === 4192ms && 14.5MB === #
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lcount = [0 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lcount[i] = max(lcount[i], lcount[j] + 1)
                    
        rcount = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    rcount[i] = max(rcount[i], rcount[j] + 1)
        
        ans = n
        for i in range(n):
            if lcount[i] != 0 and rcount[i] != 0:
                ans = min(ans, n-(1+lcount[i]+rcount[i]))
        return ans