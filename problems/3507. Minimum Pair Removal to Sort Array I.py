'''
=== 3507. Minimum Pair Removal to Sort Array I ===

Given an array nums, you can perform the following operation any number of times:
    - Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
    - Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.
An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

Example 1:
    Input: nums = [5,2,3,1]
    Output: 2
    Explanation:
    The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
    The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
    The array nums became non-decreasing in two operations.
Example 2:
    Input: nums = [1,2,2]
    Output: 0
    Explanation:
    The array nums is already sorted.

Constraints:
    1. 1 <= nums.length <= 50
    2. -1000 <= nums[i] <= 1000
'''
# === 11ms && 17.6MB === #
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        status = (n <= 1 or all(nums[i] <= nums[i+1] for i in range(n-1)))
        while status == False:
            s = nums[0] + nums[1]
            idx = 0
            for i in range(1, n-1):
                if nums[i] + nums[i+1] < s:
                    idx = i
                    s = nums[i] + nums[i+1]
            nums.pop(idx)
            nums[idx] = s
            n -= 1
            status = (n <= 1 or all(nums[i] <= nums[i+1] for i in range(n-1)))
            ans += 1
        return ans