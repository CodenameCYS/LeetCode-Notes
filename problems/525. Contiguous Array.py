'''
=== 525. Contiguous Array ===

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
    Input: [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
'''
# === 940ms(48.63%) && 20.6MB(16.67%) === #
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = 0
        memory = {0:[0]}
        for i,n in enumerate(nums):
            s = s + 1 if n == 0 else s -1
            if s in memory.keys():
                memory[s].append(i+1)
            else:
                memory[s] = [i+1]
        length = 0
        for k,v in memory.items():
            if v[-1] - v[0] > length:
                length = v[-1] - v[0]
        return length