'''
=== 697. Degree of an Array ===

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
    Input: [1, 2, 2, 3, 1]
    Output: 2
    Explanation: 
    The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.
Example 2:
    Input: [1,2,2,3,1,4,2]
    Output: 6

Note:
    1. nums.length will be between 1 and 50,000.
    2. nums[i] will be an integer between 0 and 49,999.
'''
# === 244ms(76.57%) && 15.2MB(9.09%) === #
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        counter = {}
        for i,n in enumerate(nums):
            if n in counter.keys():
                counter[n].append(i)
            else:
                counter[n] = [i]
        counter = sorted(counter.items(), key = lambda x: (-len(x[1]), x[1][-1]-x[1][0]))
        # print(counter)
        return counter[0][1][-1] - counter[0][1][0] + 1