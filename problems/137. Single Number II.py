'''
=== 137. Single Number II ===
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
'''
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        records = {}
        for num in nums:
            if num not in records.keys():
                records[num] = 1
            elif records[num] == 2:
                del records[num]
            else:
                records[num] += 1
        ans = list(records.keys())[0]
        return ans

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((3*sum(set(nums))-sum(nums))/2)
        