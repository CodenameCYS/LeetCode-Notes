'''
=== 491. Increasing Subsequences ===

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

Example:
    Input: [4, 6, 7, 7]
    Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 
Note:
    1. The length of the given array will not exceed 15.
    2. The range of integer in the given array is [-100,100].
    3. The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
'''
# === 520ms(5.29%) && 19.8MB(100%) === #
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2, len(nums)+1):
            for x in set(itertools.combinations(nums, i)):
                if all(a <= b for a,b in zip(x[:-1], x[1:])):
                    ans.append(x)
        return ans