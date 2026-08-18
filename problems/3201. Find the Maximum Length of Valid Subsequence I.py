'''
=== 3201. Find the Maximum Length of Valid Subsequence I ===

You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:
    - (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 4
    Explanation:
    The longest valid subsequence is [1, 2, 3, 4].
Example 2:
    Input: nums = [1,2,1,1,2,1,2]
    Output: 6
    Explanation:
    The longest valid subsequence is [1, 2, 1, 2, 1, 2].
Example 3:
    Input: nums = [1,3]
    Output: 2
    Explanation:
    The longest valid subsequence is [1, 3].

Constraints:
    1. 2 <= nums.length <= 2 * 105
    2. 1 <= nums[i] <= 107
'''
# === 632ms && 39.6MB === #
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        n1 = len([x for x in nums if x % 2 == 0])
        n2 = len([x for x in nums if x % 2 == 1])
        n3, tgt = 0, 0
        for x in nums:
            if x % 2 == tgt:
                n3 += 1
                tgt = 1-tgt
        n4, tgt = 0, 1
        for x in nums:
            if x % 2 == tgt:
                n4 += 1
                tgt = 1-tgt
        return max(n1, n2, n3, n4)