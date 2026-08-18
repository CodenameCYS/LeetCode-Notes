'''
=== 1512. Number of Good Pairs ===

Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:
    Input: nums = [1,1,1,1]
    Output: 6
    Explanation: Each pair in the array are good.
Example 3:
    Input: nums = [1,2,3]
    Output: 0
 
Constraints:
    1. 1 <= nums.length <= 100
    2. 1 <= nums[i] <= 100
'''
# === 32ms && 13.9MB === #
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        ans = 0
        for n in counter.values():
            ans += n*(n-1)//2
        return ans