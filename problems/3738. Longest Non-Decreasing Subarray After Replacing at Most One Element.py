'''
=== 3738. Longest Non-Decreasing Subarray After Replacing at Most One Element ===

You are given an integer array nums.
You are allowed to replace at most one element in the array with any other integer value of your choice.
Return the length of the longest non-decreasing subarray that can be obtained after performing at most one replacement.
A subarray is a contiguous sequence of elements within an array.
An array is said to be non-decreasing if each element is greater than or equal to its previous one (if it exists).

Example 1:
    Input: nums = [1,2,3,1,2]
    Output: 4
    Explanation:
    Replacing nums[3] = 1 with 3 gives the array [1, 2, 3, 3, 2].
    The longest non-decreasing subarray is [1, 2, 3, 3], which has a length of 4.
Example 2:
    Input: nums = [2,2,2,2,2]
    Output: 5
    Explanation:
    All elements in nums are equal, so it is already non-decreasing and the entire nums forms a subarray of length 5.

Constraints:
    1. 1 <= nums.length <= 105
    2. -109 <= nums[i] <= 109​​​​​​​
'''
# === 615ms && 37.17MB === #
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        s1 = [1 for _ in range(n)]
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                s1[i] = s1[i+1] + 1
        s2 = [1 for _ in range(n)]
        for i in range(n-1):
            if nums[i] <= nums[i+1]:
                s2[i+1] = 1 + s2[i]
        s3 = [1 for _ in range(n)]
        s3[0] = s1[1] + 1
        s3[-1] = s2[-2] + 1
        for i in range(1, n-1):
            if nums[i-1] <= nums[i+1]:
                s3[i] = s2[i-1] + 1 + s1[i+1]
            else:
                s3[i] = max(s2[i-1], s1[i+1]) + 1
        return max(max(x, y, z) for x, y, z in zip(s1, s2, s3))