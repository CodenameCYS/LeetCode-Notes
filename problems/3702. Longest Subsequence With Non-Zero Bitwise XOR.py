'''
=== 3702. Longest Subsequence With Non-Zero Bitwise XOR ===

You are given an integer array nums.
Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.
A subsequence is a non-empty array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: nums = [1,2,3]
    Output: 2
    Explanation:
    One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.
Example 2:
    Input: nums = [2,3,4]
    Output: 3
    Explanation:
    The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.

Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i] <= 109
'''
# === 429ms && 53.72MB === #
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        locs = defaultdict(list)
        xor = 0
        ans = 0
        st = -1
        for i, num in enumerate(nums):
            xor = xor ^ num
            if xor != 0:
                if st == -1:
                    st = i
                ans = max(ans, i+1)
            elif st != -1:
                ans = max(ans, i-st)
            locs[xor].append(i+1)
        return ans
# === 157ms && 33.33MB === #
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        ans = 0
        st = -1
        for i, num in enumerate(nums):
            xor = xor ^ num
            if xor != 0:
                if st == -1:
                    st = i
                ans = max(ans, i+1)
            elif st != -1:
                ans = max(ans, i-st)
        return ans