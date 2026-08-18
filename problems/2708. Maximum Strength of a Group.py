'''
=== 2708. Maximum Strength of a Group ===

You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].
Return the maximum strength of a group the teacher can create.

Example 1:
    Input: nums = [3,-1,-5,2,5,-9]
    Output: 1350
    Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
Example 2:
    Input: nums = [-4,-5,-4]
    Output: 20
    Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.
 
Constraints:
    1. 1 <= nums.length <= 13
    2. -9 <= nums[i] <= 9
'''
# === 77ms && 16.4MB === #
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        have_zero = 0 in nums
        if len(pos) == 0 and len(neg) <= 1:
            return 0 if have_zero else neg[0]
        
        s = 1
        for x in pos:
            s *= x
        neg = sorted(neg)
        for x in neg[:(len(neg) // 2) * 2]:
            s *= x
        return s
        
        