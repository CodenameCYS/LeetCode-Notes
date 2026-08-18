'''
=== 1493. Longest Subarray of 1's After Deleting One Element ===

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.

Example 1:
    Input: nums = [1,1,0,1]
    Output: 3
    Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:
    Input: nums = [0,1,1,1,0,1,1,0,1]
    Output: 5
    Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:
    Input: nums = [1,1,1]
    Output: 2
    Explanation: You must delete one element.
Example 4:
    Input: nums = [1,1,0,0,1,1,1,0,1]
    Output: 4
Example 5:
    Input: nums = [0,0,0]
    Output: 0
 
Constraints:
    1. 1 <= nums.length <= 10^5
    2. nums[i] is either 0 or 1.
'''
# === 388ms(89.42%) && 16.3MB === #
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        counter = []
        while i < n:
            count = 0
            while i < n and nums[i] == 1:
                count += 1
                i += 1
            counter.append(count)
            count = 0
            while i < n and nums[i] == 0:
                count += 1
                i += 1
            counter.append(count)
        # print(counter)
        if len(counter) == 2:
            return counter[0] if counter[1] != 0 else counter[0]-1
        counter.append(0)
        ans = max(counter[i] for i in range(0, len(counter), 2))
        for i in range(1, len(counter), 2):
            if counter[i] == 1:
                ans = max(ans, counter[i-1] + counter[i+1])
        return ans