'''
=== 229. Majority Element II ===

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
    Input: [3,2,3]
    Output: [3]
Example 2:
    Input: [1,1,1,3,3,2,2,2]
    Output: [1,2]
'''
# === 52ms(51.53) & 13.9MB(7.61%) === #
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        memory = {}
        for a in nums:
            if a not in memory.keys():
                memory[a] = 1
            else:
                memory[a] += 1
        s = int(len(nums)/3)
        ans = [k for k,v in memory.items() if v > s]
        return ans